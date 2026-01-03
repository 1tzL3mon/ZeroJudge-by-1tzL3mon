wid = int(input())
strin = input()
t = int(input())
lisstr = list(strin)
result = []
for i in range(wid):
    lisstr.insert(0, ' ') #在list最開頭插入
if t + wid > wid + len(strin):
    for i in range(t-len(strin)):
        lisstr.append(' ')
for i in range(wid):
    result.append(lisstr[t+i])
print(''.join(result))
