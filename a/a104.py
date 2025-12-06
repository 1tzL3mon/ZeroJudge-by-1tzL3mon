while True: #23行
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

#企鵝answer 13行
while True:
    try:
        num = int(input())
        data = input().split()
        ls = []
        for i in data:
            ls.append(int(i))
        ls.sort() #.sort()是列表的由小到大的整理功能
        for i in ls:
            print(i, end=" ") #還沒有print出來
        print() #此時才print出來
    except EOFError:
        break

