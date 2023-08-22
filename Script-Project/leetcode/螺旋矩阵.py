from typing import List
import numpy as np


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = np.zeros((n, n), dtype=int)  # 使用numpy创建一个矩阵，初始值为0
        dx, dy = 0, 1  # 用来表示x,y方向上移动的步长，这里为一步
        x, y = 0, 0  # 初始化矩阵起点为左上角
        for i in range(1, n * n + 1):  # 从1循环到n*n，即填入矩阵的数字范围
            res[x][y] = i  # 填入当前数字
            next_x, next_y = (x + dx) % n, (y + dy) % n  # 使用取模计算下一个数字的位置
            if res[next_x][next_y] != 0:  # 判断边界是否为0，非0则需要改变方向
                dx, dy = dy, -dx  # 以90度改变方向
                next_x, next_y = (x + dx) % n, (y + dy) % n  # 重新计算下一个数字的位置
            x, y = next_x, next_y  # 更新下一处数字的位置
        return res.tolist()


solution = Solution()
print(solution.generateMatrix(3))


