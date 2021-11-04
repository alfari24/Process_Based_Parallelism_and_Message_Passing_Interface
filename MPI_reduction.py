import numpy
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank
array_size = 3
recvdata =  numpy.zeros(array_size, dtype = int)
senddata =  (rank+1)*numpy.arange(array_size,dtype = int)
print("proses %s mengirim %s " %(rank, senddata))
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)
print('on task ', rank,' after reduc : data = ', recvdata)