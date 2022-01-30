'''
Given an array of positive numbers and a positive number 'S,' find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.
'''
def smallest_subarray_sum(target, arr):
    if not arr:
        return -1

    left = 0
    right = 1
    s = arr[0]
    minLength = float('inf')

    while right <= len(arr):
        if s >= target:
            minLength = min(minLength, right-left)
            s -= arr[left]
            left += 1
        elif right == len(arr):
            break
        else:
            s += arr[right]
            right += 1

    return -1 if (minLength == float('inf')) else minLength


print(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])) # 2
print(smallest_subarray_sum(7, [2, 1, 5, 2, 8])) # 1 
print(smallest_subarray_sum(8, [3, 4, 1, 1, 6])) # 3