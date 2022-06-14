total=[]
h=int(input("小名身上有幾元:0~100"))
num=int(input("販賣機有幾種飲料:1~30"))
for i in range(num):
    price=int(input("價錢為"))
    total.append(price)
print(total)
a=0
for i in range(num):
    if h>=total[i]:
        a+=1

print("可以買的杯數:"+str(a))