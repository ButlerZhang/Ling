import matplotlib.pyplot as plt


#绘制线段
squares = [1,4,9,16,25]

#linewidth表示线条的粗细
#如果没有输入值，则输出的图形不正确，4对应25
#plt.plot(squares, linewidth = 5)

#通过输入值，可以使得x和y的值能一一对应
input_values = [1,2,3,4,5]
plt.plot(input_values, squares, linewidth=5)

#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
