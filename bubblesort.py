def bubblesort(arr):

    n = len(arr)

    for i in range(n):

        is_sorted = True

        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                is_sorted = False

        if is_sorted:
            break

    return arr


print(bubblesort([3,2,6,4,8,4,2,6,7]))
print(bubblesort([3,2]))
print(bubblesort([]))