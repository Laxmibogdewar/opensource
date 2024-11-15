xy,yz,zy=map(int,input().split())
n=xy*yz
if n<=(zy*1440):
    print('YES')
else:
    print('NO')
