while True:
    try:
        times = int(input())
    except:
        break
    thre = 0
    un = 0
    du = 0
    for t in range(times):
        try:
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
