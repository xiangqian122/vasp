#画能垒图
# 0-1:IS, 2-3:TS1, 4-5:MS1,6-7:TS2,8-9:MS2以此类推（）
#能垒数据不知道的可以再输入文件里在对应的位置输入99，这样就不会显示出来了
#每一行的数据个数必须是奇数个
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#读取能垒数据进行画图(TXT文件)
#格式IS,TS1,MS1,TS2,MS2,TS3,MS3
font1 = {
    'family': 'Times New Roman',
         'weight': 'normal',
         'size': 24,
}#坐标轴标签的字体设置

font2 = {
    'family': 'Times New Roman',
         'weight': 'normal',
         'size': 15,
}#坐标轴刻度的设置
labels = [1,2,3,4,5] #每条路径的图例
data_path = "D:\\codeing\\working\\ZnCrO\\" #输入文件的路径
colormap = ['#000000','#0000FF','#FF0000','#FFFF00','#008000','#00FFFF','#EE82EE']
#黑色，蓝色，红色，黄色，绿色，青色，紫色，每条路径的颜色
with open(data_path+"input.txt", "r") as f:
    count = len(open(data_path+"input.txt", "rU").readlines())#统计文本的行数为后面的路径数做准备

fig,Axes =plt.subplots(1)
'''
定义新的图例
'''
black_patch = mpatches.Patch(color='black', label='The first line')
blue_patch = mpatches.Patch(color='blue', label='The second line')
red_patch = mpatches.Patch(color='red', label='The third line')
yellow_patch = mpatches.Patch(color='yellow', label='The fourth line')
green_patch = mpatches.Patch(color='green', label='The fifth line')
Cyan_patch = mpatches.Patch(color='Cyan', label='The sixth line')
purple_patch = mpatches.Patch(color='purple', label='The seventh line')

with open(data_path+"input.txt", "r") as f:
    for j ,line in zip(range(count),f.readlines()):
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        line = line.replace(" ","") #去掉所有的空格
        line = line.split(",") #去掉每一个的分隔符，默认是逗号
        line = [float(x) for x in line] #将字符串转换为数字
        if not (len(line)+1)%2 == 0:
            print("数据缺失，请根据格式进行输入(数字个数是奇数个)")
        else:
            for i in range(len(line)):
                if line[i] == 99:
                    continue
                else:
                    plt.hlines(line[i], 2*i, 2*i+1, color=colormap[j], linewidth = 3) #画水平的线
                #plt.text(2*i+0.5, line[i]+0.05, '%.2f'%line[i],ha ='center', fontsize= 12,color =colormap[j],)
                #下面都是画连接线以及显示能垒和反应热
                if i>=1 and i %2 == 0 :
                    plt.text(2*i+0.5, line[i]+0.02,'%.2f' %(line[i]-line[i-2]), ha='center', fontsize =12, color = colormap[j])
                if i>=1 and i%2 ==1:
                    plt.text(2*i+0.5, line[i]+0.01,'%.2f' %(line[i]-line[i-1]), ha='center', fontsize =12, color = colormap[j])
            for i in range(len(line)-1):
                if line[i+1] == 99:
                    continue
                elif line[i] == 99:
                    continue
                else:
                    Axes.plot([2*i+1,2*i+2], [line[i], line[i+1]], color=colormap[j],ls ='--', linewidth = 0.5,)
            '''
            替换横坐标的刻度值
            '''
            x_labels = ["IS","TS1","MS1","TS2","MS2","TS3",'MS3',"TS4",'MS4',"TS5","MS5","TS6",'MS6',"TS7",'MS7','TS8','MS8',"TS9",'MS9']
            x_values = [0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5,32.5,34.5,36.5]
            x1 = []
            x2 = []
            for i in range(len(line)):
                X1 = x1.append(x_values[i]) 
                X2 = x2.append(x_labels[i])
            plt.xticks(x1,x2)
    plt.xlabel("Reaction coordinate",font1)  #设置x轴标签
    plt.ylabel("Energy (eV)",font1) #设置y轴的标签
    plt.ylim(-1,3) #设置显示的范围，根据具体情况设计
    plt.title("Energy profile") #设置绘图的标题
    plt.tick_params(labelsize=18) #设置坐标轴刻度大小
    labels = Axes.get_xticklabels() + Axes.get_yticklabels()
    # print labels
    [label.set_fontname('Times New Roman') for label in labels]
    handles_all =[black_patch,blue_patch,red_patch,yellow_patch,green_patch,Cyan_patch,purple_patch]
    c = []
    for i in range(count):
        d = c.append(handles_all[i])
    Axes.legend(loc='upper right',frameon=False, prop=font2,handles=c)
    plt.show()