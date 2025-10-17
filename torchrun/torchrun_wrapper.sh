#!/bin/bash
### torchrun wrapper for SLURM

source /raid/lincy/ENV/torch/bin/activate

## Set single thread to avoid pytorch warning
export OMP_NUM_THREADS=1

## Set the first alocated host to be the master (port # can be arbitrary)
export MASTER_ADDR=$(scontrol show hostname ${SLURM_NODELIST} | head -n 1)

## - Each torchrun per node has an unique node-rank ${SLURM_NODEID}
## - Torchrun forks one processs per GPU: '--nproc_per_node=gpu'
torchrun --nnodes=${SLURM_NNODES}    \
         --node-rank=${SLURM_NODEID} \
         --nproc_per_node=gpu \
         --master-addr=${MASTER_ADDR} --master-port=11024 \
         comm.py

