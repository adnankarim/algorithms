# TC O(n)
# SC O(1)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        i=0
        maxOnes=0
        countZeros=0
        while j<len(nums):
            
            if nums[j]==0:
               
                countZeros+=1
            while countZeros==1:
                maxOnes= max(maxOnes, j - i)
                if nums[i]==0:
                    countZeros-=1
                i+=1
            
            j+=1
        if countZeros<1:
            maxOnes= max(maxOnes, j - i)
        return maxOnes