a = int(input("輸入一個度數(正整數)"))
if a <= 120 :
    print("Summer months: %.2f" % (a*2.10))
    print("Non-Summer months: %.2f" % (a*2.10))
elif a > 120 and a <= 330:
    print("Summer months: %.2f" % (a*3.02))
    print("Non-Summer months: %.2f" % (a*2.68))
elif a > 330 and a <= 500:
    print("Summer months: %.2f" % (a*4.39))
    print("Non-Summer months: %.2f" % (a*3.61))
elif a > 500 and a <= 700:
    print("Summer months: %.2f" % (a*4.97))
    print("Non-Summer months: %.2f" % (a*4.01))
else:
    print("Summer months: %.2f" % (a*5.63))
    print("Non-Summer months: %.2f" % (a*4.50))