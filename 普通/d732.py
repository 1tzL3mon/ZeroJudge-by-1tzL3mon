# 二分搜尋法

n, k = map(int, input().split())
numbers = list(map(int, input().split())) #numbers一定會遞增
queries = list(map(int, input().split()))
for target in queries:
    left = 0
    right = n - 1
    ans_index = 0  #預設找不到，索引值為 0
    while left <= right:
        # 找出正中間的位置（用整除 // 2）
        mid = (left + right) // 2
        
        # 狀況 A：中間的值剛剛好就是要找的數字
        if numbers[mid] == target:
            ans_index = mid + 1  # 題目要求從 1 開始數，所以索引值要加 1
            break                # 找到了，直接跳出 while 迴圈
            
        # 狀況 B：中間的值太大，代表目標在左半邊
        elif numbers[mid] > target:
            right = mid - 1      # 把右邊界縮小到中間的左邊一格
            
        # 狀況 C：中間的值太小，代表目標在右半邊
        else:
            left = mid + 1       # 把左邊界擴大到中間的右邊一格
            
    # 印出這一次搜尋的答案（有找到會是位置，沒找到會是 0）
    print(ans_index)
