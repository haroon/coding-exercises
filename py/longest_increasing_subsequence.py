from sys import stdin

def lis(li): 
    # Write your code here
    n = len(li)
    dp =[[0 for j in range(2)] for i in range(n+1)]
    
    for i in range(n-1,-1,-1):
        including_max = 1
        for j in range(i+1,n):
            if li[j]>li[i]:
                including_max = max(including_max,1+dp[j][0])
        dp[i][0] = including_max
        excluding_max = dp[i+1][1]
        overall_max = max(including_max,excluding_max)
        dp[i][1] = overall_max
    #print(dp)
    return dp[0][1]









        

def takeInput():
    #To take fast I/O
    n=int(input())
    if n==0:
        return list(),0
    arr=list(map(int,input().split()))
    return arr,n
    

arr,n=takeInput()
print(lis(arr))
