from . import build_max_heap as build
from . import max_heapify as heapify

def heap_sort(arr):
	# First, build a max heap with our array
	build.build(arr)
	sorted_arr = [0] * len(arr)

	# The first element is the largest in the heap, so construct our sorted array
	for i in range(len(arr)-1, -1, -1):
		sorted_arr[i] = arr.pop(0)
		heapify.heapify(arr, 0)

	return sorted_arr
