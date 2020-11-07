import sys
a,b=map(int,sys.stdin.readline().split())
dp=[[0]*(b+1) for i in range(a+1)]
for i in range(1,a+1):
    w,v=map(int,sys.stdin.readline().split())
    for j in range(1,b+1):
        if j>=w:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
