def quicksort(arr):

    if len(arr) < 2:
        return arr

    n = len(arr)
    pivot = arr[n//2]

    low, same, high = [], [], []
    for i in arr:
        if i < pivot:
            low.append(i)
        elif i == pivot:
            same.append(i)
        else:
            high.append(i)

    return quicksort(low) + same + quicksort(high)

print(quicksort([3,2,6,4,8,4,2,6,7]))
print(quicksort([3,2]))
print(quicksort([]))