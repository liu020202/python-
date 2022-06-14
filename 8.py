a=int(input("請輸入正整數:"))
b=input("請輸入數列(以空格隔開):")
list=b.split(" ")
c=set(list)
d=max(list,key=list.count)

if a==len(list):
    if len(list)==len(c):
        print("每個數字剛好只出現一次")
    else:
        print("最大出現次數的數字為:" ,d)
        print("出現次數為:",list.count(d))