import threading
import time

lock = threading.Lock()
x=0

def increment():
	global x
	for i in range (1000000):
		lock.acquire()
		x+=1
		lock.release()

def main():
	t1=threading.Thread(target=increment)
	t2=threading.Thread(target=increment)
	t3=threading.Thread(target=increment)
	t4=threading.Thread(target=increment)

	t1.start()
	t2.start()
	t3.start()
	t4.start()

	t1.join()
	t2.join()
	t3.join()
	t4.join()

if __name__=="__main__":
	for j in range (5):
		main()
		print("nilai x: %s" %x)




