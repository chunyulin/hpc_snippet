# Use PETSc on Twnia-1

- PETSc has been installed with Metis on T1. Location: `/pkg/kagra/intel/petsc-3.18.2`.
- Submit an example job from the [official tutorial](https://petsc.org/release/tutorials/handson/#handson-example-1) by:
```
git clone https://github.com/chunyulin/hpc_snippet.git
cd hpc_snippet/petsc/ksp_ex50
. ./gocom
qsub petsc.sub
```
- You can check if your output file are similar to the sample one `petsc_test.o5146928`
- If you are interested in how to build PETSc from the source, run `cat /pkg/kagra/intel/petsc-3.18.2/gocom`.
