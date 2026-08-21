T = int(input()) #Grok的答案 15行
for _ in range(T):
    num = input().strip() #.strip()可以移除開頭和結尾的空格
    product = 1
    has_zero = False
    for c in num: #c是各個num裡的數字
        if c == '0':
            has_zero = True
            break
        else:
            product *= int(c)
    if has_zero:
        print(0)
    else:
        print(product)




#2026我的Answer
while True:
    try:
        t = int(input())
        for _ in range(t):
            num = list(map(int, list(input())))
            answer = 1
            for i in num:
                answer *= i
            print(answer)
    except:
        break
