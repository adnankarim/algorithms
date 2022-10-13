#         O(N)+O(N)(worst N else O(n<<N) usual case if all are distinct)
import sys
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (not len(nums)):
            return 0
        maxSize=-sys.maxint-1
        uniques=set(nums) #O(N)
        

        for i in nums:
            if i-1 in uniques:
                continue
            elif i+1 in uniques:
                count=0
                temp=i
                while (temp in uniques):
                    count+=1
                    temp+=1
                
                maxSize=max(maxSize,count)
        return max(maxSize,1)