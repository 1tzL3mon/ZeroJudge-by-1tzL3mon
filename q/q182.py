import copy #22行
w = input()
times = int(input())
setotwo = list(w)
for t in range(times):
    n = int(input())
    if n == 0:
        for j in range(int(len(setotwo)/2)):
                setotwo[2*j], setotwo[2*j+1] = setotwo[2*j+1], setotwo[2*j]
    elif n == 1:
        for j in range(int(len(setotwo)/2)):
            if str(setotwo[2*j]) > str(setotwo[2*j+1]):
                setotwo[2*j], setotwo[2*j+1] = setotwo[2*j+1], setotwo[2*j]
    elif n == 2:
        halves = copy.deepcopy(setotwo) #copy.deepcopy()的複製不會使用同一個記憶體
        setotwo = []
        for j in range(int(len(w)/2)):
            setotwo.append(halves[j])
            setotwo.append(halves[int(len(w)/2)+j])
for i in range(len(setotwo)):
    print(setotwo[i], end='')
print()


#企鵝answer 19行
ip = input()
text = list(ip)
n = int(input())
for _ in range(n):
    ls = []
    num = int(input())
    if num == 0:
        for i in range(0, len(text), 2):
            ls.append(text[i+1])
            ls.append(text[i])
    elif num == 1:
        pair = sorted([text[i],text[i+1]])
        ls.extend(pair)
    elif num == 2:
        for i in range(0, int(len(text)/2)):
            ls.append(text[i])
            ls.append(text[(int((len(text))/2))+i])
    text = ls
print("".join(text)) #把list變成string,且中間沒有空格
