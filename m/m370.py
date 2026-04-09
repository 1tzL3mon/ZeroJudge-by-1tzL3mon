while True:
    try:
        st, f = map(int, input().split())
        spo = list(map(int, input().split()))
        sm = 0
        minspo = 100000
        bi = 0
        maxspo = 0
        for i in range(f):
            if spo[i] < st:
                sm += 1
            if spo[i] < minspo:
                minspo = spo[i]
            if spo[i] > st:
                bi += 1
            if spo[i] > maxspo:
                maxspo = spo[i]
        if sm > bi:
            print(sm, minspo)
        else:
            print(bi, maxspo)
    except:
        break
