def read_file():
    try:
        # 获取用户输入的文件名
        filename = input("请输入要读取的文件名：")
    # 尝试打开并读取文件
        with open(filename, 'r', encoding='utf-8') as f:

            content = f.read()
        print(" 文件读取成功！")
        print("文件内容：")
        print(content)
    # 异常1：文件不存在
    except FileNotFoundError:
        print("文件不存在，请检查文件名是否正确！")
    # 异常2：没有权限读取（如系统文件、只读权限）
    except PermissionError:

        print("权限不足，无法读取该文件！")
    # 异常3：其他所有文件异常
    except IOError:
        print("文件读写错误！")
    # 无论是否出错，一定会执行
    finally:
        print("文件操作程序结束")
if __name__ == "__main__":
      
    # 测试1：调用函数
    read_file()

    