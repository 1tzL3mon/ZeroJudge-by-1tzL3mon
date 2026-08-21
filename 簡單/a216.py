import sys

input_data = sys.stdin.read().split()
if not input_data:
    pass

for n_str in input_data:
    n = int(n_str)
    fn = n * (n + 1) // 2
    gn = n * (n + 1) * (n + 2) // 6
    print(f"{fn} {gn}")
