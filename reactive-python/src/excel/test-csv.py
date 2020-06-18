import csv
import numpy as np

birth_weight_file = "../file/ded.csv"
birth_data = []
with open(birth_weight_file, encoding= 'utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    birth_header = next(csv_reader)  # 读取第一行每一列的标题
    for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
        birth_data.append(row)


#birth_data = [[float(x) for x in row] for row in birth_data]  # 将数据从string形式转换为float形式


birth_data = np.array(birth_data)  # 将list数组转化成array数组便于查看数据结构
birth_header = np.array(birth_header)
print(birth_data.shape)  # 利用.shape查看结构。
print(birth_header.shape)

print(birth_header.data)