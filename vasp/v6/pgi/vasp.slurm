#!/bin/bash
#SBATCH -A GOV109092
#SBATCH -J vasp_acc
#SBATCH --nodes=1 --cpus-per-task=4         #### Change the number of nodes. It's safe to use --cpus-per-task=4
#SBATCH --ntasks-per-node=2 --gres=gpu:2    #### GPU number per node (can be 1-8).

module purge
module load pgi/2020 nvidia/cuda/10.1
source /opt/ohpc/pkg/qchem/pgi/openmpi-3.1.6/vasp.sh

srun --cpu_bind=v <your vasp bin folder>/vasp_std
