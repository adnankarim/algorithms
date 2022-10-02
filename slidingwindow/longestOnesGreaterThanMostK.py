# TC O(n)
# SC O(1)
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=0
        j=0
        maxZeros=0
        count=0
        while j<len(nums):
            if nums[j]==0:
                count+=1
                
            while count>k:
                maxZeros=max(maxZeros,j-i)
                
                if nums[i]==0:
                    count-=1
                i+=1
            j+=1
        if count <= k:
            maxZeros = max(maxZeros, j-i)    
        return maxZeros