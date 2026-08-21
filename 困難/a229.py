import sys

def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return
        
    for n_str in lines:
        n = int(n_str)
        total_len = n * 2
        path = bytearray(total_len)
        output = []
        def dfs(idx, left, right):
            if idx == total_len:
                output.append(path.decode('ascii'))
            if left < n:
                path[idx] = 40
                dfs(idx + 1, left + 1, right)
            if right < left:
                path[idx] = 41
                dfs(idx + 1, left, right + 1)
        dfs(0, 0, 0)
        sys.stdout.write('\n'.join(output) + '\n\n')

if __name__ == '__main__':
    solve()
