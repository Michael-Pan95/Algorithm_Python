import sys
import numpy as np

if __name__ == "__main__":
    # 读取第一行的n
    n = sys.stdin.readline().strip().split()
    ans = 0
    line_num = int(n[0])
    column_num = int(n[1])
    matrix = []
    for i in range(line_num):
        line = sys.stdin.readline().strip().split()
        matrix.append([int(num, 16) for num in line])

    # build empty matrix for route
    matrix2 = []
    for i in range(line_num):
        matrix2.append([[] for _ in range(column_num)])
    matrix3 = []
    for i in range(line_num):
        matrix3.append([[] for _ in range(column_num)])

    matrix2[0][0] = [matrix[0][0]]
    # 对第一行求唯一路径
    for i in range(1, column_num):
        matrix2[0][i] = [matrix2[0][i - 1][0] * matrix[0][i]]
    # 对第一列求唯一路径
    for i in range(1, line_num):
        matrix2[i][0] = [matrix2[i - 1][0][0] * matrix[i][0]]

    for i in range(1, column_num):
        matrix3[0][i].append(['>' for _ in range(i)])
    # 对第一列求唯一路径
    for i in range(1, line_num):
        matrix3[i][0].append(['v' for _ in range(i)])

    # 对剩余格求路径
    for i in range(1, line_num):
        for j in range(1, column_num):
            left_routes = matrix3[i][j - 1]
            top_routes = matrix3[i - 1][j]
            for left in left_routes:
                tmp = left
                tmp.extend(['>'])
                matrix3[i][j].append(tmp)
            for top in top_routes:
                tmp = top
                tmp.extend(['v'])
                matrix3[i][j].append(tmp)

    min_val = 10000000
    inde = -1
    for i in range(len(matrix3[line_num - 1][column_num - 1])):
        current_value = matrix[0][0]
        x = 0
        y = 0
        for s in matrix3[line_num - 1][column_num - 1][i]:
            if s == '>':
                y += 1
            else:
                x += 1
            current_value *= matrix[x][y]

        result = str(hex(current_value)[::-1])
        count = 0
        for j in result:
            if j == '0':
                count += 1
            else:
                break
        if count < min_val:
            min_val = count
            inde = i

    print(matrix2[line_num][column_num][i],min_val)

