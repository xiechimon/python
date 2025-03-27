# 螺旋矩阵 [[1,2,3][8,9,4][7,6,5]]
# [1, 2, 3]
# [8, 9, 4]
# [7, 6, 5]
# (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2) -> (3, 2) -> ...
# 定义‘右下左上’四个方位，如果遇到边界或不为0的元素就更改方向

n = 3
matrix = [[0] * n for _ in range(n)]
direction = [[0,1], [1,0], [0, -1],[-1,0]]
p, q = 0, 0  # 控制矩阵下标
d = 0  # 控制方向

for num in range(1, n**2 + 1):
    matrix[p][q] = num

    # 存放下一步走的位置，防止越界
    a = p + direction[d][0]
    b = q + direction[d][1]

    # 碰到边界或不为0，改变方向
    if  (a >= n or  a < 0 or b >= n or b < 0) or matrix[a][b] != 0:
        d = (d + 1) % 4

    p += direction[d][0]
    q += direction[d][1]


for i in matrix:
    print(i)