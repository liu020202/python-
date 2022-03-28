m=int(input("請輸入階乘M:"))
i=1
t=1
while t < m:
    i+=1
    t*=i
print("超過M為%d的最小階層N值為:%d" % (m,i))