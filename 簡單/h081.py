while True:
    try:
        t, d = map(int, input().split())
        his = list(map(int, input().split()))
        x = his[0]
        hav = 1
        fin = 0
        for i in range(1, t):
            if hav == 1 and his[i] >= (x + d):
                fin += (his[i] - x)
                x = his[i]
                hav = 0
            elif hav == 0 and his[i] <= (x - d):
                x = his[i]
                hav = 1
        print(fin)
    except:
        break
