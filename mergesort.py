def merge(left, right):

    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    arr = []
    l,r = 0,0

    while len(arr) < len(left) + len(right):

        if left[l] <= right[r]:
            arr.append(left[l])
            l+=1
        else:
            arr.append(right[r])
            r+=1

        if l == len(left):
            arr = arr + right[r:]

        if r == len(right):
            arr = arr + left[l:]

    return arr

def mergesort(arr):

    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    return merge(mergesort(arr[:mid]),mergesort(arr[mid:]))


print(mergesort([3,2,6,4,8,4,2,6,7]))
print(mergesort([3,2]))
print(mergesort([]))