w = input()
if len(w) % 2 != 0:
    print(no)
times = int(input())
setotwo = list(w)
print(setotwo)
for t in range(times):
    n = int(input())
    if n == 0:
        for j in range(int(len(setotwo)/2)):
            temp = setotwo[2*j]
            setotwo[2*j] = setotwo[2*j+1]
            setotwo[2*j+1] = temp
    elif n == 1:
        
        
print(setotwo)
