import csv

from datetime import datetime
from matplotlib import pyplot as plt



filename = "data/sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)

    #next返回下一行
    #下面调用一次，返回第一行
    header_row = next(reader)

    #enumerate返回每个元素的索引和值
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []

    #reader从停留的地方往下读取CSV文件，并返回当前所处位置的下一行
    for row in reader:

        try:

            #索引0的值是日期
            current_date = datetime.strptime(row[0], "%Y-%m-%d")

            #索引1的值是最高温度
            high = int(row[1])

            #索引3的值是最低温度
            low = int(row[3])

        except ValueError:

            print(current_date, 'missing data')

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    print(highs)

    #根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5) #alpha表示透明度
    plt.plot(dates, lows, c='blue', alpha=0.5) #0表示完全透明，1表示完全不透明

    #传递一个x值系列，两个y值系列，用facecolor填充两个y值之间的空间
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    #设置图形格式
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() #绘制斜标签
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
