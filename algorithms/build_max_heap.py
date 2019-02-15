from . import max_heapify as heapify

def build(arr):
	for i in range(int(len(arr)/2), -1, -1):
		heapify.heapify(arr, i)
	return arr

