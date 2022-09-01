from mpi4py import MPI
import numpy as np

if __name__ == "__main__":

    world_comm = MPI.COMM_WORLD
    world_size = world_comm.Get_size()
    my_rank = world_comm.Get_rank()
    
    N = 1024*1024

    ##
    ## decide mpi geometry
    my_size = (N // world_size)
    my_start = my_size *  my_rank
    my_end   = my_size * (my_rank+1)
    if my_rank == world_size-1:
        my_end = N
        my_size = my_end - my_start
       
        
    print("I am rank {} in {}, processing array index from {} to {}.".format(my_rank, world_size, my_start, my_end))

    ##
    ## init array on each rank
    ##
    a = np.ones( my_size )
    b = np.ones( my_size )
    
    ##
    ## take average
    ##
    world_comm.Barrier()
    t0 = MPI.Wtime()
    if my_rank == 0:
        total_sum = np.sum(a*b)
        for i in range( 1, world_size ):
            sub_sum = np.empty( 1 )
            world_comm.Recv( [sub_sum, MPI.DOUBLE], source=i, tag=99 )
            total_sum += sub_sum[0]
        average = total_sum / N
        t1 = MPI.Wtime()
        print("Average: {}".format(average))
        print("-- Sum {} items take {} secs.".format(N, t1-t0))

    else:
        sub_sum = np.array( [np.sum(a*b)] )
        world_comm.Send( [sub_sum, MPI.DOUBLE], dest=0, tag=99 )


    MPI.Finalize()