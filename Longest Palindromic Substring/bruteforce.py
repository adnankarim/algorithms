import sys

def subString(string,length):
    reverse=string[::-1]
    dp={}
    maxlen=-sys.maxint-1
    out=""
    for i in range(length):
        temp=""
        for j in range(i,length):
            temp+=string[j]
        
            dp[temp]=[length-j-1,length-i-1]
            
    for i in range(length): 
        tempRev=""
        for j in range(i,length):
            
            tempRev+=reverse[j]
            if tempRev in dp:
                Len=len(tempRev)
                if Len>maxlen and dp[tempRev][0]==i and dp[tempRev][1]==j:
                    maxlen=Len
                    out=tempRev    
            
            
    return out

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen=-sys.maxint-1
        out=""
        subs=subString(s,len(s))

        # for temp in subs:
        #      if isPalind(temp):
        #         Len=len(temp)
        #         if Len>maxlen:
        #             maxlen=Len
        #             out=temp
        return subs

