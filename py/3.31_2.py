import csv

# ========== 第 1 部分：读取数据 ==========
def read_data(filename):
  """读取CSV文件，返回学生列表"""
  students = []
  with open(filename, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
      # 补全代码：将字符串成绩转为整数
      student = {
        "学号": row["学号"],
        "姓名": row["姓名"],
        "语文": int(row["语文"]),
        "数学": int(row["数学"]),   # 补全1
        "英语": int(row["英语"])    # 补全2
      }
      students.append(student)
  return students
def calc_score(student):
  """计算总分、平均分、等级"""
  # 补全代码：计算总分
  total = student["语文"] + ["数学"] + ["英语"]  # 补全3,4
  # 补全代码：计算平均分（保留2位小数）
  avg = round(total / 3, 2)           # 补全5
  # 补全代码：判断等级
  if avg >= 90:
    level = "A"
  elif avg >= 80:                   # 补全6
    level = "B"
  elif avg >= 70:
    level = "C"
  else:
    level = "D"                # 补全7
  student["总分"] = total
  student["平均分"] = avg
  student["等级"] = level
  return student

# ========== 第 3 部分：写入数据 ==========
def save_data(students, filename):
  """将结果保存到CSV"""
  # 补全代码：定义表头
  header = ["学号", "姓名", "语文", "数学", "英语", 
       "总分", "平均分", "等级"]    # 补全8,9,10
   
  with open(filename, "w", encoding="utf-8-sig", newline="") as f: # 补全11
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    # 补全代码：写入所有数据
    writer.writerows(students)
      # ========== 主程序 ==========
if __name__ == "__main__":
  # 1. 先创建 scores.csv 文件（把你给的数据写进去）
  raw_data = """学号,姓名,语文,数学,英语
2024001,张崔,85,92,78
2024002,李思怡,76,88,91
2024003,王德生,92,85,88
2024004,赵乐,65,72,69"""
  
  with open("scores.csv", "w", encoding="utf-8-sig", newline="") as f:
      f.write(raw_data)
  
  # 2. 读取数据
  data = read_data("scores.csv")
  
  # 3. 计算
  for s in data:
    calc_score(s)
  
  # 4. 保存
  save_data(data, "scores_result.csv")
  print("处理完成！已生成 scores_result.csv")