### Toolchains status

|               | Intel             |  gnu/MKL | PGI |
| ------------- | ----------------- | ----- | ------ |
| VASP6 CPU     | segf (except r32) |  OK   |       |
| VASP6 cuda    | OK                |  OK    |       |
| VASP6 ACC     |  -                |  -      |  ?  |


### Compile VASP on Twnia-2

* ```makefile.include```: The makefile for VASP 5.4.4+patch.5.4.4.16052018.gz on Twnia-2
* See ```gocom``` on how to compile the VASP on Twnia-2
* Job script example: ```vasp.slurm```


### Some compiling issues:
* Segment fault with `-DUSE_PINNED_MEMORY` when compiled VASP 6 CUDA.
* Segment fault when compiled VASP 6 with Scalapack.
```
[gn1221:135789:0:135789] Caught signal 11 (Segmentation fault: address not mapped to object at address 0x440000f8)
==== backtrace (tid: 135760) ====
 0 0x0000000000069d80 PMPI_Comm_set_name()  ???:0
 1 0x0000000000069d80 PMPI_Comm_size()  /tmp/lin/openmpi-4.0.4/ompi/mpi/c/profile/pcomm_size.c:63
 2 0x0000000000029e39 MKLMPI_Comm_size()  ???:0
 3 0x0000000000028001 mkl_blacs_init()  ???:0
 4 0x0000000000027f48 Cblacs_pinfo()  ???:0
 5 0x000000000001882f blacs_gridmap_()  ???:0
 6 0x000000000001820e blacs_gridinit_()  ???:0
 7 0x00000000004469d4 __scala_MOD_procmap()  ???:0
 8 0x0000000000447786 __scala_MOD_init_scala_desc()  ???:0
 9 0x0000000000448ddd __scala_MOD_pdssyex_zheevx()  ???:0
10 0x00000000008ad929 __david_MOD_eddav()  ???:0
11 0x00000000008dd364 elmin_()  ???:0
12 0x0000000000e2d0ad electronic_optimization.4325()  main.f90:0
13 0x0000000000e1501f MAIN__()  main.f90:0
14 0x0000000000e2d72e main()  ???:0
15 0x0000000000022445 __libc_start_main()  ???:0
16 0x000000000040837f _start()  ???:0
=================================

Program received signal SIGSEGV: Segmentation fault - invalid memory reference.
```
* VASP 5 + CUDA-10.0 do not compile with intel/2020, use intel/2018 instead. 
```
/opt/ohpc/pub/nvidia/cuda/cuda-10.0/include/crt/host_config.h(89): error: #error directive: -- unsupported ICC configura
tion! Only ICC 15.0, ICC 16.0, ICC 17.0 and ICC 18.0 on Linux x86_64 are supported!
  #error -- unsupported ICC configuration! Only ICC 15.0, ICC 16.0, ICC 17.0 and ICC 18.0 on Linux x86_64 are supported!
```
* VASP5 + CUDA-10.1 do not compile with sm7.0 as `warning : Instruction 'shfl' without '.sync' is deprecated`.
* Contiguous pointer from non-contiguous target in Gcc 8. Use gcc 7 instead as it may be a compiler issue. See https://www.vasp.at/forum/viewtopic.php?f=2&t=17792
* CUDA SM70 deprecate 'shfl' without '.sync': `warning : Instruction 'shfl' without '.sync' is deprecated since PTX ISA version 6.0 and will be discontinued in a future PTX ISA version`

### Reference:
* [GPU_port_of_VASP](https://www.vasp.at/wiki/index.php/GPU_port_of_VASP)
* [A commercial service of VASP by ExaByte.io](https://docs.exabyte.io/tutorials/dft/electronic/overview/)




