while True:
    try:
        stac = []
        n = int(input())
        for n in range(n):
            m = list(map(int, input().split()))
            if m[0] == 1:
                stac.append(m[1])
            elif m[0] == 2:
                if stac:
                    print(stac[-1])
                else:
                    print(-1)
            elif m[0] == 3:
                if stac:
                    stac.pop()
    except:
        break
