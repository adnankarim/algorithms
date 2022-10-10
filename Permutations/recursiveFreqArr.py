
# TC O(n!)
# SC O(n) freq + O(n) arr + o(n!) return perms + Auxillary recurive height of tree

def rescursivePerm(nums,ds,ans,freq):
        numLength=len(nums)
        if len(ds)==numLength:
            
            ans.append(list(ds))
           
            return
        # print(ans)
        for i in range(numLength):
            
            if not freq[i]:
                freq[i]=1
                ds.append(nums[i])
                rescursivePerm(nums,ds,ans,freq)
                ds.pop()
                freq[i]=0
        return ans
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         to store permulations n!
        ans=[]
        ds=[]
        freq=[0]*len(nums)
       
        rescursivePerm(nums,ds,ans,freq)
    
        return ans