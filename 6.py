a=input("輸入由0~9的數字所組成的N個數字字串(1<=N<=7)(以,分隔)")
b=list(a.split(","))
min=sorted(b)
max=sorted(min,reverse=True)
min2=int(''.join(min))
max2=int(''.join(max))

print(max2-min2)