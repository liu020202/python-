medal = dict()
for i in range(4):
    record = input()
    record = record.split()

    medal[record[0]] = record[1]

print(f"金牌得到{medal['金']}面")
print(f"銀牌得到{medal['銀']}面")
print(f"銅牌得到{medal['銅']}面")
print(f"優牌得到{medal['優']}面")