# Quick start of mpi4py on T3

## Setup your virtual env on T3 from existing python installation
```
module load biology/Python/3.9.5
python3 -m venv ~/sandbox

module load compiler/intel/2020u4 OpenMPI/4.1.1
source ~/sandbox/bin/activate
pip install numpy mpi4py
deactivate
```

## "Hello world" for mpi4py

- Prepare mpi4py code. For example, `mpi.py` just calculating the sum of inner product of two vector and taking the average.
- Submit the job to SLURM by `sbatch mpi.sub`.
- You will notice that the walltime is reduced by increasing the MPI tasks.

See the official document of [MPI for Python](https://mpi4py.readthedocs.io/en/stable/) for more information.


## Install h5py into your python env:

- Based on HDF5 1.12.2 / Intel compiler 2020 / OpenMPI 4.1.1
```
module purge
module load biology/Python/3.9.5
source ~/sandbox/bin/activate
module load compiler/intel/2020u4 OpenMPI/4.1.1

CC=mpicc HDF5_DIR=/opt/ohpc/Taiwania3/libs/i2020-Ompi411/hdf5-1.12.2  HDF5_MPI=ON pip install --no-binary=h5py h5py
```

## Example of MPI-IO in h5py

- Submit the sample code `sbatch h5mpi.sub`.
