while True: #AI寫的
    try:
        n = int(input())
        en = list(map(int, input().split()))
        counts = {}
        for x in en:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        ans = 0
        for answer, count in counts.items():
            group_size = answer + 1
            num_groups = (count + group_size - 1) // group_size
            ans += num_groups * group_size
        print(ans)
    except:
        break
