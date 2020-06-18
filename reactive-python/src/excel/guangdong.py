# coding=utf-8
import numpy as np
import pandas as pd

excel_file_path = '../file/gd/infee_1.xlsx'
csv_file_1 = '../file/gd/infee_1.csv'
csv_file_2 = '../file/gd/infee_2.csv'
out_file = '../file/gd/outfile.csv'

df1 = pd.read_csv(csv_file_1, usecols=[2,3], encoding='utf-8', sep='\t', low_memory=False)
df2 = pd.read_csv(csv_file_2, usecols=[2,3], encoding='utf-8', sep='\t', low_memory=False)

df1.columns = ['地市','infee1']
df2.columns = ['地市','infee2']

# df1.columns = ['帐期','序号','地市','infee1']
# df2.columns = ['帐期','序号','地市','infee2']
# df1.drop('帐期',axis=1, inplace=True)
# df1.drop('序号',axis=1, inplace=True)
# df2.drop('帐期',axis=1, inplace=True)
# df2.drop('序号',axis=1, inplace=True)

print(df1)
print('>>>>>>>>>>>>')
print(df2)

out_data = pd.merge(df1, df2)
print('>>>>>>>>>>>>')
print(out_data)
out_data.to_csv(out_file, index=False, encoding='utf-8')

# excel_writer = pd.ExcelWriter(excel_file_path)
# csv_data.to_excel(excel_writer, 'sheet1', index=False)
# excel_writer.save()

print('写入文件{}完成'.format(excel_file_path))


