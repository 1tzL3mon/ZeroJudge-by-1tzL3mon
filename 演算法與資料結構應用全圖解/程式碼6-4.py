import bisect

def solve():
    # 讀取輸入
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
  
