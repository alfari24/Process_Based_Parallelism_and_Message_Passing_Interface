
# Process_Based_Parallelism_and_Message_Passing_Interface
need : 
- install mpiexec (https://www.microsoft.com/enus/download/details.aspx?id=57467)
- pip install pip install mpi4py
- install python
- installm numpy

to run : mpiexec -n 10 py name_of_your_file


# kolektif gather 
-PS A:\GitHub\Pararel> mpiexec -n 10 py .\kolektif_Gather.py
-rank : 1data : None
-rank : 5data : None
-rank : 7data : None
-rank : 3data : None
-rank : 2data : None
-rank : 6data : None
-rank : 9data : None
-rank : 4data : None
-rank : 8data : None
-rank : 0data : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Parralel
-PS A:\GitHub\Pararel> mpiexec -n 10 py .\parralel_10_.py
-rank adalah : 8 dan Size adalah : 10
-rank adalah : 4 dan Size adalah : 10
-rank adalah : 9 dan Size adalah : 10
-rank adalah : 0 dan Size adalah : 10
-rank adalah : 1 dan Size adalah : 10
-rank adalah : 7 dan Size adalah : 10
-rank adalah : 3 dan Size adalah : 10
-rank adalah : 6 dan Size adalah : 10
-rank adalah : 2 dan Size adalah : 10
-rank adalah : 5 dan Size adalah : 10

# kolektif broadcast
-PS A:\GitHub\Pararel> mpiexec -n 10 py .\kolektif_broadcast.py
-proses = 8variable dibagikan = 100
-proses = 0variable dibagikan = 100
-proses = 1variable dibagikan = 100
-proses = 9variable dibagikan = 100
-proses = 4variable dibagikan = 100
-proses = 5variable dibagikan = 100
-proses = 6variable dibagikan = 100
-proses = 2variable dibagikan = 100
-proses = 7variable dibagikan = 100
-proses = 3variable dibagikan = 100

# kolektif scatter 
-PS A:\GitHub\Pararel> mpiexec -n 10 py .\kolektif_scatter.py
-rank : 1data : 4
-rank : 4data : 25
-rank : 2data : 9
-rank : 5data : 36
-rank : 3data : 16
-rank : 6data : 49
-rank : 8data : 81
-rank : 0data : 1
-rank : 7data : 64
-rank : 9data : 100

# kolektif all to all 
-PS A:\GitHub\Process_Based_Parallelism_and_Message_Passing_Interface> mpiexec -n 10 py .\kolektif_all_to_all.py
-Prosess 4 mengirim [ 0  5 10 15 20 25 30 35 40 45] diterima [ 4  8 12 16 20 24 28 32 36 40]
-Prosess 9 mengirim [ 0 10 20 30 40 50 60 70 80 90] diterima [ 9 18 27 36 45 54 63 72 81 90]
-Prosess 7 mengirim [ 0  8 16 24 32 40 48 56 64 72] diterima [ 7 14 21 28 35 42 49 56 63 70]
-Prosess 5 mengirim [ 0  6 12 18 24 30 36 42 48 54] diterima [ 5 10 15 20 25 30 35 40 45 50]
-Prosess 8 mengirim [ 0  9 18 27 36 45 54 63 72 81] diterima [ 8 16 24 32 40 48 56 64 72 80]
-Prosess 6 mengirim [ 0  7 14 21 28 35 42 49 56 63] diterima [ 6 12 18 24 30 36 42 48 54 60]
-Prosess 3 mengirim [ 0  4  8 12 16 20 24 28 32 36] diterima [ 3  6  9 12 15 18 21 24 27 30]
-Prosess 1 mengirim [ 0  2  4  6  8 10 12 14 16 18] diterima [ 1  2  3  4  5  6  7  8  9 10]
-Prosess 2 mengirim [ 0  3  6  9 12 15 18 21 24 27] diterima [ 2  4  6  8 10 12 14 16 18 20]
-Prosess 0 mengirim [0 1 2 3 4 5 6 7 8 9] diterima [0 0 0 0 0 0 0 0 0 0]


# MPI reduction
-PS A:\GitHub\Process_Based_Parallelism_and_Message_Passing_Interface> mpiexec -n 10 py .\MPI_reduction.py
-proses 1 mengirim [0 2 4]
-on task  1  after reduc : data =  [0 0 0]
-proses 9 mengirim [ 0 10 20]
-on task  9  after reduc : data =  [0 0 0]
-proses 5 mengirim [ 0  6 12]
-on task  5  after reduc : data =  [0 0 0]
-proses 7 mengirim [ 0  8 16]
-on task  7  after reduc : data =  [0 0 0]
-proses 3 mengirim [0 4 8]
-on task  3  after reduc : data =  [0 0 0]
-proses 8 mengirim [ 0  9 18]
-on task  8  after reduc : data =  [0 0 0]
-proses 6 mengirim [ 0  7 14]
-on task  6  after reduc : data =  [0 0 0]
-proses 2 mengirim [0 3 6]
-on task  2  after reduc : data =  [0 0 0]
-proses 4 mengirim [ 0  5 10]
-on task  4  after reduc : data =  [0 0 0]
-proses 0 mengirim [0 1 2]
-on task  0  after reduc : data =  [  0  55 110]