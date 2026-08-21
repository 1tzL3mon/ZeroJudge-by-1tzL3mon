import sys
import math

input_data = sys.stdin.read().split()
if input_data:
    for idx in range(0, len(input_data), 2):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        if a > b:
            print(0)
            continue
        prime_count = 0
        for num in range(a, b + 1):
            if num <= 1:
                continue
            if num <= 3:
                prime_count += 1
                continue
            if num % 2 == 0 or num % 3 == 0:
                continue
            is_prime = True
            sqrt_num = int(math.isqrt(num))
            for i in range(5, sqrt_num + 1, 6):
                if num % i == 0 or num % (i + 2) == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_count += 1
                
        print(prime_count)
