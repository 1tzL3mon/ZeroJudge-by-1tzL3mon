a, b, c= map(int, input().split()) #我不小心沒看到要從結果回推輸入，所以花了很久在把結果當成輸入執行
lis = []
for _ in range(a):
    lis.append(list(map(int, input().split())))
ex = list(map(int, input().split()))
for i in reversed(ex): #reversed()可以把list變成一個順序相反的list
    if i == 0:
        temp = []
        for j in range(b):
            ahh = []
            for idk in range(a):
                ahh.append(lis[idk][b-1-j])
            temp.append(ahh)
        lis = temp
        a, b= b, a
    elif i == 1:
        temp = []
        for idk in range(a):
            ahh = []
            for j in range(b):
                ahh.append(lis[a-1-idk][j])
            temp.append(ahh)
        lis = temp
print(a, b)
for i in lis:
    print(*i)
