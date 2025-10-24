class Student:
    """
    学生类，用于表示学生对象
    包含类属性和实例属性，以及实例方法
    """
    # 定义类属性school，表示学校名称
    school = "华东交通大学"
    # 构造方法，初始化实例属性
    def __init__(self, name, age, student_id):
        # 给实例对象赋值属性
        self.name = name
        self.age = age
        self.student_id = student_id
    # 实例方法
    def study(self):
        print(f"{self.name}正在学习")
    # 实例方法：自我介绍
    def introduce(self):
        # 按照要求打印信息
        print(f"我是{self.name}，今年{self.age}岁，学号是{self.student_id}")
# 创建第一个学生对象
stu1 = Student("张三", 18, "2025001")
# 调用属性
print("学校：", Student.school)  # 打印类属性school
print("姓名：", stu1.name)      # 打印实例属性name
print("学号：", stu1.student_id) # 打印实例属性student_id
# 调用方法
stu1.study()  # 调用实例方法study
stu1.introduce()  # 调用实例方法introduce
print("-" * 30)  # 打印分隔线
# 创建第二个学生对象
stu2 = Student("阿卜杜加拉力", 22, "2025002")
# 调用属性
print("学校：", Student.school)  # 打印类属性school
print("姓名：", stu2.name)      # 打印实例属性name
print("年龄：", stu2.age)       # 打印实例属性age
print("学号：", stu2.student_id) # 打印实例属性student_id
# 调用方法
stu2.study()  # 调用实例方法study
stu2.introduce()  # 调用实例方法introduce