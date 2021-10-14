def selectionsort(A):

    for i in range(len(A)):
      
    # Find the minimum element in remaining 
    # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                
    # Swap the found minimum element with 
    # the first element        
        A[i], A[min_idx] = A[min_idx], A[i]

    return A

print(selectionsort([3,2,6,4,8,4,2,6,7]))
print(selectionsort([3,2]))
print(selectionsort([]))