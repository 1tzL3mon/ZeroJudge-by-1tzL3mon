while True: #10行
    try:
        n = int(input())
        a = 1
        b = 1
        for _ in range(n-1):
            a, b = b, a+b #a變成b，b變成a+b
        print(b)
    except:
        break

#企鵝answer 13行
while True:
    try:
        n = int(input())
        sum = 0
        ls = [1]
        for i in range(1, n+1): #i從1開始
            if i == 1:
                ls.append(1)
            else:
                ls.append(ls[i-1]+ls[i-2])
        print(ls[n])
    except EOFError:
        break
