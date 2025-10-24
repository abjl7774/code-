# 导入所需的库
import random  # 用于生成随机选择
import turtle  # 用于绘制图形界面

# 获取玩家昵称
name = input("欢迎来到石头剪刀布游戏！\n请输入您的昵称：")


# 初始化游戏统计变量
win = 0    # 玩家胜利次数
lose = 0   # 玩家失败次数
tie = 0    # 平局次数

# 游戏开始提示
print("\n========== 游戏开始 ==========")
# 游戏主循环
while True:
    # 显示当前比分
    print(f"\n当前比分：{name} {win} : {lose} 电脑")
    # 显示游戏选项
    print("请选择：1.石头 2.剪刀 3.布 0.退出游戏")
    # 获取玩家选择
    choice = int(input("请输入选择（0-3）："))
    
    # 如果选择退出游戏，则跳出循环
    if choice == 0:
        break
    # 检查选择是否有效
    if choice not in [1,2,3]:
        print("输入无效，请重新输入！")
        continue
    # 定义游戏选项列表
    hands = ["石头","剪刀","布"]
    # 获取玩家选择
    player = hands[choice-1]
    # 电脑随机选择
    computer = random.choice(hands)
    
    # 显示双方选择
    print(f"你出了：{player}")
    print(f"电脑出了：{computer}")
    
    # 判断游戏结果
    if player == computer:
        print("结果：平局！")
        tie +=1  # 平局次数加1
    elif (player=="石头" and computer=="剪刀") or (player=="剪刀" and computer=="布") or (player=="布" and computer=="石头"):
        print("结果：你赢了！")
        win +=1  # 胜利次数加1
    else:
        print("结果：你输了！")
        lose +=1  # 失败次数加1

# 计算总局数
total = win + lose + tie
# 游戏结束，显示最终结果
print("\n游戏结束！")
print(f"最终比分：{name} {win} : {lose} 电脑")

# 判断最终胜负
if win > lose:
    print(f"{name} 获胜！")
elif win < lose:
    print("电脑获胜！")
else:
    print("平局！")
# 使用turtle绘制对战结果统计图
turtle.title("对战结果统计图")  # 设置窗口标题
turtle.setup(800,600)  # 设置窗口大小
pen = turtle.Turtle()  # 创建画笔对象
pen.speed(0)  # 设置最快速度
pen.pensize(2)  # 设置画笔粗细

# 绘制胜利次数柱状图
pen.penup()
pen.goto(-300,150)
pen.pendown()
pen.color("green")  # 设置绿色
pen.begin_fill()  # 开始填充
pen.forward(150)  # 绘制矩形
pen.right(90)
pen.forward(win*50)  # 高度根据胜利次数调整
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(win*50)
pen.end_fill()  # 结束填充

# 绘制失败次数柱状图
pen.penup()
pen.goto(-100,150)
pen.pendown()
pen.color("red")  # 设置红色
pen.begin_fill()
pen.forward(150)
pen.right(90)
pen.forward(lose*50)  # 高度根据失败次数调整
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(lose*50)
pen.end_fill()

# 绘制平局次数柱状图
pen.penup()
pen.goto(100,150)
pen.pendown()
pen.color("gold")  # 设置金色
pen.begin_fill()
pen.forward(150)
pen.right(90)
pen.forward(tie*50)  # 高度根据平局次数调整
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(tie*50)
pen.end_fill()

# 添加文字标签
pen.penup()
pen.goto(-225,-50)
pen.color("black")
pen.write(f"胜利({win})",align="center",font=("Arial",16,"bold"))
pen.goto(-25,-50)
pen.write(f"失败({lose})",align="center",font=("Arial",16,"bold"))
pen.goto(175,-50)
pen.write(f"平局({tie})",align="center",font=("Arial",16,"bold"))

# 添加标题和总局数
pen.goto(0,220)
pen.write(f"{name} 石头剪刀布对战统计  总局数：{total}",align="center",font=("Arial",20,"bold"))
# 隐藏画笔并完成绘制
pen.hideturtle()
turtle.done()