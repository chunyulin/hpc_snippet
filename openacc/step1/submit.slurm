#! /bin/bash
#SBATCH -A GOV108017
#SBATCH -J acc_test
#SBATCH -p gtest
#SBATCH --nodes=1 --ntasks-per-node=1 --cpus-per-task=4
#SBATCH --gres=gpu:1
#SBATCH --time=0:20:00

module purge
module load pgi/2020

srun ./laplace2d_acc
srun ./laplace2d_omp

