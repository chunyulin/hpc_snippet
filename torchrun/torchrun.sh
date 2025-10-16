#!/bin/bash
### torchrun wrapper for SLURM

source /raid/lincy/ENV/torch/bin/activate

export OMP_NUM_THREADS=1
export MASTER_ADDR=$(scontrol show hostname ${SLURM_NODELIST} | head -n 1)
TORCHRUN="torchrun --nnodes=${SLURM_NNODES} --node-rank=${SLURM_NODEID} --nproc_per_node=gpu
                   --master-addr ${MASTER_ADDR} --master-port 11024"

${TORCHRUN} comm.py

