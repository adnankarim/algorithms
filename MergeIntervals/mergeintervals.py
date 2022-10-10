# TC nlogn
# SC O(n) for output mergs

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        out=[]
        intervals=sorted(intervals)
        
        curr=intervals[0]
        
        
        for interval in intervals:
# if being compared's first is <= selected interval's end or second then merged
# jo compared kia ja rha ha uska end ka andr ha ya nahi iteratve wala ka first
            if interval[0]<= curr[1]:
                curr[1]=max(curr[1],interval[1])
            else:
#     agr merge nahi hua to usko output man dal do and move on
                out.append(curr)
                curr=interval
                
        out.append(curr)#last wala ko b append kro if else loop ke waja se append nahi hua as end pr merge hua input list ka
        
        return out