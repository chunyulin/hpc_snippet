import os
import torch
import torch.distributed as dist

def dist_isendrecv():
    rank = dist.get_rank()
    world_size = dist.get_world_size()
    tensor = torch.tensor([rank + 1.0]).cuda()

    next_rank = (rank + 1) % world_size
    prev_rank = (rank - 1 + world_size) % world_size

    recv_tensor = torch.zeros_like(tensor)

    req_send = dist.isend(tensor, dst=next_rank)
    req_recv = dist.irecv(recv_tensor, src=prev_rank)

    req_send.wait()
    req_recv.wait()

    print(f"Non-blocking P2P: Rank {rank} received {recv_tensor.item()} from rank {prev_rank}")

def dist_sendrecv():
    rank = dist.get_rank()
    world_size = dist.get_world_size()

    tensor = torch.tensor([rank + 1.0]).cuda()

    next_rank = (rank + 1) % world_size
    prev_rank = (rank - 1 + world_size) % world_size

    # even ranks send first, odd ranks recv first
    if rank % 2 == 0:
        dist.send(tensor, dst=next_rank)
        recv_tensor = torch.zeros_like(tensor)
        dist.recv(recv_tensor, src=prev_rank)
        print(f"Blocking P2P: Rank {rank} received {recv_tensor.item()} from rank {prev_rank}")
    else:
        recv_tensor = torch.zeros_like(tensor)
        dist.recv(recv_tensor, src=prev_rank)
        print(f"Blocking P2P: Rank {rank} received {recv_tensor.item()} from rank {prev_rank}")
        dist.send(tensor, dst=next_rank)


def dist_all2all():
    rank = dist.get_rank()
    world_size = dist.get_world_size()

    send_tensor = torch.ones(world_size).cuda() * (rank+1)
    recv_tensor = torch.zeros_like(send_tensor).cuda()

    dist.all_to_all_single(recv_tensor, send_tensor, async_op=True)

    print(f"A2A: Rank {rank} recv_tensor:\n{recv_tensor}")


def dist_gather():
    rank = dist.get_rank()
    world_size = dist.get_world_size()

    tensor = torch.tensor([rank+1, 10.0], dtype=torch.float32).cuda()
    if dist.get_rank() == 0:
        gather_list = [torch.zeros_like(tensor).cuda() for i in range(world_size)]
    else:
        gather_list = None
    dist.gather(tensor, gather_list, dst=0, async_op=True )

    print(f"Gather, rank: {rank}, before gather: {tensor} after gather: {gather_list}")

def dist_broadcast():
    rank = dist.get_rank()
    world_size = dist.get_world_size()

    tensor = torch.ones(world_size, dtype=torch.int64).cuda() if rank == 0 else torch.zeros(world_size, dtype=torch.int64).cuda()
    before_tensor = tensor.clone()
    dist.broadcast(tensor, src=0)
    print(f"Broadcast, rank: {rank}, before broadcast tensor: {before_tensor} after broadcast tensor: {tensor}")

def dist_reduce():
    rank = dist.get_rank()
    world_size = dist.get_world_size()

    tensor = torch.tensor([rank+ 1], dtype=torch.float32, device=lrank)
    before_tensor = tensor.clone()

    dist.reduce(tensor, op=dist.ReduceOp.SUM, dst=0)

    print(f"Reduce, rank: {rank}, before reduce: {before_tensor} after reduce: {tensor}")

def dist_allreduce():
    rank = dist.get_rank()
    tensor = torch.tensor([rank+1, 10*rank+1]).cuda()
    input_tensor = tensor.clone()
    dist.all_reduce(tensor)

    print(f"All_reduce, rank: {rank}, before allreduce tensor: {input_tensor}, after allreduce tensor: {tensor}")

def dist_allgather():
    rank = dist.get_rank()
    world_size = dist.get_world_size()

    input_tensor = torch.tensor([rank]).cuda()
    tensor_list = [torch.zeros(1, dtype=torch.int64).cuda()  for _ in range(world_size)]
    dist.all_gather(tensor_list, input_tensor)
    print(f"Allgather, rank: {rank}, input_tensor: {input_tensor}, output: {tensor_list}")

def dist_reducescatter():
    rank = dist.get_rank()
    world_size = dist.get_world_size()

    output = torch.empty(2, dtype=torch.float32).cuda()
    output_old = output.clone()

    input_list = [ torch.tensor([i+1,2], dtype=torch.float32).cuda() for i in range(world_size)]
    dist.reduce_scatter(output, input_list, op=dist.ReduceOp.SUM)   ## zeros if len(input_list) < work_size
    print(f"Reduce_scatter, rank: {rank}, old_output: {output_old}, outputr: {output}")

def dist_scatter():
    rank = dist.get_rank()
    world_size = dist.get_world_size()

    tensor = torch.zeros(1, device='cuda')
    before_tensor = tensor.clone()
    scatter_list  = [ torch.ones(1).cuda() * (i+1) for i in range(world_size)] if rank == 0 else None

    dist.scatter(tensor, scatter_list, src=0, async_op=True)
    print(f"Scatter, rank: {rank}, before scatter: {before_tensor} after scatter: {tensor}")

def nodereport():
    rank = dist.get_rank()
    world_size = dist.get_world_size()
    local_rank = int(os.environ["LOCAL_RANK"])   # GPU index on this node
    node_rank = int(os.environ.get("SLURM_NODEID", -1))
    node_name = os.uname()[1]
    print(f"[Node: {node_name} {node_rank}] Global rank {rank}/{world_size} using GPU {local_rank}")

if __name__ == "__main__":
    lrank = int(os.environ["LOCAL_RANK"])
    torch.cuda.set_device(lrank)
    #torch.accelerator.set_device_index(lrank)
    acc = torch.accelerator.current_accelerator()
    backend = torch.distributed.get_default_backend_for_device(acc)
    dist.init_process_group(backend)
    rank = dist.get_rank()
    if rank==0: print("Backend: ", backend)

    nodereport()
    dist.barrier(device_ids=[lrank])


    test_list = [ dist_sendrecv, dist_isendrecv, 
                  dist_scatter,  dist_reducescatter,
                  dist_reduce,   dist_allreduce,
                  dist_gather,   dist_allgather,
                  dist_broadcast ]

    for f in test_list:
        if rank==0: print(f"Testing {f.__name__} ----------------------------------------------------")
        dist.barrier(device_ids=[lrank])
        try:
           f()
        except Exception as e:
           print(f"Skipping {f.__name__} due to exception: {e}")

        dist.barrier(device_ids=[lrank])
        if rank==0: print("\n\n\n")

    dist.destroy_process_group()

