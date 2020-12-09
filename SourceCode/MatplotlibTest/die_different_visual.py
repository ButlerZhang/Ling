import pygal

from die import Die

#D6和D10
die1 = Die()
die2 = Die(10)

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
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

hist.title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice_visual.svg') #用浏览器查看
