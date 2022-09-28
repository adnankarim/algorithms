# https://leetcode.com/problems/subarray-sum-equals-k/ with prefix or comulative sum
 # TC O(n^2)
def accumulate(lists):
    total=0
    for i in lists:
        total+=i
        yield total
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # TC O(n^2)
        lists = []
        comm=list(accumulate(nums))
        print(comm)
        for i in range(len(nums)):
            for j in range(0,i+1):
                if j==0:
                    lists.append(comm[i])
                else:
                    lists.append(comm[i]-comm[j-1])
        print(lists)
        return lists.count(k)
 