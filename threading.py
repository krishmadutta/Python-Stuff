import threading

counter = 0
def worker():
	global counter
	counter +=1
	print("The count in %d" %counter)
	print("-------------------------")

print("Starting up")
for i in range(10):
#	worker()
	t = threading.Thread(target=worker)
	threads.append(t)
	t.start()
print("Finishing up")