

from symbol import subscript


def subString(string,length):
    
    for i in range(length):
        temp=""
        for j in range(i,length):
            temp+=string[j]
            print(temp)








Str = "abcd"
subString(Str,len(Str))