# 螺旋矩阵 [[1,2,3][8,9,4][7,6,5]]
# [1, 2, 3]
# [8, 9, 4]
# [7, 6, 5]
# (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2) -> (3, 2) -> ...
# 定义‘右下左上’四个方位，默认从这个方向开始，循环
n = 3
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
matrix = [[0] * n for _ in range(n)]

i, j = 0, 0  # 默认索引
for idx in range(1, n ** 2 + 1):
    matrix[i, j] = idx
    if matrix[i , j + 1]: 
        i += directions[0][0]
        j += directions[0][1]
    elif matrix[i + 1 , j]: 
        i += directions[1][0]
        j += directions[1][1]
    elif matrix[i , j - 1]: 
        i += directions[2][0]
        j += directions[2][1]
    else: 
        i += directions[3][0]
        j += directions[3][1]

print(matrix)

    

