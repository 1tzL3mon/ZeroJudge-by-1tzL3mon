a = int(input())
for _ in range(a):
    err = []
    n = input().split()
    m = input().split()
    if n[1] == n[3] or n[1] != n[5] or m[1] == m[3] or m[1] != m[5]:
        if 'A' not in err:
            err.append('A')
    if int(n[6]) != 1 or int(m[6]) != 0:
        if 'B' not in err:
            err.append('B')
    if n[1] == m[1] or n[3] == m[3] or n[5] == m[5]:
        if 'C' not in err:
            err.append('C')
    if not err:
        print('None')
    else:
        print(''.join(err))
