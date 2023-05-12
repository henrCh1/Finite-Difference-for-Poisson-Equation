# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 15:05:28 2023

@author: 86319
"""

import math

# 定义函数f(x)、g(x)、d(x)和F(x,y)
def f(x):
    return 2 * math.pow(math.e, x)

def g(x):
    return x

def d(x):
    return math.pow(math.e, x)

def F(x, y):
    return x * math.pow(math.e, y)

a = 10 # 定义a和b
b = 5

h = 0.2 # 定义步长、松弛因子和误差限
w = 1.25
eps = 1e-4

solve = [[0] * (b + 1) for i in range(a + 1)] # 创建一个a+1行b+1列的二维数组solve

# 输入已知的边界条件
for i in range(a + 1):
    solve[i][0] = g(h * i)

for i in range(a + 1):
    solve[i][b] = d(h * i)

for j in range(b + 1):
    solve[0][j] = 0

for j in range(b + 1):
    solve[a][j] = f(h * j)

# 初始化待解的格点的值为0
for i in range(1, a):
    for j in range(1, b):
        solve[i][j] = 0

count = 0 # 记录迭代次数
max_error = 1 # 初始时，将最大误差置为1
result = 0

# 当最大误差小于误差限时停止迭代
while max_error >= eps:
    max_error = 0 # 每次迭代前将最大误差置为0
    for i in range(1, a):
        for j in range(1, b):
            result = solve[i][j]
            # 应用迭代公式
            solve[i][j] = ((w / 4) * (solve[i][j-1] + solve[i-1][j] + solve[i][j+1] + solve[i+1][j] - h * h * F(h * i, h * j))) + (1 - w) * result
            # 计算误差并更新最大误差
            if abs(result - solve[i][j]) > max_error:
                max_error = abs(result - solve[i][j])
    count += 1 # 迭代次数加1

print("最终答案是：")
for i in range(1, a):
    for j in range(1, b):
        if j == b - 1:
            print("{:.6f}".format(solve[i][j]))
        else:
            print("{:.6f}".format(solve[i][j]), end=" ")
print("循环次数为：{}".format(count))

# 输出真值表
print("真值表如下：")
for i in range(1, a):
    for j in range(1, b):
        if j == b - 1:
            print("{:.6f}".format(F(h * i, h * j)))
        else:
            print("{:.6f}".format(F(h * i, h * j)), end=" ")
