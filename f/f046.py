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

#企鵝answer
wide = int(input())
word = list(input())
time = int(input())
ls = []
for _ in range(wide):
    ls.append(" ")
for item in word:
    if time == 0:
        break
    else:
        ls.pop(0) #先在最前面拿掉一個空格
        ls.append(item)
    time -= 1
while time != 0:
    ls.pop(0) #不斷拿掉最前面的，直到time變成0
    ls.append(" ")
    time -= 1
print(*ls, sep="") #(*list, sep='')
