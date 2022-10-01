import sys
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        cs=0
        i=0
        j=0
        minSize=sys.maxint
        
        while j<len(nums):
            cs+=nums[j]
            
            while cs>=target:
                if (j-i+1)<minSize:
                    minSize=(j-i+1)
                cs-=nums[i]
                i+=1
            j+=1
            
            
        return 0 if minSize==sys.maxint else minSize