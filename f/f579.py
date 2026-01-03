a, b = map(int, input().split())
n = int(input())
res = 0
for i in range(n):
    d = {}
    dil = input().split()
    for j in range(len(dil)-1):
        d[int(dil[j])] = d.get(int(dil[j]), 0) + 1
    if (d.get(a,0)-d.get(-a,0)) > 0 and (d.get(b,0)-d.get(-b,0)) > 0: #正數的key的value減掉負數的key的value
        res += 1
print(res)
