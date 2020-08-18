### Compile VASP.6 on Twnia-2

* VASP 6 support GPU via PGI compiler and OpenACC, which might have long-term support for VASP on GPU.
* We have prepare most of prerequest such as OpenMPI and PGI QD lib in ```/opt/ohpc/pkg/qchem```. So you could complile your own VASP binary simply by the provided script here.
* To compile OpenACC version, please check out script in ```v6/pgi```: copy the vasp makefile ```makefile.include``` into your vasp scource and run compiltion script by ```. ./gocom```.
* Job script example: ```vasp.slurm```

### Preliminary [testing results](https://docs.google.com/spreadsheets/d/1NJ5DjBFuAiLij8Sc5XTnC0TvKyMY-4YPJ8q7jN8ARbk/edit#gid=525954215) for [the three cases from NVIDIA](https://github.com/smaintz-nv/gpu-vasp-files)
