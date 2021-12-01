import os
import sys
import time
from PIL import Image
from mpi4py import MPI

def compressMe(file, verbose=False):
	picture = Image.open(file)
	dim = os.stat(file).st_size

	picture.save("Compressed_"+picture.filename, "JPEG", optimize=True, quality=85)
	newsize = os.stat("Compressed_"+picture.filename).st_size
	percent = (dim-newsize)/float(dim)*100

	if(verbose):
		print("File compressed from {0} to {1} or {2}%".format(dim,newsize,percent))
	return percent

def utama():
	verbose=False
	if(len(sys.argv)>1):
		if(sys.argv[1].lower()=="-v"):
			verbose = True
	pwd=os.getcwd()
	file = '10.jpg'

	tot = compressMe(file, verbose)
	
	print("Average Compression: %d" %tot)

if __name__ == "__main__":
	utama()