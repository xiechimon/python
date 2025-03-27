# 快读模板，可提高读入数据效率
import sys
input = lambda: sys.stdin.readline().strip()  # noqa: E731

# 常见输入格式
# 0.多行单个
# n1 = int(input())  # 行数
# lst1 = [int(input()) for _ in range(n1)]  # 读取n次，将每一次读取到的数放入列表
# 1.多行多个（矩阵）
# n2, m2 = map(int, input().split())  # 矩阵大小，其实m没必要
# matrix = [list(map(int, input().split())) for _ in range(n2)]

# 列表推导器
n = 3
zero_matrix = [[0] * n  for _ in range(n) ]
print(zero_matrix)
