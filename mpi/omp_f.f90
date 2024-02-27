program main
use OMP_LIB
implicit none
integer, parameter :: M=1000, N = 1024*1000, ITER=100
integer :: i,j,k
real(kind=8), dimension(M,N) :: testval
real(kind=8) :: tmp, t0,t1,t2,t3, zetam2

!!!
!!! Note:
!!!   1) 1/k**2 can be pull out of the loop
!!!   2) The memory affinity matters for the testval(i,j) loop. Instead of using testval = 0.0, using OMP loop initialization to 
!!!      ensure "First Touch Data Placement Policy" for better memory affinity 
!!!   3) The performance drop at 28 core (1-socket), possiably due to wired cpu binding where one core is located into the other socket.
!!!      We ignore it unless it really matters for the whole project.
!!!

zetam2 = 0.0
t0 = omp_get_wtime()
!$omp parallel do reduction(+:zetam2)
do k = 1,ITER
   zetam2 = zetam2 + 1.0/dble(k**2)   ! dble(i*j)/dble(k**2)
enddo

!! Instead of use testval = 0.0, using loop initialization to ensure "First Touch Data Placement Policy"
!$omp parallel do shared(testval)
do j = 1, N
do i = 1, M
   testval(i,j) = 0
enddo
enddo
!$omp end parallel do


!! OMP scaling not good for this loop, probably due to the matrix update?
t1= omp_get_wtime()
!$omp parallel do shared(testval)
do j = 1, N
do i = 1, M
   testval(i,j) = testval(i,j) + dble(i)*dble(j)*zetam2
enddo
enddo
!$omp end parallel do
t2= omp_get_wtime()

tmp=0.0
!$omp parallel do reduction(+:tmp) collapse(2)
do j = 1, N
do i = 1, M
   tmp = tmp + testval(i,j)
enddo
enddo
!$omp end parallel do
t3= omp_get_wtime()


print '(A,I3,A,3E9.2,A,E11.4)', "#Cores " , omp_get_max_threads(), "  Walltime/secs: ", t1-t0, t2-t1, t3-t2,"    Check: ", tmp

end program




! To avoid using temp variable, see https://stackoverflow.com/questions/14420740/how-to-use-reduction-on-an-array-in-fortran