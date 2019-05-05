ls = [0,1,2,4,5,6,7,8,9]
k = 7 
left = 0
right = len(ls)-1
print(right)
print(len(ls))

while left <= right:
    mid = left + (right-left)//2
    if ls[mid ] > ls[k-1]:
        right = mid - 1
    elif ls[mid] < ls[k-1] :
        left = mid + 1
    else:
        print("find it %d"%(mid+1) )
