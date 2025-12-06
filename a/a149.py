T = int(input()) #Grok的答案 15行
for _ in range(T):
    num = input().strip()
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
