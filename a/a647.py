from decimal import Decimal, ROUND_HALF_UP

def proper_round(number, decimal_places):
    d = Decimal(str(number))
    target = Decimal('1e-{}'.format(decimal_places))
    return d.quantize(target, rounding=ROUND_HALF_UP)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    pointer = 1
    for _ in range(n):
        if pointer + 1 >= len(input_data):
            break
        pbuy = Decimal(input_data[pointer])
        pnow = Decimal(input_data[pointer + 1])
        pointer += 2
        prof = (pbuy - pnow) * 100 / pbuy 
        display_val = proper_round(prof, 2)
        if display_val == 0:
            display_val = Decimal('0.00')
        if prof >= 7 or prof <= -10:
            print(f"{display_val}% dispose")
        elif prof <= -7 or prof >= 10:
            print(f"{display_val}% dispose")
        else:
            print(f"{display_val}% keep")
            
def final_proper_logic():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    pointer = 1
    for _ in range(n):
        pbuy = Decimal(input_data[pointer])
        pnow = Decimal(input_data[pointer+1])
        pointer += 2
        raw_prof = 100 - (pnow * 100 / pbuy)
        ans = -1 * proper_round(raw_prof, 2)
        if ans == 0: ans = Decimal('0.00')
        check_val = -1 * raw_prof
        if check_val <= -7 or check_val >= 10:
            print(f"{ans}% dispose")
        else:
            print(f"{ans}% keep")

final_proper_logic()
