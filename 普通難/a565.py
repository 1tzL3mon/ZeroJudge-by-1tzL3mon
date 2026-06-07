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
