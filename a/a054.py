while True:
    try:
        citi = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z', 'I', 'O']
        num = input()
        if len(num) != 9:
            continue
        lis = list(num)
        result = []
        for i in range(26):
            su = 0
            if i+10 < 20:
                su += 1 + i*9
            elif i+10 < 30:
                su += 2 + (i-10)*9
            else:
                su += 3 + (i-20)*9
            for j in range(8):
                su += (int(lis[j]) * (8-j))
            if (10 - (su % 10)) % 10 == int(lis[8]):
                result.append(citi[i])
        result.sort() #因為I跟O在最後面，但print的時候要照字母順序，所以要.sort()
        print(''.join(result))
    except:
        break
