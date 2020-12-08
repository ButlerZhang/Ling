import matplotlib.pyplot as plt


#s参数表示点的尺寸，下面是绘制一个点
#plt.scatter(2, 4, s=200)

#绘制五个点
#x_values = [1,2,3,4,5]
#y_values = [1,4,9,16,25]
#plt.scatter(x_values, y_values, s=100)

#绘制一千个点
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
#plt.scatter(x_values, y_values, s=40)

#删除数据点的轮廓需要传递参数edgecolor='none'
#plt.scatter(x_values, y_values, edgecolor='none', s=40)

#自定义点的颜色：使用颜色名称
#plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

#自定义点的颜色：使用RGB值
#plt.scatter(x_values, y_values, c=(0,0,0.8), edgecolor='none', s=40)

#使用颜色映射，例如由浅变深
#给参数c赋值y值列表，使用cmap告诉pyplot使用哪个颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

#设置图表标题并给出坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
#plt.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标轴的取值范围，x和y的最小值和最大值
plt.axis([0,1100,0,1100000])

plt.show()

#自动保存图表，注释掉show()调用
#第一个参数表示文件名，第二个参数表示是否裁减掉空白区域
#plt.savefig('squares_plot.png', bbox_inches='tight')
