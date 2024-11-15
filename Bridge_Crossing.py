k,l,m=map(int,input().split())
sum=l
count=0
while(sum+k<=m):
    sum+=k
    count+=1
print(count)
