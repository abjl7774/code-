import random

with open('data.txt', 'w', encoding='utf-8') as fp:
    for _ in range(10):
        num = random.randint(0, 100)
        fp.write(str(num) + '\n')

with open('data.txt', 'r') as fp:
    data = fp.readlines()

data = [int(line.strip()) for line in data]
data.sort()
data = [str(i) + '\n' for i in data]

with open('data_asc.txt', 'w', encoding='utf-8') as fp:
    fp.writelines(data)