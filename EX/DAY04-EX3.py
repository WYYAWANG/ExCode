row = int(input('请输入行数: '))
for i in range(row):
    for x in range(i + 1):
        print('*', end='') #不换行输出
    print()