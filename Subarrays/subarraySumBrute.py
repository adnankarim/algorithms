# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # TC O(n^3)
        lists = [[]]
        for i in range(len(nums) + 1):
            for j in range(i):
                lists.append(sum(nums[j: i]))
        return lists.count(k)
 
        