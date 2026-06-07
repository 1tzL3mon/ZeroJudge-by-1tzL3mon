itema, itemb = map(int, input().split())
n = int(input())
res = 0
for i in range(n): 
    d = {}
    dil = list(map(int, input().split()))
    for j in range(len(dil)-1): #跑完所有商品後再進入if句
        d[dil[j]] = d.get(dil[j], 0) + 1 #把d字典裡的dil[j]物件設為他原本的數量加1
    if (d.get(itema,0)-d.get(-itema,0)) > 0 and (d.get(itemb,0)-d.get(-itemb,0)) > 0: #正值的key的value減掉負值的key的value，且兩個都大於0
        res += 1
print(res)
