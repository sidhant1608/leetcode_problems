def jump(nums):
    n, cur_max, next_max, steps = len(nums), 0, 0, 0
    for i in range(n):
        if i > cur_max:
            steps += 1
            cur_max = next_max
            if cur_max >= n: break
        next_max = max(next_max, nums[i] + i)
    return steps


print(jump([2,0,1,4,3,5,1,2]))
print(jump([2,3,1,1,4]))
print(jump([2,3,0,1,4]))


