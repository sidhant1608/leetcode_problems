def binarysearch(arr, x):

    arr.sort()    
    print(arr)
    l,r = 0, len(arr) - 1
    mid = 0

    while l <= r:

        mid = (l+r) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    return l

print(binarysearch([2,45,6,3,6,4,765,2,4,6,2345,456], 8888))