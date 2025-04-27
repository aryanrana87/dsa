# Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. 
# You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

arr= [1, 2, 3, 7, 5]
target = 12
n = len(arr)
start = 0
current_sum = 0
for end in range(n):
    current_sum += arr[end]
    while current_sum > target and start < end:
        print(current_sum)
        current_sum -= arr[start]
        start += 1
    if current_sum == target:
        print( [start + 1, end + 1])
print (-1)