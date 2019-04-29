def binary_search(arr,start,end,hkey):
	if start > end:		#不满足条件直接返回
		return -1
	mid = start + (end - start) / 2
	if arr[mid] > hkey:		#递归
		return binary_search(arr, start, mid - 1, hkey)
	if arr[mid] < hkey:
		return binary_search(arr, mid + 1, end, hkey)
	return mid
