while True:
    try:
        n = int(input())
        if n == 0:
            break
        print(*(i for i in range(1, n) if i % 7 != 0))
    except:
        break
