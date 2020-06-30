### Compile VASP on Twnia-2

* ```makefile.include```: The makefile for VASP 5.4.4+patch.5.4.4.16052018.gz on Twnia-2
* See ```gocom``` on how to compile the VASP on Twnia-2
* Job script example: ```vasp.slurm```


### Compiler issues:
1. VASP 5 + CUDA-10.0 do not compile with intel/2020, use intel/2018 instead. 
```
/opt/ohpc/pub/nvidia/cuda/cuda-10.0/include/crt/host_config.h(89): error: #error directive: -- unsupported ICC configura
tion! Only ICC 15.0, ICC 16.0, ICC 17.0 and ICC 18.0 on Linux x86_64 are supported!
  #error -- unsupported ICC configuration! Only ICC 15.0, ICC 16.0, ICC 17.0 and ICC 18.0 on Linux x86_64 are supported!
```
1. Contiguous pointer from non-contiguous target in Gcc8: See https://www.vasp.at/forum/viewtopic.php?f=2&t=17792


### Reference:
* [GPU_port_of_VASP](https://www.vasp.at/wiki/index.php/GPU_port_of_VASP)
* [A commercial service of VASP by ExaByte.io](https://docs.exabyte.io/tutorials/dft/electronic/overview/)




