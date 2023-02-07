from math import sqrt

p_sum = 0
sum_squares = 0
x_i = int(input())
n = 0
while x_i != 0:
    n += 1
    p_sum += x_i
    sum_squares += x_i ** 2
    x_i = int(input())
print(sqrt((sum_squares - p_sum ** 2 / n) / (n - 1)))