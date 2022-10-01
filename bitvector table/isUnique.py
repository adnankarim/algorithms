# array vector
# TC O(n) argueable O(1) max ieration in worst case would be 256
# SC (1)   or O(charset length)
def isUnique(string):
    vector=[0]*256
    for i in string:
        if vector[ord(i)]:
            return False
        
        vector[ord(i)]=1
    return True

print(isUnique('stringg'))
    
    
    