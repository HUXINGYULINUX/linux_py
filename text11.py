from tkinter import * #tkinter是TK GUI工具包的接口
import time
root = tkinter( )#生成主窗口
root.geometry('300x300')#可视化窗口大小设置

var = StringVar( )#StringVar是tkinter下的变量
def show( ):
	global var
	text = time.strftime('%Y-%m-%d %H:%M:%S')#显示当前时间
	root.after(1000,show)
	var.set(text)
show( )
Label(root,textvariable=var).pack( )#用于显示窗口上的文本或部件

root.mainloop( )#显示主窗口