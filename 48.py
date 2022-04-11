m = float(input("輸入路程公里數(KM):"))
n = 75
if m <= 1.5 :
    print("所需車資為:%d" %(n))
elif m > 1.5:
    if m - 1.5 < 0.25:
        print("所需車資為:%d" %(n + 5))
    else:
        print("所需車資為:%d" %(n + 5*((m-1.5)/1.5)))