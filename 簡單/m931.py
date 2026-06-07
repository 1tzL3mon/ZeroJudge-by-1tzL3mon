while True:
    try:
        t = int(input())
        atk = []
        des = []
        maxab = 0
        m = 0
        for i in range(t):
            a, b = map(int, input().split())
            atk.append(a)
            des.append(b)
            if (a**2 + b**2) > maxab:
                maxab = (a**2 + b**2)
                m = i
        secab = 0
        s = 0
        for i in range(t):
            if (atk[i]**2 + des[i]**2) > secab and (atk[i]**2 + des[i]**2) < maxab:
                secab = (atk[i]**2 + des[i]**2) 
                s = i
        print(atk[s], des[s])
    except:
        break
