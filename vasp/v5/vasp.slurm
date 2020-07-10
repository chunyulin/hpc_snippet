#!/bin/bash
#SBATCH -A GOV108008
#SBATCH -J vasp
#SBATCH --nodes=1 --ntasks-per-node=32 --cpus-per-task=1
#SBATCH --ntasks-per-socket=16    ###  evenly place 32 rank into each socket
#SBATCH --gres=gpu:8
#SBATCH --time=24:30:00

export I_MPI_PMI_LIBRARY=/lib64/libpmi.so

module purge
module load compiler/intel/2018
module load nvidia/cuda/10.0

VASP_EXE=/home/p00lcy01/VASP/icc_mkl/bin/vasp_std

OPTION="--cpu_bind=core"

srun ${OPTION} ${VASP_EXE}

echo "=== Wall time: $SECONDS secs."


