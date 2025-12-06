while True: #9行
    try:
        a, b = input().split()
        n = 1
        while int(a)+int(a)*(n-1)+(n-1)*n/2 < int(b):
            n += 1
        print(n)
    except:
        break
