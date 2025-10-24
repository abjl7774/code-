#姓名：阿卜杜加拉力·玉素甫、学号：2024061014000233、日期：2026-04-03
import json  # 导入json模块，用于处理JSON数据
import csv   # 导入csv模块，用于处理CSV文件
def create_data():
    """创建列车数据，返回列表"""
    #
    train1 = {
        "车次": "G1234",
        "车型": "CRH380A",
        "站点数": 3,
        "站点列表": [
            {"站名": "北京南", "到达": "-", "发车": "08:00"},
            {"站名": "济南西", "到达": "09:30", "发车": "09:33"},
            {"站名": "上海虹桥", "到达": "11:30", "发车": "-"}
        ]  # 列表的结束括号，用于闭合前文定义的列表
    }  # 字典的结束花括号，用于闭合前文定义的字典
    # 第二趟车G5678(已补全)
    train2 = {
        "车次": "G5678",
        "车型": "CRH380B",
        "站点数": 3,
        "站点列表":[
        {   "站名": "北京南", "到达": "-", "发车": "09:00"},
        {    "站名": "天津南", "到达": "9:30", "发车": "9:33"},
        {    "站名": "青岛北", "到达": "12:00", "发车": "-"}
        ]
    }    
    return [train1, train2]
#============== 任务2：保存到JSON =======
def save_json(data, filename):
    """
    保存数据到JSON文件
    参数：data - 要保存的数据，filename - 文件名
    """
    with open(filename, 'w', encoding='utf-8-sig') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✓ 已保存到 {filename}")
def load_json(filename):
    """
    从JSON文件读取数据
    返回：读取到的数据
    """
    with open(filename, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    print(f"✓ 已从 {filename} 读取")
    return data
#已补全
# ============ 任务3：保存/读取 CSV ==========
def save_csv(data, filename):
    """
    保存统计信息到CSV文件
    参数：data - 列车列表，filename - 文件名
    """        
    # 表头：车次, 车型, 站点数, 始发站, 终到站
    headers = ["车次", "车型", "站点数", "始发站", "终到站"]
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)  # 写入表头
        # 遍历每趟列车，写入数据
        for train in data:
            train_id = train["车次"]
            model = train["车型"]
            count = train["站点数"]
            start = train["站点列表"][0]["站名"]   # 始发站
            end = train["站点列表"][-1]["站名"]    # 终点站
            writer.writerow([train_id, model, count, start, end])
    print(f"✓ 已保存到 {filename}")
def load_csv(filename):
    """
    从CSV文件读取数据
    返回：读取到的数据列表
    """
    data_list = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data_list.append(row)
    return data_list
#已补全
#=========== 任务4：查询功能 ===========
def find_train(data, train_number):
    """
    根据车次号查找列车
    参数：data - 列车列表，train_number - 车次号
    返回：找到的列车信息，找不到返回None
    """
    for train in data:
        if train["车次"] == train_number:
            return train
    return None
#1. 添加列车（查重）
def add_train(data, new_train, json_file, csv_file):
    if find_train(data, new_train["车次"]):
        print(f"✕ 车次 {new_train['车次']} 已存在，不可重复添加！")
        return False
    data.append(new_train)
    save_json(data, json_file)
    save_csv(data, csv_file)
    print(f"✓ 车次 {new_train['车次']} 已添加！")
    return True
# 2. 删除列车
def delete_train(data, train_number, json_file, csv_file):
    train = find_train(data, train_number)
    if not train:
        print(f"✕ 车次 {train_number} 不存在，无法删除！")
        return False
    data.remove(train)
    save_json(data, json_file)
    save_csv(data, csv_file)
    print(f"✓ 车次 {train_number} 已删除！")
    return True
#打印列车详细信息
def print_train_info(train):
    """打印列车详细信息"""
    print(f"\n车次:{train['车次']} 车型：{train['车型']}")
    print("时刻表：")
    for i, station in enumerate(train["站点列表"],1):
        print(f"{i}. {station['站名']:<6} 到:{station['到达']:<6} 发:{station['发车']}")
# 已补全
# ============ 主程序 ===========
def main():
    print("="*50)
    print("列车时刻表查询系统")
    print("="*50)
    # 1. 创建数据
    print("\n【1】创建数据...")
    trains = create_data()
    print(f"共 {len(trains)} 趟列车")
    # 2. 保存到JSON（完整数据）
    print("\n【2】保存到JSON文件...")
    save_json(trains, 'trains.json')
    # 3. 保存到CSV（统计信息）
    print("\n【3】保存到CSV文件...")
    save_csv(trains, 'trains.csv')
    # 4. 从JSON读取并查询
    print("\n【4】从JSON读取 - 查询详情...")
    json_data = load_json('trains.json')
    t = find_train(json_data, 'G1234')
    if t:
        print_train_info(t)
   # 5. 从CSV读取并统计 
    print("\n【5】从CSV读取 - 简单统计...")
    csv_data = load_csv('trains.csv')
    print(f"CSV中共有 {len(csv_data)} 趟列车：")
    for row in csv_data:
        print(f"  {row['车次']}: {row['车型']} ({row['始发站']}→{row['终到站']})")
    print("\n" + "="*50)
    print("实验完成！请查看生成的文件：")
    print("  - trains.json（时刻表详情）")
    print("  - trains.csv（统计汇总）")
    print("="*50)
if __name__ == '__main__':
    main()