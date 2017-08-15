score=open("1.txt").read()
a=score.split()
av=float(a[2])/int(a[0])
o=a[0]
p=a[1]
q=a[2]
print("你已玩%s次，最好成绩是%s轮猜中，本次猜了%s轮,平均用了%.2f次。"%(o,p,q,av))
