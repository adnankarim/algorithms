# https://www.codingninjas.com/codestudio/problems/palindrome-permutation_1171180

# TC 

from os import *
from sys import *
from collections import *
from math import *

def swap(i,j,arr):
    arr[i],arr[j]= arr[j],arr[i]
    return arr
    
def isPalind(arr):
    return arr==arr[::-1]

def rescursivePerm(index,nums,ans):
        numLength=len(nums)
        if index==numLength:#Reached at end index for swap out of length
            if isPalind(nums):
                ans.append(list(nums))
            
            return 
        # print(ans)
        for i in range(index,numLength):
            
            swap(i,index,nums)
            rescursivePerm(index+1,nums,ans)
            swap(i,index,nums)
    
def palindromeString(s):
    # Write your code here.
    out=[]
    s=[i for i in s]
    rescursivePerm(0,s,out)
    
    
    
    return len(out)>0