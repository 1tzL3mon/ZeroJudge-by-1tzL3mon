while True:
    try:
        t = int(input())
        x = [0]
        y = [0]
        for _ in range(t):
            a, b = map(int, input().split())
            x.append(a)
            y.append(b)
        pre = [0, 0] #上一個方向
        now = [0, 0]
        leftturn = 0
        rightturn = 0
        uturn = 0
        for i in range(t): #一大堆如果句
            if (x[i+1] - x[i]) > 0:
                now = [1, 0]
                if pre[1] == 1:
                    rightturn +=1
                if pre[1] == -1:
                    leftturn +=1
                if pre[0] == -1:
                    uturn += 1
            if (x[i+1] - x[i]) < 0:
                now = [-1, 0]
                if pre[1] == -1:
                    rightturn +=1
                if pre[1] == 1:
                    leftturn +=1
                if pre[0] == 1:
                    uturn += 1
            if (y[i+1] - y[i]) > 0:
                now = [0, 1]
                if pre[0] == -1:
                    rightturn +=1
                if pre[0] == 1:
                    leftturn +=1
                if pre[1] == -1:
                    uturn += 1
            if (y[i+1] - y[i]) < 0:
                now = [0, -1]
                if pre[0] == 1:
                    rightturn +=1
                if pre[0] == -1:
                    leftturn +=1
                if pre[1] == 1:
                    uturn += 1
            pre = list(now) #pre設為現在方向，並繼續下一次迴圈
        print(leftturn, rightturn, uturn)
    except:
        break
