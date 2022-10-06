# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
import sys
def lookup(freq1,freq2):
        
        for i in freq2.keys():            
            if i in freq1:
                if freq2[i]!=freq1[i]:
                    return False
            else:
                return False
        return True
    
class Solution(object):
    
        
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        j=0
        i=0
        minSize=sys.maxint
        minShape=[]
#         hasmap frequency
        freq2={}
        for k in t:
            freq2[k]=1+freq2.get(k,0)
        freq1={}
        while j<len(s):
            freq1[s[j]]=1+freq1.get(s[j],0)
            if lookup(freq1,freq2) :
                print ('i-j' +str(i)+'-'+str(j))
                if minSize>=j-i:
                    minSize=j-i
                    minShape=[i,j]
                while i<j:
                    if lookup(freq1,freq2):
                        if minSize>j-i:
                            minSize=j-i
                            minShape=[i,j]

                    freq1[s[i]]-=1
                    i+=1
            
            j+=1
        if lookup(freq1,freq2):
            minSize= min(minSize ,j - i)
        return s[minShape[0]:minShape[1]+1] if len(minShape)>0 else ""
        