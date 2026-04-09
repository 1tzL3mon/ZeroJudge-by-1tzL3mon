while True:
    try:
        t = int(input())
        x = []
        y = []
        d = []
        for i in range(t):
            a, b = map(int, input().split())
            x.append(a)
            y.append(b)
        for i in range(t-1):
            d.append(abs(x[i]-x[i+1]) + abs(y[i]-y[i+1]))
        print(max(d), min(d))
    except:
        break
