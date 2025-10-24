import json

# ========== 第 1 部分：读取 JSON ==========
def read_json(filename):
  """读取JSON文件，返回Python对象"""
  with open(filename, "r", encoding="utf-8") as f:
    data = json.load(f)    # 补全1：读取方法
  return data

# ========== 第 2 部分：修改数据 ==========
def update_data(data):
  """修改学生信息"""
  # 补全代码：添加一门新课程 "Vue"
  data["courses"].append("Vue")   # 补全2：列表添加方法

  # 补全代码：年龄增加1岁
  data["age"] = data["age"] + 1 # 补全3

  # 补全代码：计算平均分，添加到数据中
  avg_score = sum(data["scores"]) / len(data["scores"]) # 补全4：计算元素个数
  data["avg_score"] = round(avg_score, 2)   # 补全5：新增字段名 

  # 补全代码：修改地址中的城市为 "上海"
  data["address"]["city"] = "上海"     # 补全6,7：嵌套字典访问  

  # 补全代码：将 is_student 改为 True
  data["is_student"] = True        # 补全8,9

  return data

# ========== 第 3 部分：写入 JSON ==========
def save_json(data, filename):
  """将数据保存到JSON文件"""
  with open(filename, "w", encoding="utf-8") as f:
    json.dump(          # 补全10：写入方法
      data, 
      f, 
      ensure_ascii=False,    # 补全11：中文显示参数
      indent=4        # 补全12：缩进空格数
    )

# ========== 主程序 ==========
if __name__ == "__main__":
  # 读取
  student = read_json("student.json")
  print(f"原始数据: {student}")

  # 修改
  updated = update_data(student)

  # 保存
  save_json(updated, "student_updated.json")
  print("处理完成！")   