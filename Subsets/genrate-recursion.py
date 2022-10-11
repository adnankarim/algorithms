# recursion
def solve(i, s,f,out): 
	if (i == len(s)): 
		out.append(list(f))
		return
	
	#picking up and goinf forward in one brach of recursion tree
    
	f.append(s[i])
	solve(i + 1, s,  f,out)
	#poping out while backtracking and moving in branch (right)
	f.pop()
	solve(i + 1, s,  f,out)



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out=[]
        temp=[]
        solve(0,nums,temp,out)
        
        return out