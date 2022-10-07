
# Time complexity: O(N2), where N is the length of the input string.
# Auxiliary Space: O(N), where N is the length of the input string.
def subString(string,length):
    
    for i in range(length):
        temp=""
        for j in range(i,length):
            temp+=string[j]
            print(temp)







Str = "abcd"
subString(Str,len(Str))






