import csv # 导入模块
import csv # 导入模块

header = ["姓名","年龄","城市"]

data = [["张三", 20,"北京"], ["李四", 25,"上海"],["阿卜杜加拉力",22,"新和县"],["冯旭",22,"江西"]]

with open("test.csv","w", encoding="utf-8-sig", newline="") as f:

    writer = csv.writer(f)

    writer.writerow(header)# 写表头

    writer.writerows(data)# 写数据


    # 读test.csv文件并打印输出
import csv

with open("test.csv","r",encoding='utf-8') as f:

    reader = csv.reader(f)

    header = next(reader) # 读取表头

    for row in reader: # 遍历数据行

        print(row) 

