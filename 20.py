group = int(input("輸入組數:"))
inpList = []
for n in range(group):
    inpList.append(input(f"第{n+1}組:"))

fullList = []
halfList = []
for i in range(group):
    fullList.append(int(inpList[i][0]))
    halfList.append(int(inpList[i][2]))

fee = []
for s in range(group):
    fee.append(fullList[s]*250 + halfList[s]*175)
    print(f"第{s+1}組應收費用:{fee[s]}")