n = int(input())
i = 0
b = n
count = count_m = 0
while n != 0:
    if b == n:
        count = count + 1
    else:
        b = n
        count = 1
    count_m = max(count_m, count)

    n = int(input())
    i = i + 1

print(count_m)