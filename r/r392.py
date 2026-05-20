#校長站在會場出口，問了若干位同學：「你知道全校新生中有多少人和你有一樣的帽子顏色嗎？」
#10
#3 3 3 726 255 0 255 1 1 1
#4+727+256+1+2+2=992 輸出992

while True: #AI寫的
    try:
        n = int(input())
        en = list(map(int, input().split()))
        counts = {} #把次數弄為字典
        for x in en:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        ans = 0
        for answer, count in counts.items(): #字典.items()可以用在for迴圈
            group_size = answer + 1
            num_groups = (count + group_size - 1) // group_size
            ans += num_groups * group_size
        print(ans)
    except:
        break
