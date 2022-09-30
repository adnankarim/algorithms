# https://leetcode.com/submissions/detail/812143804/
# TC O(n)
# SC o(1)
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
            
            if cs <0:
                cs=0
        return maxSum