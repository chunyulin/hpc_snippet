### Compile VASP.6 on Twnia-2

* VASP 6 support GPU via PGI compiler and OpenACC, which might have long-term support for VASP on GPU.
* To compile OpenACC version, copy ```makefile.include*``` in ```v6/pgi``` into your vasp source folder and run ```gocom```.
* Job script example: ```vasp.slurm```

### Preliminary [testing results](https://docs.google.com/spreadsheets/d/1NJ5DjBFuAiLij8Sc5XTnC0TvKyMY-4YPJ8q7jN8ARbk/edit#gid=525954215) for [the three cases from NVIDIA](https://github.com/smaintz-nv/gpu-vasp-files)
