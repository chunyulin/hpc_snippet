### Compile VASP.6 on Twnia-2

* VASP 6 support GPU via OpenACC, which might have long-term support for VASP-GPU compared to CUDA version.
* We prepare most of prerequests such as OpenMPI and PGI QD lib in ```/opt/ohpc/pkg/qchem```. So you could simplt complile your own VASP binary by the provided script here.
* To compile OpenACC version, please check out script in ```v6/pgi```: copy the vasp makefile ```makefile.include``` into your vasp scource and run compiltion script by ```. ./gocom```.
* Job script example: ```vasp.slurm```. If it compules and runs successfully, you should see the output like
```
 running on    8 total cores
 distrk:  each k-point on    8 cores,    1 groups
 distr:  one band on    1 cores,    8 groups
 using from now: INCAR.....
 OpenACC runtime initialized ...    8 GPUs detected
 vasp.6.1.2 22Jul20 (build Aug 16 2020 22:44:56) gamma-only......................
```


### Performance note
* The tests of VASP GPU on Twnia-2 seems not as fast as [NVidia's result](https://news.developer.nvidia.com/nvidia-gpu-accelerated-vasp-6-uses-openacc-to-deliver-15x-more-performance/). We are still trying to workaround that and we appreciate any suggestion from users.
* For some small cases, we see VASP/OpenACC can be 3x faster than CUDA version. However, the actual performance seems highly depend on the problem type and size.
* Preliminary [testing results](https://docs.google.com/spreadsheets/d/1NJ5DjBFuAiLij8Sc5XTnC0TvKyMY-4YPJ8q7jN8ARbk/edit#gid=525954215) for [the three cases from NVIDIA](https://github.com/smaintz-nv/gpu-vasp-files)
* We tested with the latest VASP 6.1.2.
