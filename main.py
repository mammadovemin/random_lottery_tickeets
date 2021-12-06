import random

numbers = set(range(1, 41))
out_num = [2, 8, 9, 14, 23, 37,
           5, 6, 7, 11, 31, 35,
           24, 28, 29, 33, 39, 40,
           1, 10, 19, 28, 30, 35,
           10, 11, 15, 20, 21, 27,
           ]

res = numbers - set(out_num)

for _ in range(10):
    print(sorted(random.sample(list(res), 6)))

print(sorted(res))
