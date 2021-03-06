import sys
sys.stdin=open("00.txt","r")


def next_permutation(a):
    i = len(a)-1

    while i > 0 and a[i-1] >= a[i] : #다음순열 찾기
        i -= 1
    if i<= 0 : # 다음순열이 없다
        return False
    j = len(a)-1

    while a[j] <= a[i-1]: #오른쪽에 있으면서 a[i-1]보다 큰 수 나올 경우 끝
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]
    j = len(a) -1

    while i < j :
        a[i],a[j] = a[j],a[i] # a[i]부터 순열 뒤집기
        i += 1
        j -= 1

    return True

n = int(input())
a = list(map(int,input().split()))
if next_permutation(a):
    print(' '.join(map(str,a)))
else :
    print(-1)

