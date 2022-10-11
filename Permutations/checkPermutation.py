class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
#         if (len(s)!=len(t)):
#             return False
#         dp1={}
#         dp2={}
#         for i in range(len(s)):
#             if s[i] in dp1.keys():
#                 dp1[s[i]]+=1
#             else:
#                 dp1[s[i]]=1
            
#             if t[i] in dp2.keys():
#                 dp2[t[i]]+=1
#             else:
#                 dp2[t[i]]=1
            
#         for i in s:
#             if (i not in dp1.keys()) or (i not in dp2.keys() )or dp1[i]!=dp2[i]:
#                 return False
#         return True
    
    
    
    
    
    # alternatively
        # return sorted(s)==sorted(t)
#    alternatively
        if len(s)!=len(t):
            return False

        chars=[0]*256
        for i in s:
            chars[ord(i)]+=1
        
        for i in t:
            chars[ord(i)]-=1
            if chars[ord(i)]<0:
                return False
        return True