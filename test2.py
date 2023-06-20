import csv

batch_size = 80
data = []

# 读取CSV文件并保存为列表
with open('fyx_chinamoney.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        data.append(row)

# 将列表拆分成多个批次
batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

# 打印输出每个批次
for idx, batch in enumerate(batches):
    print('第{}批次:'.format(idx))
    print(batch)
    print()