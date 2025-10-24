"""
学生成绩统计系统
功能：文件读写、增删改查、统计分析、排序输出
文件格式：scores.csv
"""

# 读取CSV文件中的学生成绩数据
def read_data():
    """
    从scores.csv文件读取学生成绩数据
    返回：列表，每个元素是字典，存储单个学生信息
    """
    # 初始化空列表用于存放所有学生数据
    data = []
    try:
        # 打开CSV文件，读取所有内容
        with open("scores.csv", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # 从第二行开始读取数据（跳过表头）
            for line in lines[1:]:
                line = line.strip()
                # 跳过空行
                if not line:
                    continue
                # 按逗号分割每一行数据
                stu_id, name, chinese, math, english = line.split(",")
                # 构造学生字典
                student = {
                    "学号": stu_id,
                    "姓名": name,
                    "语文": int(chinese),
                    "数学": int(math),
                    "英语": int(english)
                }
                data.append(student)
    # 文件不存在时，创建一个带表头的空文件
    except FileNotFoundError:
        with open("scores.csv", "w", encoding="utf-8") as f:
            f.write("学号,姓名,语文,数学,英语\n")
    return data

# 将内存中的数据保存回CSV文件
def save_data(data):
    """
    将数据保存回scores.csv文件
    """
    # 写入表头和所有学生数据
    with open("scores.csv", "w", encoding="utf-8") as f:
        f.write("学号,姓名,语文,数学,英语\n")
        for stu in data:
            f.write(f"{stu['学号']},{stu['姓名']},{stu['语文']},{stu['数学']},{stu['英语']}\n")
    print("数据保存成功！")

# 以表格形式显示所有学生成绩
def show_all(data):
    """格式化显示所有学生成绩（表格形式）"""
    # 判断是否有数据
    if not data:
        print("暂无学生成绩数据！")
        return

    # 打印表格表头
    print("=" * 60)
    print(f"{'学号':<10}{'姓名':<6}{'语文':<6}{'数学':<6}{'英语':<6}{'总分':<6}{'平均分':<8}")
    print("=" * 60)
    # 遍历输出每个学生信息并计算总分、平均分
    for stu in data:
        total = stu["语文"] + stu["数学"] + stu["英语"]
        avg = total / 3
        print(f"{stu['学号']:<10}{stu['姓名']:<6}{stu['语文']:<6}{stu['数学']:<6}{stu['英语']:<6}{total:<6}{avg:.2f}")
    print("=" * 60)

# 添加新学生成绩
def add_student(data):
    """添加学生成绩（自动检查学号重复）"""
    stu_id = input("请输入学生学号：")
    # 检查学号是否重复
    for stu in data:
        if stu["学号"] == stu_id:
            print("该学号已存在，添加失败！")
            return

    # 输入姓名和各科成绩
    name = input("请输入学生姓名：")
    try:
        chinese = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩："))
        english = int(input("请输入英语成绩："))
    # 处理成绩输入非数字的异常
    except ValueError:
        print("成绩必须输入数字，添加失败！")
        return

    # 构造新学生信息并加入列表
    new_stu = {
        "学号": stu_id,
        "姓名": name,
        "语文": chinese,
        "数学": math,
        "英语": english
    }
    data.append(new_stu)
    print("学生成绩添加成功！")

# 根据学号删除学生
def delete_student(data):
    """根据学号删除学生成绩"""
    stu_id = input("请输入要删除的学生学号：")
    # 查找对应学号并删除
    for i, stu in enumerate(data):
        if stu["学号"] == stu_id:
            del data[i]
            print("学生成绩删除成功！")
            return
    print("未找到该学号的学生！")

# 修改指定学号学生的成绩
def modify_score(data):
    """修改指定学生的成绩"""
    stu_id = input("请输入要修改的学生学号：")
    # 查找学生
    for stu in data:
        if stu["学号"] == stu_id:
            print(f"当前信息：{stu['姓名']} 语文：{stu['语文']} 数学：{stu['数学']} 英语：{stu['英语']}")
            try:
                # 重新输入成绩
                stu["语文"] = int(input("请输入新的语文成绩："))
                stu["数学"] = int(input("请输入新的数学成绩："))
                stu["英语"] = int(input("请输入新的英语成绩："))
                print("成绩修改成功！")
            except ValueError:
                print("成绩必须输入数字，修改失败！")
            return
    print("未找到该学号的学生！")

# 按学号或姓名查询学生
def query_student(data):
    """按学号/姓名查询个人成绩"""
    if not data:
        print("暂无学生成绩数据！")
        return

    keyword = input("请输入要查询的学号或姓名：")
    find_list = []
    # 匹配学号或姓名
    for stu in data:
        if keyword == stu["学号"] or keyword in stu["姓名"]:
            find_list.append(stu)

    # 显示查询结果
    if find_list:
        print("=" * 50)
        print(f"{'学号':<10}{'姓名':<6}{'语文':<6}{'数学':<6}{'英语':<6}{'总分':<6}{'平均分':<8}")
        for stu in find_list:
            total = stu["语文"] + stu["数学"] + stu["英语"]
            avg = total / 3
            print(f"{stu['学号']:<10}{stu['姓名']:<6}{stu['语文']:<6}{stu['数学']:<6}{stu['英语']:<6}{total:<6}{avg:.2f}")
        print("=" * 50)
    else:
        print("未查询到相关学生信息！")

# 成绩统计分析
def statistics(data):
    """成绩统计分析"""
    if not data:
        print("暂无学生成绩数据！")
        return

    total_num = len(data)
    # 提取各科成绩
    chinese_scores = [stu["语文"] for stu in data]
    math_scores = [stu["数学"] for stu in data]
    english_scores = [stu["英语"] for stu in data]

    # 语文统计
    c_avg = sum(chinese_scores) / total_num
    c_max = max(chinese_scores)
    c_min = min(chinese_scores)
    c_pass = len([s for s in chinese_scores if s >= 60]) / total_num * 100

    # 数学统计
    m_avg = sum(math_scores) / total_num
    m_max = max(math_scores)
    m_min = min(math_scores)
    m_pass = len([s for s in math_scores if s >= 60]) / total_num * 100

    # 英语统计
    e_avg = sum(english_scores) / total_num
    e_max = max(english_scores)
    e_min = min(english_scores)
    e_pass = len([s for s in english_scores if s >= 60]) / total_num * 100

    # 计算总分并排名
    stu_total = []
    for stu in data:
        total = stu["语文"] + stu["数学"] + stu["英语"]
        avg = total / 3
        stu_total.append({"姓名": stu["姓名"], "总分": total, "平均分": avg})
    # 按总分降序排列
    stu_total.sort(key=lambda x: x["总分"], reverse=True)

    # 输出统计结果
    print("===== 成绩统计 =====")
    print(f"总人数：{total_num}人")
    print(f"语文平均分：{c_avg:.2f}，最高分：{c_max}，最低分：{c_min}，及格率：{c_pass:.2f}%")
    print(f"数学平均分：{m_avg:.2f}，最高分：{m_max}，最低分：{m_min}，及格率：{m_pass:.2f}%")
    print(f"英语平均分：{e_avg:.2f}，最高分：{e_max}，最低分：{e_min}，及格率：{e_pass:.2f}%")
    print("\n总分排名：")
    for i, stu in enumerate(stu_total, 1):
        print(f"{i}. {stu['姓名']}  总分:{stu['总分']}  平均:{stu['平均分']:.2f}")

# 成绩排序功能
def sort_scores(data):
    """成绩排序"""
    if not data:
        print("暂无学生成绩数据！")
        return

    # 显示排序菜单
    print("===== 排序选项 =====")
    print("1. 按总分降序")
    print("2. 按语文成绩降序")
    print("3. 按数学成绩降序")
    print("4. 按英语成绩降序")
    print("5. 按平均分降序")

    choice = input("请选择排序方式(1-5)：")
    temp_data = data.copy()

    # 根据选择进行排序
    if choice == "1":
        temp_data.sort(key=lambda x: x["语文"] + x["数学"] + x["英语"], reverse=True)
    elif choice == "2":
        temp_data.sort(key=lambda x: x["语文"], reverse=True)
    elif choice == "3":
        temp_data.sort(key=lambda x: x["数学"], reverse=True)
    elif choice == "4":
        temp_data.sort(key=lambda x: x["英语"], reverse=True)
    elif choice == "5":
        temp_data.sort(key=lambda x: (x["语文"] + x["数学"] + x["英语"]) / 3, reverse=True)
    else:
        print("输入错误！")
        return

    # 显示排序后结果
    print("===== 排序结果 =====")
    show_all(temp_data)

# 主函数，程序入口
def main():
    """主函数"""
    # 读取文件数据
    data = read_data()
    while True:
        # 打印系统菜单
        print("\n===== 学生成绩统计系统 =====")
        print("1. 显示所有成绩")
        print("2. 添加学生成绩")
        print("3. 删除学生成绩")
        print("4. 修改学生成绩")
        print("5. 查询个人成绩")
        print("6. 成绩统计分析")
        print("7. 成绩排序")
        print("8. 保存并退出")
        print("============================")

        choice = input("请选择功能(1-8)：")

        # 根据用户选择调用对应函数
        if choice == "1":
            show_all(data)
        elif choice == "2":
            add_student(data)
        elif choice == "3":
            delete_student(data)
        elif choice == "4":
            modify_score(data)
        elif choice == "5":
            query_student(data)
        elif choice == "6":
            statistics(data)
        elif choice == "7":
            sort_scores(data)
        elif choice == "8":
            save_data(data)
            print("感谢使用，再见！")
            break
        else:
            print("请输入1-8之间的数字！")

# 运行主程序
if __name__ == "__main__":
    main()