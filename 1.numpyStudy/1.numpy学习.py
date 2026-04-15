#%% md
# # 一、ndarray
# 
# ## 1.ndarray的特性
# ### 多维性
#%%
import numpy as np
#%%
arr = np.array(5)  # 创建0维的ndarray数组
print(arr)
print('arr的维度: ', arr.ndim)  # number of dimensions
#%%
arr = np.array([1, 2, 3])  # 创建1维的ndarray数组
print(arr)
print('arr的维度: ', arr.ndim)  # number of dimensions
#%%
arr = np.array([[1, 2, 3], [4, 5, 6]])  # 创建2维的ndarray数组
print(arr)
print('arr的维度: ', arr.ndim)  # number of dimensions
#%% md
# # 同质性
#%%
arr = np.array([1, 'hello'])  # 不同的数据类型会被强制转换成相同的数据类型
print(arr)  # '1' 和 1
#%%
arr = np.array([1, 2.5])  # 不同的数据类型会被强制转换成相同的数据类型
print(arr)  # 1. 和 1
#%% md
# ## 2.ndarray的属性
#%%
arr = np.array(1)
print(arr)
print('数组的形状: ', arr.shape)
print('arr的维度: ', arr.ndim)
print('元素的个数: ', arr.size)
print('元素的数据类型: ', arr.dtype)
print('元素的转置: ', arr.T)
#%%
arr = np.array([1, 2.5, 3])
print(arr)
print('数组的形状: ', arr.shape)
print('arr的维度: ', arr.ndim)
print('元素的个数: ', arr.size)
print('元素的数据类型: ', arr.dtype)
print('元素的转置: ', arr.T)
#%%
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print('数组的形状: ', arr.shape)
print('arr的维度: ', arr.ndim)
print('元素的个数: ', arr.size)
print('元素的数据类型: ', arr.dtype)
print('元素的转置: ', arr.T)
#%% md
# ## 3.ndarray的创建
#%%
# 基础的创建方法
list1 = [4, 5, 6]
arr = np.array(list1, dtype=np.float64)
print(arr.ndim)  # 属性
print(arr)
#%%
# copy
arr1 = np.copy(arr) # 深度拷贝
print(arr1)
arr1[0] = 8
print(arr1)
print(arr)
#%%
# 预定义形状
# 全0 全1 未初始化
# 全0
arr = np.zeros((2, 3))
print(arr)
print(arr.dtype)
arr = np.zeros((2, 3), dtype=int)
print(arr)
print(arr.dtype)
#%%
arr = np.zeros((2,), dtype=int)
print(arr)
#%%
# 全1
arr = np.ones((5, 8), dtype=int)
print(arr)
#%%
# 未初始化
arr = np.empty((2, 3), dtype=int)
print(arr)
arr = np.empty((4, 2))
print(arr)
arr = np.full((3, 4), 2025)
print(arr)
print()

arr1 = np.zeros_like(arr)
print(arr1)
arr1 = np.empty_like(arr)
print(arr1)
arr1 = np.ones_like(arr)
print(arr1)
arr1 = np.full_like(arr, 2026)
print(arr1)
#%%
# 等差数列 2 4 6 8 10
arr = np.arange(1, 10, 1)  # start,end,step(步长)
print(arr)
#%%
# 等间隔数列
arr = np.linspace(1, 10, 5)
print(arr)
arr = np.linspace(0, 100, 5)
print(arr)
arr = np.linspace(0, 100, 5, dtype=int)
print(arr)
#%%
# 对数间隔数列
arr = np.logspace(0, 4, 2, base=2)
print(arr)
arr = np.logspace(0, 4, 3, base=2)
print(arr)
arr = np.logspace(0, 4, 3, dtype=int)  # 默认base是10
print(arr)
arr = np.logspace(0, 4, 3)
print(arr)
#%%
# 特殊矩阵
# 单位矩阵:
arr = np.eye(3, dtype=int)
print(arr)
arr = np.eye(3, 4, dtype=int)
print(arr)
#%%
# 对角矩阵:
arr = np.diag([5, 1, 2, 3])
print(arr)
#%%
# 随机数组的生成
# 生成0到1之间的随机浮点数(均匀分布)
arr = np.random.rand(2, 3)
print(arr)
#%%
# 生成指定范围区间的随机浮点数
arr = np.random.uniform(3, 6, (2, 3))
print(arr)
#%%
# 生成指定范围区间的随机整数
arr = np.random.randint(3, 30, (2, 3))
print(arr)
#%%
# 生成随机数列(正态分布) (范围是全体实数,但大概率是-3到3)
arr = np.random.randn(2, 3)
print(arr)
#%%
# 设置随机种子(设置相同种子则能固定随机数序列)
np.random.seed(20)
arr = np.random.randint(1, 10, (2, 5))
print(arr)
#%% md
# ## 4.ndarray的数据类型
# ### 布尔类型 bool
# 
# ### 整数类型 int uint
# 
# ### 浮点数  float
# 
# ### 复数    complex
# 
#%%
arr = np.array([1, 0, 1, -1, 2, 0], dtype='bool')
print(arr)
#%%
arr = np.array([1, 0, 127, 0], dtype=np.int8)  # 最大127
print(arr)
#%% md
# ## 5.索引与切片
#%%
# 一维数组的索引与切片
arr = np.random.randint(1, 100, 20)
print(arr)
#%%
print(arr[10])
print(arr[:])
print(arr[2:5])
print(arr[slice(2, 15, 3)])
print(arr[arr > 10])
print(arr[(arr > 10) & (arr < 70)])
print(arr[(arr > 90) | (arr < 10)])
#%%
# 二维数组的索引与切片
arr = np.random.randint(1, 100, (4, 8))
print(arr)
#%%
print(arr[1, 3])
print(arr[1][3])
print(arr[:, :])
print(arr[1, :])
print(arr[1, 2:5])
print(arr[arr > 50])
print(arr[2])
print(arr[2][arr[2] > 50])
print(arr[:, 3])
#%% md
# ## 6.ndarray的运算
#%%
# 算术运算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# a=[1, 2, 3]
# b=[4, 5, 6]
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
#%%
c = [1, 2, 3]
d = [4, 5, 6]
print(c + d)
# print(c-d)
#%%
# 算术运算
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[4, 5, 6], [7, 8, 9], [1, 2, 3]])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
#%%
# 数组与标量之间的算术运算
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a + 3)
print(a * 3)
#%%
# 广播机制
a = np.array([1, 2, 3])  # 1*3
b = np.array([[4], [5], [6]])  # 3*1
print(a + b)
print(b - a)
#%%
# a=np.array([1,2,3]) # 1*3
# b=np.array([4,5])
# print(a+b)
#%%
# 矩阵运算
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = (np.array([[4, 5, 6], [7, 8, 9], [1, 2, 3]]))
print(a * b)
print(a @ b)
#%% md
# # 二、numpy中的常用函数
# ## 1.基本数学函数
#%%
# 计算平方根
print(np.sqrt(9))
print(np.sqrt([1, 4, 9]))
arr = np.array([1, 25, 81])
print(np.sqrt(arr))
#%%
# 计算指数 e^x=y
print(np.exp(1))  # e
print(np.exp(0))  # e
#%%
# 计算自然对数 lny=x
print(np.log(2.71))
#%%
# 计算正弦值、余弦值
print(np.sin(np.pi))
print(np.sin(np.pi / 2))
print(np.cos(np.pi))
#%%
# 计算绝对值
arr = np.array([-1, 1, 2, -3])
print(np.abs(arr))
#%%
# 计算a的b次幂
print(np.power(arr, 2))
#%%
# 四舍五入
print(np.round([3.2, 4.5, 8.1, 9.6]))
#%%
# 向上取整,向下取整
arr = np.array([1.6, 25.1, 81.7])
print(np.ceil(arr))
print(np.floor(arr))
#%%
# 检测缺失值
np.isnan([1, 2, 3])
np.isnan([1, 2, np.nan, 3])
#%% md
# ## 2.统计函数
# 
# 求和、计算平均值、计算中位数、标准差、方差
# 
# 查找最大值、最小值
# 
# 计算分位数、累积和、累积差
#%%
arr = np.random.randint(1, 20, 8)
print(arr)
#%%
# 求和
print(np.sum(arr))
#%%
# 计算平均值
print(np.mean(arr))
#%%
# 计算中位数
print(np.median(arr))
#%%
# 计算标准差、方差
print(np.var([1, 2, 3]))
print(np.std([1, 2, 3]))
#%%
# 计算最大值、最小值
print(arr)
print(np.max(arr), np.argmax(arr))
print(np.argmin(arr))
print(np.min(arr), np.argmin(arr))
#%%
# 分位数(不同方法得到的结果可能不一样)
# 中位数
print(np.median([1, 2, 3]))
print(np.median([1, 2, 3, 4]))
np.random.seed(0)
arr = np.random.randint(0, 100, 4)
print(arr)
print(type(arr))
print(np.median(arr))
print(np.percentile(arr, 50))
print(np.percentile(arr, 20))
print(np.percentile(arr, 0))
print(np.percentile(arr, 100))
print(np.percentile(arr, 25))
#%%
# 累计和、累积积
arr = np.array([1, 2, 3])
print(np.sum(arr))
print(np.cumsum(arr))
print(np.prod(arr))
print(np.cumprod(arr))
#%% md
# ## 比较函数
# ### 比较是否大于、小于、等于
# ### 逻辑与、或、非
# ### 检查数组中是否有一个True,是否所有的都为True,自定义条件
#%%
# 是否大于
print(np.greater([3, 4, 5, 6, 7], 4))
# 是否小于
print(np.less([3, 4, 5, 6, 7, 8], 4))
# 是否等于
print(np.equal([3, 4, 5, 6, 7, 8], 4))
print(np.equal([3, 4, 5], [4, 4, 4]))
# print(np.equal([3,4,5],[4,4,3,4]))
#%%
print(np.logical_and([1, 0], [1, 1]))
print(np.logical_or([0, 0], [1, 0]))
print(np.logical_not([1, 0]))
#%%
# 检查元素是否至少有一个元素为True
print(np.any([0, 0, 0, 0, 0]))
print(np.any([0, 0, 0, 1, 0]))
# 检查是否全部元素为True
print(np.all([1, 1, 0, 0, 0]))
print(np.all([1, 1, 1]))
#%%
# 自定义条件
# print(np.where(条件,符合条件,不符合条件的))
arr = np.array([1, 2, 3, 4, 5])
print(np.where(arr > 3, arr+1, 0))
#%%
arr = np.array([1, 2, 3, 4, 5])
print(np.where(arr < 3, 1, 0))
#%%
score = np.random.randint(50, 100, 20)
print(score)
print(np.where(score >= 60, '及格', '不及格'))
#%%
print(np.where(
    score < 60, '不及格', np.where(
        score < 80, '良好', '优秀'
    )
))
#%%
# np.select(条件,返回的结果)
print(np.select([score > 80, (score >= 60) & (score < 80), score < 60],
                ['优秀', '良好', '不及格']))
print(np.select([score > 80, (score >= 60) & (score < 80), score < 50],
                ('优秀', '良好', '不及格'),
                default='未知'))
#%% md
# ## 排序函数
#%%
np.random.seed(0)
arr = np.random.randint(1, 100, 20)
print(arr)
print(arr.sort())
print(arr)

print()

np.random.seed(0)
arr = np.random.randint(1, 100, 20)
print(np.sort(arr))
print(np.argsort(arr))
print(arr)
#%% md
# ## 去重函数
#%%
print(np.unique(arr))
#%% md
# 
#%% md
# ## 数组的拼接
#%%
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)
print(np.concatenate((arr1, arr2)))
#%% md
# ## 数组的分割
#%%
print(np.split(arr, [6, 12, 18]))
print(np.split(arr, 4))
#%% md
# ## 调整数组的形状
#%%
print(np.reshape(arr, (4, 5)))