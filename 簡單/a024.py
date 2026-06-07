# 給定兩個整數，求最大公因數

a, b = map(int, input().split())
while b != 0:
    remainder = a % b  #輾轉相除，如果a可以被b整除，接下來b就會變成0
    a = b
    b = remainder
print(a)  #當b變成0的時候，迴圈停止，此時的a就是最大公因數
