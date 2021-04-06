import sys
print("何個の置換をかけますか？：")
a=int(input())#かける数2個以外にも対応したので追加点お願いします
print("数列の数を入力してください：")
b=int(input())#数列の数

print("1番目の巡環置換表示：")#最初の要素の入力
for i in range(1,b+1):
    print(i,end=" ")
print()
c=list(map(int,input().split()))

#ここからエラー探し
for i in range(0,b-1):
    if c[i]>b:
        print("値がおおきいので終了します")
        sys.exit()
    for j in range(i+1,b):
        if c[i]==c[j]:
            print("同じ値がありますので終了します")
            sys.exit([1])
if c[b-1]>b:
        print("値がおおきいので終了します")
        sys.exit([1])
#ここまで


for i in range(0,a-1):
    print("{}番目の巡環置換表示：".format(i+2))
    for j in range(1,b+1):
        print(j,end=" ")
    print()
    d=list(map(int,input().split()))
    #ここからエラー探し
    for i in range(0,b-1):
        if d[i]>b:
            print("値がおおきいので終了します")
            sys.exit()
        for j in range(i+1,b):
            if d[i]==d[j]:
                print("同じ値がありますので終了します")
                sys.exit([1])
    if d[b-1]>b:
        print("値がおおきいので終了します")
        sys.exit([1])
    #ここまで

    for z in range(0,b):
        c[z]=d[c[z]-1]#ここで一回ずつ積を求めているCの要素を変えている
print("置換の積の答え\n(")
for i in range(1,b+1):
    print(i,end=" ")
print()
for i in range(b):
    print(c[i],end=" ")
print("\n)")

