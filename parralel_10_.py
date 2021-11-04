from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print("rank adalah : %s" %rank + " dan Size adalah : %s" %size)