from . import max_heapify

def build(arr):
	for i in range(int(len(arr)/2), -1, -1):
		max_heapify.heapify(arr, i)
	return arr


#heap = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
#print(build_max_heap(heap))