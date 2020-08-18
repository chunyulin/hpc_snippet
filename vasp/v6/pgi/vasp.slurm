#!/bin/bash
#SBATCH -A GOV109092                        #### Change to your project ID
#SBATCH -J vasp_acc
#SBATCH --nodes=1                           #### Number of nodes.
#SBATCH --ntasks-per-node=2 --gres=gpu:2    #### Number of MPI tasks and GPU number per node. They are the same usually and can be from 1-8. 
#SBATCH --cpus-per-task=4                   #### Threads per MPI task. It's safe to use 4 for vasp.

module purge
module load pgi/2020 nvidia/cuda/10.1
source /opt/ohpc/pkg/qchem/pgi/openmpi-3.1.6/vasp.sh

srun --cpu_bind=v <your vasp bin folder>/vasp_std
