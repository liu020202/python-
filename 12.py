numlist = []
for k in range(15):
    num = input("輸入一整數,輸入 ok 結束輸入)")
    numlist.append(num)
    if numlist[k] == "ok":
        numlist.pop()
        break
ans = ""
for i in range(len(numlist)):
    if numlist.count(numlist[i]) > len(numlist)/2:
        ans = numlist[i]
if ans == "":
    print("過半元素為:",)
else:
    print("過半元素為:",)
