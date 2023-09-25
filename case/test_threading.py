
import threading
def suiteTest(a):
	print (a+1)
threads = []
for i in range(3):
	t = threading.Thread(target=suiteTest,args=(i,))
	threads.append(t)
print(threads)
for thread in threads:
	thread.start()
