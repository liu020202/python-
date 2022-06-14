n=int(input('小狗可能跑到哪幾個地方2~10'))
p=[]
for i in range(n):
    n1=int(input("那個地方與家的距離"))
    p.append(n1)
    if p[i]%9==0 or p[i]%11==0:
        print('第'+str(i+1)+'個點'+str(p[i]))