while True:
    try:
        alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        num = input().upper()
        lis = list(num)
        su = 0
        for i in lis:
            su += alp.index(i) + 1
        print(su)
    except:
        break
