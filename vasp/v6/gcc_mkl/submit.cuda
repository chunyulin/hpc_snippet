#!/bin/bash
#SBATCH --nodes=1 --ntasks-per-node=2 --cpus-per-task=4
#SBATCH --gres=gpu:2
 
module purge
module load gnu7/7.3.0
module load nvidia/cuda/10.1
source /home/p00lcy01/local/gcc7/openmpi-4.0.4/env.sh

srun --cpu_bind=v /home/p00lcy01/VASP/b_gcc_mkl/bin/vasp_gpu
echo "== Wall time: ${SECONDS} secs"
