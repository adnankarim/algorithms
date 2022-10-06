# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def find_window(s, p):
# 	//Array as a Freq Map or you can hashmap
    FP = [0]*256
    FS = [0]*256
    for i in p:
        FP[ord(i)]+=1
# 	Sliding Window Algori
    
    cnt=0
    start=0 # left contractio
    start_idx = -1 #start_idx for best window
    min_so_far =100000 #large number
    window_size =None

    for i in range(len(s)):
# 		expand the window by including current character
        ch = s[i]
        FS[ord(ch)]+=1

# 		Count how many characters have been matched till now (string and pattern)
        if(FP[ord(ch)]!=0 and FS[ord(ch)]<= FP[ord(ch)]):
            cnt += 1
# 		

# 		another thing 
# 		if all characters of the pattern are found in the current window then you can start contracting
# if cnt is mor
        if(cnt==len(p)):

# 			start contracting from the left to remove unwanted characters 
# 			contract for unwanted char and unwanted greater frequncy
            while(FP[ord(s[start])]==0 or FS[ord(s[start])] > FP[ord(s[start])]):
                FS[ord(s[start])]-=1
                start+=1
# 			

# 			note. the window size
            window_size = i - start + 1
            if(window_size < min_so_far):
                min_so_far = window_size
                start_idx = start
# 			}

# 		}

# 	
# 
    if start_idx==-1:
        return "No window found"
# 	
    return s[start_idx:start_idx+min_so_far]
# }


print(find_window("123","12"))
