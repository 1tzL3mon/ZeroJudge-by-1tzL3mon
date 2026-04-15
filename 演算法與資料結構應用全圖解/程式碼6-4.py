#使用二元搜尋法加速「數對和最適化問題」的全域搜尋解法
#3-4 求數對和之最小值
import bisect

def solve():
    try:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
    except EOFError:
        return

    inf = float('inf')
    min_value = inf

    # 對 b 進行排序
    b.sort()
    
    # Python 的 bisect 會回傳索引，不需要像 C++ 額外 push_back(INF)
    # 但為了邏輯一致性，我們直接處理回傳的索引
    
    for x in a:
        # 目標是找到 b[j] 使得 x + b[j] >= k，即 b[j] >= k - x
        target = k - x
        
        # bisect_left 相當於 C++ 的 lower_bound
        idx = bisect.bisect_left(b, target)
        
        # 如果索引在範圍內，代表找到了滿足條件的 b[j]
        if idx < len(b):
            val = b[idx]
            if x + val < min_value:
                min_value = x + val

    print(min_value)

if __name__ == "__main__":
    solve()





try:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
except:
    exit()
b.sort()
min_value = float('inf')
for x in a:
    target = k - x #找b大於k-x的最小值
    low = 0
    high = len(b) - 1
    best_idx = -1
    while low <= high: #二分搜尋到都搜尋完為止
        mid = (low + high) // 2
        if b[mid] >= target:
            best_idx = mid  
            high = mid - 1 #下一次搜尋範圍就不用包含mid
        else:
            low = mid + 1
    if best_idx != -1:
        res = x + b[best_idx] #把a加回best_idx的b上
        if res < min_value:
            min_value = res
print(min_value)
