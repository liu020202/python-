m=int(input("星座月"))
d=int(input("星座日"))
if (m==1 and (d>=21 and d<=31 )) or (m==2 and (d>=1 and d<=18 )):
    print("水瓶")
elif (m==2 and (d>=19 and d<=30 )) or (m==3 and (d>=1 and d<=20 )):
    print("雙魚")
elif (m==3 and (d>=21 and d<=31 )) or (m==4 and (d>=1 and d<=20 )):
    print("牡羊")
elif (m==4 and (d>=21 and d<=30 )) or (m==5 and (d>=1 and d<=21 )):
    print("金牛")
elif (m==5 and (d>=22 and d<=31 )) or (m==6 and (d>=1 and d<=21 )):
    print("雙子")
elif (m==6 and (d>=22 and d<=30 )) or (m==7 and (d>=1 and d<=22 )):
    print("巨蟹")
elif (m==7 and (d>=23 and d<=31 )) or (m==8 and (d>=1 and d<=23 )):
    print("獅子")
elif (m==8 and (d>=24 and d<=31 )) or (m==9 and (d>=1 and d<=23 )):
    print("處女")
else:
    print("天秤")
