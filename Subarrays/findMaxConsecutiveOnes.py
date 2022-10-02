class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=0
        maxOnes=float('-inf')
        count=0
        while j<len(nums):
            if nums[j]==1:
                count+=1
            else:
                count=0
            if count>maxOnes:
                maxOnes=count
            j+=1
        return 0 if  maxOnes==float('-inf') else maxOnes
                