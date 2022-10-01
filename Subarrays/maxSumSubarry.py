# https://leetcode.com/submissions/detail/812143804/
# TC O(n)
# SC o(1)

    # Finding maximum subarray sum for a given array of integer
    # Used as an image processing algorithm
    # It can be used to solve the problems like “Station Travel in Order” and “Hotels Along the Coast”
    # It is used for business analysis

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum=float('-inf')
        
        cs=0
        for i in nums:
            cs+=i
            if  cs>maxSum:
                maxSum=cs
            
            if cs <0:  #if negative is reached we will start sum again as neagtive as are of no use for sum
                cs=0
        return maxSum