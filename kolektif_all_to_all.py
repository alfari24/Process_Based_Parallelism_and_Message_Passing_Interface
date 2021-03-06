from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_size = 1 
senddata = (rank+1)*numpy.arange(size, dtype = int)
recvdata = numpy.empty(size*a_size, dtype = int)

comm.Alltoall(senddata, recvdata)

print("Prosess %s mengirim %s diterima %s " %(rank , senddata , recvdata))