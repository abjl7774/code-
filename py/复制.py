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
