import pygal

from die import Die

#创建一个D6
die = Die()

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#print(results)

#分析结果，统计每个点出现的次数
frequencies = []
for value in range(1, die.num_sides+1):
    frequencie = results.count(value)
    frequencies.append(frequencie)

print(frequencies)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [str(x) for x in range(1, die.num_sides+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg') #用浏览器查看
