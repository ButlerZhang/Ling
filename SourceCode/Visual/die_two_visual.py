import pygal

from die import Die

#创建两个D6
die1 = Die()
die2 = Die()

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

#print(results)

#分析结果，统计每个点出现的次数
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequencie = results.count(value)
    frequencies.append(frequencie)

print(frequencies)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg') #用浏览器查看
