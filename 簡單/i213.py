# 實作stack相關的基本操作
# 有一個N，代表接下來會有N行
# 開頭k若為1，後面會有一個數字，在stack頂端加入該數字
# 開頭k若為2，輸出堆疊最頂端的元素，如果當前堆疊內沒有元素，請輸出 −1 
# 開頭k若為3，刪除堆疊最頂端的元素，如果當前堆疊內沒有元素，請無視該操作

while True:
    try:
        stac = []
        n = int(input())
        for n in range(n):
            m = list(map(int, input().split()))
            if m[0] == 1:
                stac.append(m[1])
            elif m[0] == 2:
                if stac:
                    print(stac[-1])
                else:
                    print(-1)
            elif m[0] == 3:
                if stac:
                    stac.pop()
    except:
        break
