n=int(input('輸入一整數1~100'))
t=[]
while True:
    if n==1:
        break
    elif n%2!=0:
        n=3*n+1
    elif n%2==0:
        n=n/2
    t.append(int(n))
print('數列為:'+str(t))
