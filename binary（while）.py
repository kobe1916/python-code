def binary_search(arr, start, end, hkey):
	while start <= end:
		mid = start + (end - start) / 2
		if arr[mid] < hkey:
			start = mid + 1
		elif arr[mid] > hkey:
			end = mid - 1
		else:
			return mid
     return -1
