while True: #17行
    try:
        times = int(input())
        thre = 0
        un = 0
        du = 0
        for t in range(times):
            n = int(input())
            if n % 3 == 0:
                thre +=1
            elif n % 3 == 1:
                un += 1
            else:
                du += 1
    except:
        break
    print(f"{thre} {un} {du}")


#企鵝answer 11行
ip = int(input())
a, b, c = 0, 0, 0 #創建一個三物件的tuple
for i in range(ip):
    n = int(input())%3
    if n == 0:
        a += 1
    elif n == 1:
        b += 1
    else:
        c += 1
print(a, b, c) #print tuple的時候，不會有逗點
