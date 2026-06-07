# 範例輸入1  20
# 範例輸出1  2^2 * 5

while True:
    try:
        n = int(input())
        ans = []
        d = 2
        while n > 1: #只要n還沒有被除盡
            count = 0
            while n % d == 0: #如果n可以被d整除，便會開始除以d並增加coumt直到無法再被d整除為止
                count += 1
                n //= d
            if count > 0: #如果count大於0，代表剛才有至少除以d至少一次
                if count == 1:
                    ans.append(str(d)) #直接把d當成文字儲存
                else:
                    ans.append(f"{d}^{count}") #直接把d^count當成文字儲存
            d += 1
            if d * d > n and n > 1: #如果d一直到根號n (d^2>n) 都沒有找到n的因數，代表n是質數
                ans.append(str(n))
                break
        print(" * ".join(ans))
    except:
        break
