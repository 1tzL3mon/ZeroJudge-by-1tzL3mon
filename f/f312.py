a1, b1, c1 = map(int, input().split()) #3個元素分別都是int
a2, b2, c2 = map(int, input().split())
nsum = int(input())
su = a1*(0**2) + b1*0 + c1 + a2*(nsum**2) + b2*nsum + c2 #i等於0的情況
for i in range(nsum + 1):
    j = nsum - i
    current_val = (a1*i*i + b1*i + c1) + (a2*j*j + b2*j + c2)
    if current_val > su:
        su = current_val
print(su)
