from heapq import heapify, heappop
from typing import List

def optimizing_box_weights(arr: List[int]) -> List[int]:
    target = sum(arr) / 2

    # we need max heap, so reverse the order by negating all values
    for i in range(len(arr)):
        arr[i] = -arr[i]
    heapify(arr)

    cur_sum = 0
    res = []
    i = 0
    while cur_sum <= target:
        print(arr[i])
        val = -heappop(arr)
        cur_sum += val
        res.append(val)
    res.reverse()
    return res

arr = [1, 2, 2, 3, 4, 4,4, 5]
res = optimizing_box_weights(arr)
print(' '.join(map(str, res)))

