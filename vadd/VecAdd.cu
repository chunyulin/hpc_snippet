#include <cstdio>
#include <cstdlib>
#include <random>
#include <vector>
#include <cuda_runtime.h>
#include <omp.h>

using namespace std;

/*
 * Retrieve device IDs for all CUDA devices in the current system.
 */
int getAllGpus(int **gid)
{
    int i;
    int nGpus;

    cudaGetDeviceCount(&nGpus);

    *gid = (int *)malloc(sizeof(int) * nGpus);

    for (i = 0; i < nGpus; i++)
    {
        (*gid)[i] = i;
    }

    return nGpus;
}

//-------------------------------------------------------------------------------------------------------
// Function    :  get_cpuid
// Description :  Get the CPU ID
//
// Note        :  Work on both macOS and Linux systems
//-------------------------------------------------------------------------------------------------------
int get_cpuid()
{

// See https://stackoverflow.com/questions/33745364/sched-getcpu-equivalent-for-os-x
   int CPU;

   CPU = sched_getcpu();

   return CPU;

} // FUNCTION : get_cpuid

int main(void)
{
    int N_GPU;
    long N = 1L<<31;
//    long N = 1L<<3;
    double t_start, t_stop;
    int *gid;

    N_GPU = getAllGpus(&gid);

    printf("N = %ld .\n", N);
    printf("Total %d GPU(s) are available.\n", N_GPU);

    vector<float> A(N);
    vector<float> B(N);
    vector<float> C(N);

    t_start = omp_get_wtime();
    // initialization
    #pragma omp parallel num_threads( 12*N_GPU )
    {
        long seed = 149874015+omp_get_thread_num();
        mt19937 generator( seed );
        normal_distribution<float> norm(0.0, 1.0);

        #pragma omp master
        printf("Total %2d threads are initialized.\n", omp_get_num_threads());
        #pragma omp barrier
        printf("My CPU ID is %2d for Thread %2d\n", get_cpuid(), omp_get_thread_num());

        #pragma omp for
        for (long i = 0; i < N; i++)
        {
            A[i] = norm(generator);
            B[i] = norm(generator);
        }
    }

    // vector add
    #pragma omp parallel for num_threads( 12*N_GPU )
    for (long i = 0; i < N; i++)
    {
        C[i] = A[i] + B[i];
    }
    t_stop = omp_get_wtime();

//    for (long i = 0; i < N; i++)
//        printf("C[%ld] = %+.8e\n", i, C[i]);

    printf("--------------------------------------------------------------\n");
    printf("Total execution time is %.4e s .\n", t_stop - t_start);

    return EXIT_SUCCESS;
}

