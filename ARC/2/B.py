import datetime


a=input()

ymd=datetime.datetime.strptime(a, "%Y/%m/%d")

while True:
    ans=ymd.strftime('%Y/%m/%d')
    y,m,d=map(int, ans.split('/'))
    if y%(m*d)== 0:
        break
    ymd=ymd+datetime.timedelta(days=1)
print(ans)