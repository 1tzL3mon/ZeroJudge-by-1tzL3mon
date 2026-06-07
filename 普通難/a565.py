# 第一行n，代表接下來會有n行

#Gemini的解法
n = int(input())
for _ in range(n):
    line = input()
    p_count = 0  # 記錄目前手上有幾個還沒配對的 'p'
    pair_count = 0  # 記錄成功配對的總對數
    for char in line:
        if char == 'p':
            p_count += 1  # 遇到 p，未配對的 p 增加一個
        elif char == 'q':
            if p_count > 0:  # 遇到 q，且前面有 p 可以配對
                p_count -= 1  # 配對成功，扣掉一個 p
                pair_count += 1 
    print(pair_count)



import sys

def solve():
    # 讀取 n，並處理可能的多餘換行
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line.strip())
    
    for _ in range(n):
        text = sys.stdin.readline().strip()
        stack = []
        groups = 0
        
        for char in text:
            if char == 'p':
                stack.append('p')
            elif char == 'q':
                # 如果看到 q，且前面有 p 可以配對
                if stack and stack[-1] == 'p':
                    stack.pop() # 把配對成功的 p 拿掉
                    groups += 1
                else:
                    # 如果 q 沒人配對，看題目需求，通常就忽略或存入 stack
                    pass 
        
        print(groups)

if __name__ == '__main__':
    solve()
