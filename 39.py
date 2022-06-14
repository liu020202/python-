n=int(input('請輸入一正整數'))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    
    print()

for i in range(n-1):
    for j in range(i+1):
        print(' ',end='') 
    for j in range(-2*i+(1+(n-2)*2)):
        print('*',end='')
    print()
