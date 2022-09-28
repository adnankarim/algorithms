# Housing sum equals k 
# positive n consective of any window
# TC  O(N) as we are removing once or few <<N times 

def findSum(lists,length,k):
    i=0
    j=0
    cs=0
    count=None
    while j<length:
        cs+=lists[j]
        j+=1
        while cs>k:
            cs-=lists[i]
            i+=1
        if cs==k:
            count+=1
    return count
    
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return findSum(nums,len(nums),k)
 
        