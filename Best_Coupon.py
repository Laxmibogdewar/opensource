z=int(input())
discount1=z-(z//10)
discount2=z-100
if discount1<discount2:
    print(discount1)
else:
     print(discount2)
