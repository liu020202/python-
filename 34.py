n = int(input("輸入一正整數"))
if n >= 11 and n <=1000:
    if n % 2 == 0 and n % 11 ==0:
        if n % 5 != 0 or n % 7 != 0:
            print("%d為新公倍數?:Yes" % (n))
        else:
            print("%d為新公倍數?:No" % (n))
    else:
        print("%d為新公倍數?:No" % (n))
else:
    print("mistake")