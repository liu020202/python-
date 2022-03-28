a = list(input("輸入一組四位數字為:"))
for i in range(3):
    a[i] = (int(a[i])+7)%10
b = 0
b = a[0]
a[0] = a[2]
a[2] = b
c = 0
c = a[1]
a[1] = a[3]
a[3] = c

print(list(a))