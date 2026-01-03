while True:
    try:
        num = int(input())
        list = []
        for _ in range(num):
            list.append(int(input()))
        list.sort()
        for i in range(num):
            print(list[i])
    except:
        break
