# array vector
# TC O(n) argueable O(1) max ieration in worst case would be 256
# SC (1)   or O(charset length) a-z lowercase
def isUnique(string):
    character=0
    for i in string:
       
        if character & 1<<(ord(i)-ord('a')):
            return False
        
        character|=1<<(ord(i)-ord('a'))
    return True

print(isUnique('str'))
    
    
    