abjl = 3
users = {}
current_user = None
def register():
    print("\n【用户注册】")
    while True:
        username = input("请输入用户名：").strip()
        if not username:
            print("用户名不能为空！")
            continue
        if username in users:
            print("用户名已存在！")
            continue
        break
    while True:
        password = input("请输入密码（6-16位）：").strip()
        if len(password) < 6 or len(password) > 16:
            print("密码长度需6-16位！")
            continue
        confirm_pwd = input("确认密码：").strip()
        if password != confirm_pwd:
            print("两次密码不一致！")
            continue
        break
    users[username] = password
    print("注册成功！")
def login():
    print("\n【用户登录】")
    username = input("请输入用户名：").strip()
    if username not in users:
        print("用户名不存在！")
        return None
    for i in range(abjl):
        remaining = abjl - (i + 1)
        password = input("请输入密码：").strip()
        
        if password == users[username]:
            print(f"登录成功！欢迎回来，{username}！")
            return username
        else:
            if remaining > 0:
                print(f"密码错误！您还剩 {remaining} 次尝试机会")
            else:
                print("\n您已连续3次输入错误，登录失败！")
    return None
def modify_pwd():
    print("\n【修改密码】")
    old_pwd = input("请输入原密码：").strip()
    if old_pwd != users[current_user]:
        print("原密码错误！")
        return
    while True:
        new_pwd = input("新密码（6-16位）：").strip()
        if len(new_pwd) < 6 or len(new_pwd) > 16:
            print("密码长度需6-16位！")
            continue
        if new_pwd == old_pwd:
            print("新密码不能和原密码相同！")
            continue
        confirm_pwd = input("确认新密码：").strip()
        if new_pwd != confirm_pwd:
            print("两次密码不一致！")
            continue
        break
    users[current_user] = new_pwd
    print("密码修改成功！")
print("欢迎使用用户登录系统！")
while True:
    if not current_user:
        print("\n请选择操作：1.登录 2.注册 3.退出")
        choice = input("输入选择：").strip()
        
        if choice == "1":
            current_user = login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("再见！")
            break
        else:
            print("请输入1/2/3！")
    else:
        print(f"\n[{current_user}] 1.查询信息 2.修改密码 3.退出登录")
        sub_choice = input("输入选择：").strip()
        if sub_choice == "1":
            print(f"\n用户名：{current_user}")
        elif sub_choice == "2":
            modify_pwd()
        elif sub_choice == "3":
            print(f"已退出登录，{current_user}！")
            current_user = None
        else:
            print("请输入1/2/3！")