z=int(input())
if (z%4==0)and(z%100!=0):
    print('YES')
elif(z%400==0)and(z%100==0):
    print('YES')
else:
    print('NO')
