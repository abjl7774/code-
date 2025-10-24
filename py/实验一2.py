# 导入随机数模块和turtle图形绘制模块
import random
import turtle

# 打印欢迎信息
print("欢迎使用'华交好人'投票系统！")

# 循环获取候选人数量，确保数量在2-8之间
while True:
    n = int(input("请输入候选人数量："))  # 输入候选人数量
    if 2 <= n <= 8:  # 检查数量是否在有效范围内
        break
    print("数量必须在2-8之间，请重新输入！")  # 提示重新输入
# 初始化候选人姓名列表和票数列表
names = []
votes = []
# 循环输入每位候选人的姓名，并初始化票数为0
for i in range(n):
    name = input(f"请输入第{i+1}位候选人姓名：")  # 输入候选人姓名
    names.append(name)  # 将姓名添加到列表
    votes.append(0)  # 初始化票数为0
# 打印开始投票信息
print("\n========== 开始投票 ==========\n当前候选人：")
# 投票循环
while True:
    # 打印所有候选人及其当前票数
    for i in range(n):
        print(f"{i+1}.{names[i]}：（当前票数{votes[i]}）")
    print("0. 结束投票\n")
    
    # 获取用户输入的投票选择
    choice = input("请输入候选人编号进行投票（0结束）：")
    if not choice.isdigit():  # 检查输入是否为数字
        print("输入无效！请输入数字\n")
        continue
    
    num = int(choice)  # 将输入转换为整数
    if num == 0:  # 如果输入0，结束投票
        break
    if 1 <= num <= n:  # 检查输入是否在有效范围内
        idx = num - 1  # 计算候选人索引
        votes[idx] += 1  # 增加对应候选人的票数
        print(f"已为【{names[idx]}】投票！当前票数：{votes[idx]}\n")  # 显示投票成功信息
    else:
        print("无效编号！请输入0-%d之间的数字\n" % n)  # 提示输入无效

# 计算总票数
total = sum(votes)
# 打印投票结果
print("\n========== 投票结果 ==========")
# 打印每位候选人的票数和得票率
for i in range(n):
    pct = votes[i]/total*100 if total != 0 else 0  # 计算得票率
    print(f"{names[i]}：{votes[i]}票  得票率：{pct:.1f}%")

# 定义柱状图颜色列表
colors = ["red","blue","green","orange","purple","gold","pink","cyan"]
# 设置turtle图形窗口标题
turtle.title("华交好人投票结果统计图")
# 创建turtle屏幕
screen = turtle.Screen()
# 设置屏幕大小
screen.setup(1000,600)
# 创建turtle对象
t = turtle.Turtle()
# 设置绘制速度为最快
t.speed(0)
# 抬起画笔
t.penup()
# 移动到起始位置
t.goto(-350, -200)
# 放下画笔
t.pendown()
# 隐藏turtle箭头
t.hideturtle()

# 在顶部绘制标题
t.penup()
t.goto(0, 250)
t.write(f"华交好人投票结果  总票数：{total}", align="center", font=("Arial",20,"bold"))
# 移动到柱状图起始位置
t.goto(-400, -200)
t.pendown()

# 绘制柱状图
for i in range(n):
    c = colors[i]  # 获取当前柱子的颜色
    h = votes[i] * 30  # 计算柱子高度
    t.fillcolor(c)  # 设置填充颜色
    t.begin_fill()  # 开始填充

    # 绘制柱子
    t.left(90)  # 向左转90度
    t.forward(h)  # 向前绘制柱子高度
    t.penup()  # 抬起画笔
    t.forward(20)  # 向前移动一小段距离
    # 在柱子上方显示候选人姓名和票数
    t.write(f"{names[i]}\n{votes[i]}票", align="center", font=("Arial",12,"bold"))
    t.forward(-20)  # 向后移动一小段距离
    t.pendown()  # 放下画笔
    t.right(90)  # 向右转90度
    t.forward(60)  # 向前移动一小段距离
    t.right(90)  # 向右转90度
    t.forward(h)  # 向前绘制柱子高度
    t.left(90)  # 向左转90度
    t.end_fill()  # 结束填充
    t.forward(30)  # 向前移动一小段距离

# 完成绘制
turtle.done()