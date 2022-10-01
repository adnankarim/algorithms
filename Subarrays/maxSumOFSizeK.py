# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# TC O(n)
# SC O(1)
def getMaxSum(arr, k):
    maxSum = 0
    windowSum = 0
    start = 0
    
    for i in range(len(arr)):
        windowSum += arr[i]
        
        if ((i - start + 1) == k):
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[start]
            start += 1
    
    return maxSum


print( getMaxSum([3, 5, -2, 4, 7], 3))