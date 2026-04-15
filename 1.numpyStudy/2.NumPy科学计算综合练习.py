#%% md
# # 二、NumPy科学计算综合练习
#%%
"""
题目1: 温度数据分析
某城市一周的最高气温为[28,30,29,31,32,30,29]
- 计算平均气温、最高气温和最低气温
- 找出气温超过30的天数
"""
import numpy as np

temps = np.array([28, 30, 29, 31, 32, 30, 29])
print(temps)
print('平均气温:', '%.3f' % np.mean(temps))
print('最高气温:', np.max(temps))
print('最低气温:', np.min(temps))
print('气温超过30的天数:', len(temps[temps > 30]))
print(np.where(temps > 30, temps, 0))
print(np.cumsum(np.where(temps > 30, 1, 0))[-1])
print(np.count_nonzero(temps > 30))
#%%
"""
题目2:学生成绩统计
某班级5名学生的成绩[85,90,78,92,88]
- 计算成绩的平均分、中位数和标准差
- 将成绩转换成十分制(假设满分为10)
"""
score = np.array([85, 90, 78, 92, 88])
print(score)
print(np.sort(score))
print('平均分:', np.mean(score))
print('中位数:', np.median(score))
print('标准差:%.3f' % np.std(score))
print(score / 10)

#%%
"""
题目3:矩阵运算
给定矩阵A=[[1,2],[3,4]]和B=[[5,6],[7,8]]
- 计算A+B和A*B(逐元素乘法)
_ 计算A和B的矩阵乘法(点积)
"""
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A + B)
print(A * B)
print(A @ B)
print(np.dot(A, B))
#%%
"""
题目4:随机数据生成
生成一个(3,4)的随机整数数组,范围[0,10]
- 计算每列的最大值和每行的最小值
- 将数组中的所有奇数替换为-1
"""
np.random.seed(0)
arr = np.random.randint(0, 10, (3, 4))
print(arr)
print('每列的最大值', np.max(arr, axis=0))  #axis=0表示列,=1表示行
print('每行的最小值', np.min(arr, axis=1))
print(np.where(arr % 2 == 1, -1, arr))
arr[arr % 2 == 1] = -1
print(arr)
#%%
"""
题目5:数组变形
创建一个1到12的一维数组,并转换为(3,4)的二维数组
- 计算每行的和与每列的平均值
- 将数组展平为一维数组
"""
arr = np.arange(1, 13)
print(arr)
print(np.reshape(arr, (3, 4)))
arr = np.reshape(arr, (3, 4))
print('每行的和', np.sum(arr, axis=1))
print('每列的平均值', np.mean(arr, axis=0))
print(arr)
print(np.reshape(arr, (12)))
#%%
"""
题目6:布尔索引
生成一个(5,5)的随机数组,范围[0,20]
- 找出数组中大于10的元素
- 将所有大于10的元素替换为0
"""
np.random.seed(0)
arr = np.random.randint(0, 20, (5, 5))
print(arr)
print(arr[arr > 10])
arr[arr > 10] = 0
print(arr)
#%%
"""
题目7:统计函数应用
某公司6个月的销售额(万元)为[120,135,110,125,130,140]
- 计算销售额的总和、均值和方差
- 找出销售额最高的月份和最低的月份
"""
money = np.array([120, 135, 110, 125, 130, 140])
print('总和', np.sum(money))
print('平均值', np.mean(money))
print('方差', np.var(money))
print('最高的月份', np.argmax(money) + 1)
print('最低的月份', np.argmin(money) + 1)

#%%
"""
题目8:数组拼接
给定A=[1,2,3]和B=[4,5,6]
- 将A和B水平拼接为一个新数组
- 将A和B垂直拼接为一个新数组
"""
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.concatenate((A, B))
print(C)
print(np.reshape(C, (2, 3)))
#%%
"""
题目9:唯一值与排序
给定数组[2,1,2,3,1,4,3]
- 找出数组中的唯一值并排序
- 计算每个唯一值出现的次数
"""
arr = np.array([2, 1, 2, 3, 1, 4, 3])
u_arr, counts = np.unique(arr, return_counts=True)
print(u_arr)
print(counts)
#%%
""""
题目20: 综合应用
某商店5天的销售额(万元)和成本(万元)如下:
销售额:[20,25,22,30,28]
成本:[15,18,16,22,20]
- 计算每天的利润(销售额-成本)
- 计算利润的平均值和标准差
- 找出利润最高的天数
"""
money = np.array([20, 25, 22, 30, 28])
a = np.array([15, 18, 16, 22, 20])
print('每天的利润: ', money - a)
b = money - a
print('利润的平均值', np.mean(b))
print('利润的标准差', np.std(b))
print('利润最高的天数', len(b[b == np.max(b)]))