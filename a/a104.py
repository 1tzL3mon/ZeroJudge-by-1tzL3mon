while True:
    try:
        n = int(input())
    except:
        break
    i = input().split()
    if len(i) != n:
        break
    try:
        for t in range(n-1):
            for s in range (n-1):
                if int(i[s]) > int(i[s+1]):
                    temp = i[s]
                    i[s] = i[s+1]
                    i[s+1] = temp
    except:
        break
    output = ''
    for p in range(n-1):
        output += i[p]
        output += ' '
    output += i[n-1]
    print(output)
