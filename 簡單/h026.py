while True:
    try:
        bfr = int(input())
        bli = []
        bli.append(bfr)
        rou = int(input())
        sli = list(map(int, input().split()))
        finish = 0
        if rou >= 2:
            bli.append(sli[0])
        if rou >= 3:
            for i in range(2, rou):
                if sli[i-1] == sli[i-2]:
                    if sli[i-1] == 0:
                        bli.append(5)
                    if sli[i-1] == 2:
                        bli.append(0)
                    if sli[i-1] == 5:
                        bli.append(2)
                else:
                    bli.append(sli[i-1])
        for i in range(rou):
            if finish == 0:
                print(f'{bli[i]} ',end='')
            if bli[i] == 5 and sli[i] == 0 and finish == 0:
                print(f': Won at round {i+1}')
                finish = 1
            if bli[i] == 0 and sli[i] == 2 and finish == 0:
                print(f': Won at round {i+1}')
                finish = 1
            if bli[i] == 2 and sli[i] == 5 and finish == 0:
                print(f': Won at round {i+1}')
                finish = 1
            if bli[i] == 0 and sli[i] == 5 and finish == 0:
                print(f': Lost at round {i+1}')
                finish = 1
            if bli[i] == 2 and sli[i] == 0 and finish == 0:
                print(f': Lost at round {i+1}')
                finish = 1
            if bli[i] == 5 and sli[i] == 2 and finish == 0:
                print(f': Lost at round {i+1}')
                finish = 1
        if finish == 0:
            print(f': Drew at round {rou}')
    except:
        break
