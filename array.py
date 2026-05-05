import numpy as np

# 1次元配列
arr1d = np.array([1, 2, 3, 4, 5])
print("1次元配列:", arr1d)

# 2次元配列
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2次元配列:\n", arr2d)

# ゼロ配列
zeros = np.zeros((3, 3))
print("ゼロ配列:\n", zeros)

# 等差数列
arange = np.arange(0, 10, 2)
print("等差数列:", arange)

# 乱数配列
rng = np.random.default_rng(seed=42)
random_arr = rng.random((3, 3))
print("乱数配列:\n", random_arr)

# 基本統計
print("平均:", arr1d.mean())
print("合計:", arr1d.sum())
print("最大値:", arr1d.max())
