while True:
    try:
        l = list(map(int, input().split()))
        p = 1
        if l[0] == l[1]:
            p+=1
        if l[1] == l[2]:
            p+=1
        if l[0] == l[2] and not ((l[0]==l[1]) and (l[1]==l[2])):
            p+=1
        fin = []
        for i in range(3):
            if l[i] not in fin:
                fin.append(l[i])
        fin.sort(reverse=True)
        print(p, *fin)
    except:
        break
