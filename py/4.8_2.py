# 基类：人类
class Person:
    def __init__(self, name, age):
        """
        人类构造函数
        :param name: 姓名
        :param age: 年龄
        """
        self.name = name
        self.age = age
    # 自我介绍方法
    def introduce(self):
        """
        人类自我介绍方法
        打印姓名和年龄信息
        """
        print(f"我是{self.name}，今年{self.age}岁")
# 子类：学生类，继承 Person
class Student(Person):
    """
    学生类，继承自Person类
    新增学号属性，重写自我介绍方法
    """
    # 新增学号属性 stu_id
    def __init__(self, name, age, stu_id):
        # 调用父类构造方法
        super().__init__(name, age)
        # 子类自己的属性
        self.stu_id = stu_id
    # 重写自我介绍
    def introduce(self):
        print(f"我是{self.name}，今年{self.age}岁，学号是{self.stu_id}")
    # 学习方法
    def study(self):
        print(f"{self.name}正在学习")
# 测试
if __name__ == '__main__':
    stu1 = Student("小明", 16, "2025001")
    stu1.introduce()
    stu1.study()
    stu2 = Student("小红", 17, "2025002")
    stu2.introduce()
    stu2.study()