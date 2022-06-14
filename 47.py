medal = list()

for i in range(4):
    record = input()
    record = record.split()

    medal.append(record)

for item in medal:
    print(f"{item[0]}牌得到{item[1]}面")