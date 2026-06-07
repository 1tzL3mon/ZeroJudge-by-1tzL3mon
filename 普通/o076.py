while True: #修正前，AC但很醜
    try:
        k = int(input())
        x = list(map(int, input().split()))
        sh = list()
        m = 0
        for i in range(1, k):
            m += 1
            if x[i] >= x[i-1]:
                sh.append(m)
                m = 0
        m += 1 #超級醜，我發現我最range必須只跑4次，但這樣最後一個會少算一次，所以我強行加在最後面
        sh.append(m) #反正是找最大值，他最後一個滑翔距離會重複又沒差
        print(max(sh))
    except:
        break

while True: #修正過後
    try:
        k = int(input())
        x = list(map(int, input().split()))
        sh = list()
        m = 1 #一開始就由1開始，就不會有一次內+=1又append，導致最後一次比較的時候是加到倒數第2個的+=
        for i in range(1, k):
            if x[i] >= x[i-1]:
                sh.append(m)
                m = 1
            else:
                m += 1
        sh.append(m)
        print(max(sh))
    except:
        break
