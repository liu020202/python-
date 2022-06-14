import random
ans=random.sample('1234567890',4)
res=list(input("輸入你的答案"))
a=0
b=0
for i in range(4):
    if ans[i]==res[i]:
        a+=1
    elif res[i] in ans:
        b+=1
ans1="".join(ans)
print(f"{ans1}為答案")
print("%dA%dB" %(a,b))