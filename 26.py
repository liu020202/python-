time=0
a=input("檢測的字串:(end結束)")
a1=[n for n in a]
b=input("檢測字串:")

if a == "end":
    print("結束")
else:
    for i in range(0,len(a1)): 
        if b == a1[i]:
            time+=1
        else:
            continue

print(f"字元{b}出現的次數為:{time}")