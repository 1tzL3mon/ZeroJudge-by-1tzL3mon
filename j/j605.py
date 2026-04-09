while True:
    try:
        ts = int(input())
        dea = 0
        high = -1
        hightime = 0
        for _ in range(ts):
            a, b = map(int, input().split())
            if b > high:
                high = b
                hightime = a
            if b == -1:
                dea += 1
        fin = high - ts - (dea)*2
        if fin < 0:
            fin = 0
        print(fin, hightime)
    except:
        break
