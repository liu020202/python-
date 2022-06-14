a1=input("甲方的數字")
a2=input("乙方的數字")
c=a1.split(" ")
d=a2.split(" ")
for i in range(len(c)):

    if c[i]==d[i]:
        print("和")
    elif c[i]>d[i]:
        print("贏")
    else:
        print("輸")