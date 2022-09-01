# Quick start of mpi4py on T3

- Setup your virtual env on T3 from any python installation
```
module load biology/Python/3.9.5
python3 -m venv ~/myenv

module load compiler/intel/2020u4 OpenMPI/4.1.1
source ~/myenv/bin/activate
pip install numpy mpi4py
deactivate
```
- Prepare your mpi4py code. For example, `mpi.py` just calculating the sum of inner product of two vector and taking the average.
- Submit the job to SLURM by `sbatch mpi4py.sub`.
- You will notice that the walltime is reduced by increasing the MPI tasks.

See the official document of [MPI for Python](https://mpi4py.readthedocs.io/en/stable/) for more information.
