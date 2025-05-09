# %% 导入库
import math
import matplotlib.pyplot as plt

# %% 简单变量计算
radius = 5
area = math.pi * radius ** 2
print(f"Area of circle: {area:.2f}")

# %% 绘图示例
x = [i for i in range(100)]
y = [math.sin(i / 10) for i in x]

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()

# %% 测试函数


def square(n):
    return n * n


print("Square of 7:", square(7))
