def heapify(arr, index):
	# create indices for left child and right child of arr[i]
	l_child = 2 * index + 1
	r_child = 2 * index + 2
	swap = index
	# If we are not on the bottom row and left child is larger than parent, swap
	if l_child + 1 <= len(arr) and arr[l_child] > arr[swap]:
		swap = l_child
		
	# Same as above but for right child
	if r_child + 1 <= len(arr) and arr[r_child] > arr[swap]:
		swap = r_child

	# If either of the two above if statements were true, swap and recurse
	if swap != index:
		temp = arr[swap]
		arr[swap] = arr[index]
		arr[index] = temp
		heapify(arr, swap)
	return arr
