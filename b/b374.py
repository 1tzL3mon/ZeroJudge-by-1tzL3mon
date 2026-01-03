n = int(input())
all_nums = map(int, input().split())
counts = {}
for x in all_nums:
    counts[x] = counts.get(x, 0) + 1
max_freq = max(counts.values())
for x in sorted(counts.keys()):
    if counts[x] == max_freq:
        print(x, max_freq)
