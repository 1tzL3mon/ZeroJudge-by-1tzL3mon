while True:
    try:
        n, d = map(int, input().split())
        am = 0
        fina = 0
        for i in range(n):
            a = list(map(int, input().split()))
            if max(a) - min(a) >= d:
                am += 1
                fina += ((a[0] + a[1] + a[2])//3)
        print(am, fina)
    except:
        break
