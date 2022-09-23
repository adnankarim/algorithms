# https://leetcode.com/problems/uncommon-words-from-two-sentences/submissions/
# 
# Time Complexity: O(M+N) where M,NM, NM,N are the lengths of A and B respectively.
# Space Complexity: O(M+N) the space used by hasmaps

def removeRepeated(arr):
    dp={}  
    res=[]
    for i in arr:
        if i in dp.keys():
            if i in res:
                res.remove(i)
        else:
            dp[i]=i
            res.append(i)
    return res
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1=s1+" "+s2  
        s1=removeRepeated(s1.split(" "))
       
       
        return s1