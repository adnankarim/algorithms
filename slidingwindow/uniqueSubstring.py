# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# TC O(n)
# SC O(1)
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
# update left to prev occurinWindow+1
            if s[j] in dp and dp[s[j]]>=i:
                i=dp[s[j]]+1
                windowLen=j-i
# update lookup table
            dp[s[j]]=j
            j+=1
            windowLen+=1
#             update maxlen at every step 
            if windowLen>maxLen:
                maxLen=windowLen
            
            
            
            
            
        return maxLen