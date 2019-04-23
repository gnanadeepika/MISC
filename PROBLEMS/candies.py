def candies(n, arr):
    left = [0]*len(arr)
    right = [0]*len(arr)
    left[0]=1
    right[-1]=1
    for i in range(1,len(arr)):
        if arr[i-1]<arr[i]:
            left[i]=left[i-1]+1
        else:
            left[i]=1
    for i in reversed(range(0,len(arr)-1)):
        if arr[i] > arr[i+1]:
            right[i]=right[i+1]+1
        else:
            right[i]=1
    print("Left--->",left )
    print("Right-->",right)
    return sum([max(left[i],right[i]) for i in range(len(arr))])

print("output-->",candies(10,[2,4,2,6,1,7,8,9,2,1]))