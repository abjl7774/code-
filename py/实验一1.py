import random
def main():
    total_rounds = 0
    total_guesses = 0
    total_score = 0
    print("欢迎进入猜数字游戏！")
    while True:
        print("\n请选择难度：1.简单(1-50) 2.中等(1-100) 3.困难(1-500)")
        difficulty = input("请输入选择：")
        if difficulty == '1':
            max_num = 50
        elif difficulty == '2':
            max_num = 100
        elif difficulty == '3':
            max_num = 500
        else:
            print("输入错误，请选择1、2或3")
            continue
        target = random.randint(1, max_num)
        guess_count = 0
        print(f"\n游戏开始！我已想好一个1-{max_num}之间的数字，请你来猜。")
        while True:
            try:
                guess = int(input(f"第{guess_count + 1}次猜测："))
                if guess < 1 or guess > max_num:
                    print(f"请输入1-{max_num}之间的整数！") 
                    continue
                guess_count += 1
                if guess > target:
                    print(f"{guess} → 太大了！")
                elif guess < target:
                    print(f"{guess} → 太小了！")
                else:
                    score = max(0, 100 - (guess_count - 1) * 5)
                    print(f"{guess} → 恭喜！猜对了！")
                    print(f"本轮猜测{guess_count}次，获得积分{score}分")
                    total_rounds += 1
                    total_guesses += guess_count
                    total_score += score
                    break
            except ValueError:
                print("请输入有效的整数！")
        while True:
            continue_game = input("是否继续游戏？(y/n)：").lower()
            if continue_game in ['y', 'n']:
                break
            print("请输入y或n！")
        if continue_game == 'n':
            print("\n===== 游戏统计 =====")
            print(f"总游戏轮数：{total_rounds}")
            if total_rounds > 0:
                print(f"平均每轮猜测次数：{total_guesses / total_rounds:.1f}")
                print(f"总积分：{total_score}")
                print(f"平均每轮积分：{total_score / total_rounds:.1f}")
            print("感谢游玩！")
            break
if __name__ == "__main__":
    main()