  # 5. 从CSV读取并统计
print("\n【5】从CSV读取 - 简单统计...")
csv_data = load_csv('trains.csv')
print(f"CSV中共有 {len(csv_data)} 趟列车：")
for row in csv_data:
        print(f"  {row['车次']}: {row['车型']} ({row['始发站']}→{row['终到站']})")