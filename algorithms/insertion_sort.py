def insertion(arr):
	ret = arr
	for i in range(1, len(arr)):
		key = ret[i]
		j = i - 1
		while key < ret[j] and j >= 0:
			ret[j+1] = ret[j]
			j = j - 1
		ret[j+1] = key
	return ret
