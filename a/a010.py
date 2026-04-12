while True:
    try:
        n = int(input())
        ans = []
        d = 2
        while n > 1: #只要n還沒有被除盡
            count = 0
            while n % d == 0: #如果n可以被d整除，便會開始執行
                count += 1
                n //= d
            if count > 0:
                if count == 1:
                    ans.append(str(d)) #直接把d當成文字儲存
                else:
                    ans.append(f"{d}^{count}") #直接把d^count當成文字儲存
            d += 1
            if d * d > n and n > 1: #如果一直到根號n都沒有找到n的因數，代表n是質數
                ans.append(str(n))
                break
        print(" * ".join(ans))
    except:
        break
