number = []
n = int(input("輸入一整數n"))
number.append(n)
if n > 0 and n < 1000000:
    while n == 1:
        if n % 2 != 0:
            n = 3*n+1
            number.append(n)
        else:
            n = n/2
            number.append(n)
    print(number)
else:
    print("不再範圍內")
