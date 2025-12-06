while True: #21行
    try:
        times = int(input())
    except:
        break
    l = []
    for t in range(times):
        l.append(input()) #空list增加新物件要用append
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

#企鵝answer 12行
ip = int(input())
for i in range(ip):
    data = input().split()
    num = int(data[0])
    if num == 1:
        print(int(data[1]) + int(data[2])) #每次輸入完就直接輸出
    elif num == 2:
        print(int(data[1]) - int(data[2]))
    elif num == 3:
        print(int(data[1]) * int(data[2]))
    else:
        print(int(int(data[1]) / int(data[2])))
