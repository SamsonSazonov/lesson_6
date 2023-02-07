n = int(input())
k = 0
p = 0
while n != 0:
    if p < n:
        k += 1
    p = n
    n = int(input())
print(k-1)
