while True:
    try:
        num = int(input())
        while num >= 10:
            adding = 0
            for i in str(num):
                adding += int(i)
            num = adding
        if (num == 3) or (num == 6) or (num == 9) or (num == 0):
            print("YES")
        else:
            print("NO")
    except:
        break
