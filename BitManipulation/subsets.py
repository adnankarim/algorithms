# Time Complexity: O(2^n * n)

# Reason: O(2^n) for the outer for loop and O(n) for the inner for loop.

# Space Complexity: O(1)

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         if contigionus is demannded we cannot use 2^n
        subsets=[]
        for i in range(pow(2,len(nums))):
            temp=[]
            for j in range(len(nums)):
#                 check whether j is set in i if it is then include it
                if (i &(1<<j)):
                    temp.append(nums[j])
                
            subsets.append(temp)
        return subsets