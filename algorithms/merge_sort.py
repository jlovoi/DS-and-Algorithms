def merge_sort(arr):
	mid = int(len(arr)/2)

	left = arr[:mid]
	right = arr[mid:]

	# keep breaking it down until the arrays are size of 1
	if len(left) > 1:
		merge_sort(left)
	if len(right) > 1:
		merge_sort(right)

	for i in range(len(arr)):
		if not left:
			arr[i] = right.pop(0)
		elif not right:
			arr[i] = left.pop(0)
		elif left[0] < right[0]:
			arr[i] = left.pop(0)
		else:
			arr[i] = right.pop(0)

	return arr