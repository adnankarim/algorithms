def removeRepeated(arr):
    dp={}  
    res=[]
    for i in arr:
        if i in dp.keys():
            if i in res:
                res.remove(i)
        else:
            dp[i]=i
            res.append(i)
    return res