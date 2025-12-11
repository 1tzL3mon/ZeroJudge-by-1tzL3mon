while True: #10行
    try:
        n = int(input())
        a = 1
        b = 1
        for _ in range(n-1):
            a, b = b, a+b #a變成b，b變成a+b
        print(b)
    except:
        break
