### Compile VASP.6 on Twnia-2

* VASP 6 support GPU via OpenACC, which might have long-term support for VASP-GPU compared to CUDA version.
* We prepared most of prerequests such as OpenMPI and Scalapack in ```/opt/ohpc/pkg/qchem```. So you could simply complile your own VASP binary by copying ```makefile.include*``` into your vasp source folder and running the compilation script ```. ./gocom```.
* Job submission script is in ```vasp.slurm```.


### Performance note
* The tests of VASP GPU on Twnia-2 seems not as fast as [NVidia's result](https://news.developer.nvidia.com/nvidia-gpu-accelerated-vasp-6-uses-openacc-to-deliver-15x-more-performance/). We are still trying to workaround that and we appreciate any suggestion from users.
* For some small cases, we see VASP/OpenACC can be 3x faster than CUDA version. However, the actual performance seems highly depend on the problem type and size.
* Preliminary [testing results](https://docs.google.com/spreadsheets/d/1NJ5DjBFuAiLij8Sc5XTnC0TvKyMY-4YPJ8q7jN8ARbk/edit#gid=525954215) for [the three cases from NVIDIA](https://github.com/smaintz-nv/gpu-vasp-files)
* We tested with the latest VASP 6.1.2.
