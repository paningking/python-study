import pandas as pd
import time
import os

excel_file_path = 'D:/Document/咪咕/统一结算/工单取数/201906/tmp_ded_list_20190624.tar/tmp_ded_list_20190624/ded_list_11.xlsx'
csv_file_path = 'D:/Document/咪咕/统一结算/工单取数/201906/tmp_ded_list_20190624.tar/tmp_ded_list_20190624/ded_list_11.csv'

# csvrootdir = 'D:\data'
# list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
# for i in range(0,len(list)):
#        path = os.path.join(rootdir,list[i])
#        if os.path.isfile(path):

csv_data = pd.read_csv(csv_file_path, sep='\t', low_memory=False)
# print("条数", len(csv_data))
print(csv_data.shape)
start = time.time()

excel_writer = pd.ExcelWriter(excel_file_path)
csv_data.columns = ['帐期','号码','业务名称','省份','订购时间','退订时间','核减时间','核减原因']
csv_data.to_excel(excel_writer, 'sheet1', index=False)
excel_writer.save()

print('写入文件{}完成'.format(excel_file_path))
end = time.time()
print(end - start)