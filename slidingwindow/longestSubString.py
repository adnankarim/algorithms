
# TC O(n)
# SC O(1)
# https://leetcode.com/submissions/detail/811377735/
# keep two pointer i, j
# maxLength and current length of window
# hashmap for lookup O(1)
# j moves until length (end) of string
# i updates only to dp[s[j]]+1 if repeating char is after 1st pointer i (dp[s[j]]>=i)) after lookup from hashmap
# currlength and maxlength updated at each iteration only if conditions are met.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        windowLen=0
        maxLen=0
        i=0
        j=0
        dp={}
        
        while j<len(s):
            if s[j] not in dp:
                
                windowLen=j+1-i   
                if windowLen>maxLen:
                    maxLen=windowLen
                dp[s[j]]=j
                        
            else:
                if dp[s[j]]>=i:
                    i=dp[s[j]]+1
                windowLen=j+1-i   
                if windowLen>maxLen:
                        maxLen=windowLen
                dp[s[j]]=j
                
            j+=1
        return maxLen