def max_sub_array_of_size_k(k, arr): 
    right = k-1
    currSum = maxSum = 0

    for i in range(0, right+1):
        currSum += arr[i]

    maxSum = currSum

    while right < len(arr)-1:
        currSum -= arr[right-k+1]
        currSum += arr[right+1]
        if currSum > maxSum:
            maxSum = currSum

        right += 1

    return maxSum

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))) #9
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))) #7

main()