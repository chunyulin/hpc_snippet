#include "mpi.h"
#include <cstdio>
#include <cstring>

int main(int argc, char *argv[])
{
    int i, rank, size, namelen;
    char name[MPI_MAX_PROCESSOR_NAME];
    MPI_Status stat;

    MPI_Init(&argc, &argv);

    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Get_processor_name(name, &namelen);

    if (rank == 0) {
        printf("Rank %d of %d on %s\n", rank, size, name);

        for (i = 1; i < size; i++) {
            MPI_Recv(&rank, 1, MPI_INT, i, 1, MPI_COMM_WORLD, &stat);
            MPI_Recv(&size, 1, MPI_INT, i, 1, MPI_COMM_WORLD, &stat);
            MPI_Recv(&namelen, 1, MPI_INT, i, 1, MPI_COMM_WORLD, &stat);
            MPI_Recv(name, namelen + 1, MPI_CHAR, i, 1, MPI_COMM_WORLD, &stat);
            printf("Rank %d of %d on %s\n", rank, size, name);
        }
    } else {
        MPI_Send(&rank, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
        MPI_Send(&size, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
        MPI_Send(&namelen, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
        MPI_Send(name, namelen + 1, MPI_CHAR, 0, 1, MPI_COMM_WORLD);
    }

    MPI_Finalize();
    return (0);
}
