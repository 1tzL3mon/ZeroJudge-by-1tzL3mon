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
