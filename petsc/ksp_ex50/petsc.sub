#!/bin/bash
#PBS -P GOV109092       ### Yours account ID
#PBS -q ctest
#PBS -l select=1:ncpus=4:mpiprocs=4
#PBS -N petsc_test
#PBS -j oe

cd $PBS_O_WORKDIR

module purge
module load python3/3.5.6
module load intel/2018_u1
export I_MPI_PIN=1
export PETSC_DIR=/pkg/kagra/intel/petsc-3.18.2
export LD_LIBRARY_PATH=${PETSC_DIR}/lib:${LD_LIBRARY_PATH}


MPIRUN="mpiexec -PSM2 -print-rank-map"

${MPIRUN} -np 4 ./ex50 -da_grid_x 1025 -da_grid_y 1025 -pc_type mg -pc_mg_levels 9 -ksp_monitor
