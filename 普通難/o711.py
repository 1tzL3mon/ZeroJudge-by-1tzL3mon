while True:
    try:
        a = int(input())
        x, y, g, h = map(int, input().split())
        ki = list(map(int, input().split()))
        left = (x**2) * g + (y**2) * h
        xh = (x**2) * g
        yh = (y**2) * h
        et = list()
        for i in ki:
            if left <= 0: #append(0)，這樣找最大值時就會自動跳過
                et.append(0)
                continue
            if i >= left:
                if left > yh:
                    et.append(h + (left - yh) // (x**2))
                else:
                    et.append(left // (y**2))
                left = 0
            else:
                if left > yh:
                    if left - i >= yh:
                        et.append(i // (x**2))
                    else:
                        et.append((left - yh) // (x**2) + (i - (left - yh)) // (y**2))
                else:
                    et.append(i // (y**2))
                left -= i
        print(int(max(et)))
    except:
        break
