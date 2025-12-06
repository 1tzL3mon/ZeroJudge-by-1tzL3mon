while True:
    try:
        times = int(input())
    except:
        break
    l = []
    for t in range(times):
        l.append(input())
    for s in range(times):
        try:
            if int(l[s].split()[0]) == 1:
                print(int(l[s].split()[1]) + int(l[s].split()[2]))
            elif int(l[s].split()[0]) == 2:
                print(int(l[s].split()[1]) - int(l[s].split()[2]))
            elif int(l[s].split()[0]) == 3:
                print(int(l[s].split()[1]) * int(l[s].split()[2]))
            elif int(l[s].split()[0]) == 4:
                print(int(l[s].split()[1]) // int(l[s].split()[2]))
        except:
            break
    break
