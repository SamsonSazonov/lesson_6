max, c, a = 0, 0, int(input())
while(a):
    if a > max: max, c = a, 1
    elif a == max: c += 1
    a = int(input())
print(c)
