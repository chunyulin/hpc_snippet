# Quick start of mpi4py with HDF5 on T3

## Prepare your virtual env on T3 from existing python installation
```
module load biology/Python/3.9.5
python3 -m venv ~/sandbox

module load compiler/intel/2020u4 OpenMPI/4.1.1
source ~/sandbox/bin/activate
pip install numpy mpi4py h5py
deactivate
```

## "Hello world" for mpi4py

- Prepare mpi4py code. For example, `mpi.py` just calculating the sum of inner product of two vector and taking the average.
- Submit the job to SLURM by `sbatch mpi.sub`.
- You will notice that the walltime is reduced by increasing the MPI tasks.

See the official document of [MPI for Python](https://mpi4py.readthedocs.io/en/stable/) for more information.

## "Hello world" for HDF5
- Install `h5py` in your existing virtual env:
```
module load compiler/intel/2020u4 OpenMPI/4.1.1
source ~/sandbox/bin/activate
pip install numpy h5py
deactivate
```
- Submit the sample code by `sbatch h5.sub`.
