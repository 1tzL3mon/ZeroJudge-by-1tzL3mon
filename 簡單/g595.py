while True:
    try:
        t = int(input())
        li = list(map(int, input().split()))
        fin = 0
        for i in range(t):
            if li[i] == 0:
                if i == 0:
                    fin += li[i+1]
                elif i == (t-1):
                    fin += li [i-1]
                else:
                    if li[i-1] >= li[i+1]:
                        fin += li[i+1]
                    else:
                        fin += li[i-1]
        print(fin)
    except:
        break
