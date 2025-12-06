while True:
    try:
        days = int(input())
    except:
        break
    enumbers = input().split()
    if len(enumbers) != days:
        break
    sum = 0
    for i in range(days):
        try:
            sum += int(enumbers[i]) * (i+1)
        except:
            break
    print(sum)
