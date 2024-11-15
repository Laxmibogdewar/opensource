L,M,N,A=map(int,input().split())
if A<=L+M or A<=M+N or A<=L+N:
    print('YES')
else:
    print('NO')
