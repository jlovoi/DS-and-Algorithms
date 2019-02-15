from . import build_max_heap as build
from . import max_heapify as heapify

def heap_sort(arr):
	# First, build a max heap with our array
	array = arr[:]
	build.build(array)
	sorted_arr = [0] * len(array)

	# The first element is the largest in the heap, so construct our sorted array
	for i in range(len(arr)-1, -1, -1):
		print(array)
		sorted_arr[i] = array.pop(0)
		#heapify(array, 0)
		build.build(array)

	return sorted_arr

if __name__ == '__main__':
	prob1 = [4, 1, 3, 2, 7, 16, 9, 10, 14, 8]

	print (heap_sort(prob1))