

# TC O(n!)
# SC  o(n!) return perms + Auxillary recurive height of tree


def swap( pos1, pos2,list):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def rescursivePerm(index,nums,ans):
        numLength=len(nums)
        if index==numLength:#Reached at end index for swap out of length
            
            ans.append(list(nums))
            
            return 
        # print(ans)
        for i in range(index,numLength):
            
            swap(i,index,nums)
            rescursivePerm(index+1,nums,ans)
            swap(i,index,nums)
            
        
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         to store permulations n!
        ans=[]
        
       
        rescursivePerm(0,nums,ans)
    
        return  ans