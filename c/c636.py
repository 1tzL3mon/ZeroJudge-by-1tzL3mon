zodiac = ['鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊', '猴', '雞', '狗', '豬'] #12行
while True:
    try:
        m = int(input())
        if m < 0: #沒有0年，1年的前一年是-1年，負號往前一格
            m += 1
        elif m == 0: #沒有0年，1年的前一年是-1年
            continue
        n = m + 1911
        print(zodiac[(n-3)%12-1])
    except EOFError:
        break
