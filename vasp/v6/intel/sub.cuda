#!/bin/bash
#SBATCH -A GOV109092
#SBATCH --nodes=1 --ntasks-per-node=${NGPU} --cpus-per-task=4
#SBATCH --gres=gpu:${NGPU}
 
module purge
module load intel/2020 nvidia/cuda/10.1
export I_MPI_PMI_LIBRARY=/lib64/libpmi.so
export I_MPI_OFI_PROVIDER=mlx
srun --cpu_bind=v,cores /home/p00lcy01/VASP/b_intel/bin/vasp_gpu
echo "== Wall time: ${SECONDS} secs"
