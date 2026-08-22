import sys
from datetime import date

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    for i in range(0, len(input_data), 6):
        y1 = int(input_data[i])
        m1 = int(input_data[i+1])
        d1 = int(input_data[i+2])
        y2 = int(input_data[i+3])
        m2 = int(input_data[i+4])
        d2 = int(input_data[i+5])
        date1 = date(y1, m1, d1)
        date2 = date(y2, m2, d2)
        diff_days = abs((date1 - date2).days)
        print(diff_days)

if __name__ == '__main__':
    solve()
