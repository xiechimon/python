# 判断 n 以内的素数
# 素数：只能被 1 和自身整除的数，大于 1 的整数

# 埃氏筛
# 先定义一个bool数组表示所有数都是素数，从前面开始直接划去这个数的倍数，最后再便利一遍这个数组打印素数
from math import sqrt

n = 10
ans = []
is_primes = [True] * (n + 1)  # 下标即为数
is_primes[0] = is_primes[1] = False  # 0和1不是素数

# 为什么到√n？ - 因为筛素数的时候要从 i² 开始筛，i² <= n
# i 是用于划去他的平方数
for i in range(2, int(sqrt(n)) + 1):
    # 如果i是素数，则他的倍数都不是素数
    if is_primes[i]:
        for j in range(i**2, n + 1, i):
            is_primes[j] = False

for i in range(2, n + 1):
    if is_primes[i]:
        ans.append(i)

print(ans)



# My method
# import sys
# import math
# input = lambda: sys.stdin.readline().strip()  # noqa: E731

# n = int(input())
# ans = []

# for num in range(2, n + 1):
#     # 检查 num
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             break
#     else:
#         ans.append(num)

# print(ans)
