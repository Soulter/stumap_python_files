import numpy as np
def search(dataset,k):
    k = input("输入要查找的数:")
    dataset = np.random.rand(10) #生成随机数
    return dataset.index(k) #查找某个元素在列表中每次出现的位置（返回列表）
