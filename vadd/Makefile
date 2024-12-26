
##CUDIR   := /work/d07222009/NVIDIA_HPC_SDK/nvidia_hpc_sdk/Linux_x86_64/24.11/cuda/12.6

CC      := nvc
CFLAGS  := -O3 -Wall -g -std=c++11
CPP     := nvc++
#NVCC    := $(CUDIR)/bin/nvcc
NVCC    := nvcc

NVFLAGS_ARCH := -arch=compute_90 -code=sm_90,compute_90
NVFLAGS := -O3 -Xptxas -v -std=c++11

LDFLAGS := -lm

exec=VecAdd

all: $(exec)

$(exec): $(exec).cu
	$(NVCC) $(NVFLAGS) -Xcompiler -fopenmp -dc $<
	$(NVCC) $(LDFLAGS) $(NVFLAGS_ARCH) $(exec).o -o $@ -g -lgomp

clean:
	rm -f *.o ${exec}
