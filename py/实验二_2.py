import re  # 导入正则表达式模块，用于字符串匹配
import os  # 导入操作系统模块，用于文件操作
# 数据存储文件常量
DATA_FILE = "students.txt"
def init_file():
    """初始化数据文件，若文件不存在则创建"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            pass
def check_student_id_exists(student_id):
    """检查学号是否已存在"""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip().split(",")
            if data and data[0] == student_id:
                return True
    return False
def validate_password(password):
    """验证密码强度：至少6位，包含字母和数字"""
    if len(password) < 6:
        return False
    # 正则匹配：包含字母和数字
    if not re.search(r'[a-zA-Z]', password) or not re.search(r'[0-9]', password):
        return False
    return True
def validate_phone(phone):
    """验证手机号格式（11位数字）"""
    return re.match(r'^1[3-9]\d{9}$', phone) is not None
def validate_email(email):
    """验证邮箱格式"""
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None
def register():
    """用户注册功能"""
    print("---------- 用户注册 ----------")
    # 输入学号并验证唯一性
    while True:
        student_id = input("请输入学号: ").strip()
        if not student_id:
            print("学号不能为空！")
            continue
        if check_student_id_exists(student_id):
            print("该学号已注册，请重新输入！")
        else:
            break
    # 输入姓名
    while True:
        name = input("请输入姓名: ").strip()
        if name:
            break
        print("姓名不能为空！")
    # 输入密码并验证强度
    while True:
        password = input("请输入密码: ").strip()
        if validate_password(password):
            break
        print("密码强度不足！至少6位，必须包含字母和数字！")
    # 确认密码
    while True:
        confirm_pwd = input("请确认密码: ").strip()
        if confirm_pwd == password:
            break
        print("两次密码不一致，请重新输入！")
    # 输入手机号并验证格式
    while True:
        phone = input("请输入手机号: ").strip()
        if validate_phone(phone):
            break
        print("手机号格式错误，请输入11位有效手机号！")
    # 输入邮箱并验证格式
    while True:
        email = input("请输入邮箱: ").strip()
        if validate_email(email):
            break
        print("邮箱格式错误，请重新输入！")
    # 写入文件
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{student_id},{name},{password},{phone},{email}\n")
    print("注册成功！")
def login():
    """用户登录功能，最多尝试3次"""
    print("---------- 用户登录 ----------")
    count = 3
    while count > 0:
        student_id = input("请输入学号: ").strip()
        password = input("请输入密码: ").strip()
        # 校验账号密码
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(",")
                if data and data[0] == student_id and data[2] == password:
                    print("登录成功！")
                    return data  # 返回登录用户的信息
        count -= 1
        print(f"学号或密码错误！剩余尝试次数：{count}")
    print("登录失败3次，程序退出！")
    exit()
def show_info(user):
    """查看个人信息"""
    print("\n---------- 个人信息 ----------")
    print(f"学号: {user[0]}")
    print(f"姓名: {user[1]}")
    print(f"密码: ******")  # 密码隐藏显示
    print(f"手机号: {user[3]}")
    print(f"邮箱: {user[4]}")
def change_password(user):
    """修改密码功能"""
    print("\n---------- 修改密码 ----------")
    # 验证原密码
    while True:
        old_pwd = input("请输入原密码: ").strip()
        if old_pwd == user[2]:
            break
        print("原密码错误，请重新输入！")
    # 输入新密码并验证强度
    while True:
        new_pwd = input("请输入新密码: ").strip()
        if validate_password(new_pwd):
            break
        print("密码强度不足！至少6位，必须包含字母和数字！")
    # 确认新密码
    while True:
        confirm_pwd = input("请确认新密码: ").strip()
        if confirm_pwd == new_pwd:
            break
        print("两次密码不一致，请重新输入！")
    # 读取所有数据，修改密码后重新写入
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for line in lines:
            data = line.strip().split(",")
            if data and data[0] == user[0]:
                # 更新密码
                f.write(f"{data[0]},{data[1]},{new_pwd},{data[3]},{data[4]}\n")
            else:
                f.write(line)
    print("密码修改成功！")
    # 更新当前用户信息
    user[2] = new_pwd
def user_center(user):
    """个人中心菜单"""
    while True:
        print("\n---------- 个人中心 ----------")
        print("1. 查看个人信息")
        print("2. 修改密码")
        print("3. 返回主菜单")
        choice = input("请选择功能(1-3): ").strip()
        if choice == "1":
            show_info(user)
        elif choice == "2":
            change_password(user)
        elif choice == "3":
            print("已返回主菜单。")
            break
        else:
            print("输入无效，请选择1-3！")
def main():
    """主函数，程序入口"""
    init_file()
    while True:
        print("\n========== 学生个人信息管理系统 ==========")
        print("1. 用户注册")
        print("2. 用户登录")
        print("3. 退出系统")
        choice = input("请选择功能(1-3): ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            user_info = login()
            user_center(user_info)
        elif choice == "3":
            print("感谢使用，再见！")
            break
        else:
            print("输入无效，请选择1-3！")         
        # 继续操作判断
        while True:
            flag = input("\n是否继续操作？(y/n): ").strip().lower()
            if flag in ["y", "n"]:
                break
            print("输入无效，请输入y或n！")
        if flag == "n":
            print("感谢使用，再见！")
            break
# 启动程序
if __name__ == "__main__":
    main()
