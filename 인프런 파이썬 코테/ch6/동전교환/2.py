import sys
sys.stdin = open("00.txt","r")

def DFS(L,sum):
    global res
    if L>= res:
        return
    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1,sum+data[i])





n = int(input())
data = list(map(int, input().split()))
m = int(input())
res= 2147000000
data.sort(reverse=True)
DFS(0,0)
print(res)