x=float(input("X軸座標:"))
y=float(input("Y軸座標:"))
d = x**2 + y**2
if x > 0:
    if y > 0:
        print("該點位於第一象限,離原點距離為根號%d" % (d))
    elif y < 0:
        print("該點位於第四象限,離原點距離為根號%d" % (d))
    else:
        print("該點位於右半平面,離原點距離為根號%d" % (d))
elif x < 0 :
    if y > 0:
        print("該點位於第二象限,離原點距離為根號%d" % (d))
    elif y < 0:
        print("該點位於第三象限,離原點距離為根號%d" % (d))
    else:
        print("該點位於左半平面,離原點距離為根號%d" % (d))
else:
    if y == 0 :
        print("該點位於原點")
    elif y > 0:
        print("該點位於上半平面,離原點距離為根號%d" % (d))
    elif y < 0:
        print("該點位於下半平面,離原點距離為根號%d" % (d))