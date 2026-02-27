#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : gui_demo.py
# @Author: yangyaxin
# @Date  : 2024/4/24
# @Desc  :

# 带有标签和按钮的tkinter gui程序
import tkinter
from tkinter import *

def lock_devId():
    devId =  entry_devId.get()
    output_devId= f'输出产品mac：{devId}\n'
    print("output_devId:",output_devId)
    txt.insert(END,output_devId)

def lock_prodTypeId():
    prodTypeId = entry_prodTypeId.get()
    output_prodTypeId = f'输出产品型号：{prodTypeId}\n'
    print("output_prodTypeId:",output_prodTypeId)
    txt.insert(END,output_prodTypeId)



win = Tk()
win.title("自动化测试工具")
win.geometry("720x640")

txt = Text(win)
txt.place(rely=0.6,relheight=0.8)

label_devId = Label(win,text="产品mac：")
label_devId.grid(row=0,column=0,padx=5,pady=5,sticky="w")
entry_devId = Entry(win,width=30)
entry_devId.grid(row=0,column=1,padx=5,pady=5)
# devId = entry_devId.get()
# print("devId:",devId)

label_prodTypeId = Label(win,text="产品型号：")
label_prodTypeId.grid(row=1,column=0,padx=5,pady=5,sticky="w")
entry_prodTypeId = Entry(win,width=30)
entry_prodTypeId.grid(row=1,column=1,padx=5,pady=5)
# prodTypeId = entry_prodTypeId.get()
# print("prodTypeId:",prodTypeId)

button_devId = Button(win,text="输入mac",command = lock_devId )
button_devId.grid(row=0,column=2,padx=5,pady=5)

button_prodTypeId = Button(win,text="输入型号",command = lock_prodTypeId)
button_prodTypeId.grid(row=1,column=2,padx=5,pady=5)

button_start = Button(win, text="开始测试" )
button_start.grid(row=5, columnspan=2, padx=5, pady=5)

win.mainloop()
#
# # win = Tk()
# # win.title("自动化测试工具")
# # win.geometry("700x700+200+50")
# # entry = Entry(win)
# # entry.pack()
# #
# # def get_input():
# #     input_str = entry.get()
# #     output_label = Label(win,text=f"输入框内容为：{input_str}")
# #     output_label.pack()
# #
# # button = Button(win,text="获取内容",command=get_input())
# # button.pack()
# #
# # win.mainloop()

# def run1():
#     a = float(inp1.get())
#     b = float(inp2.get())
#     s = '%0.2f+%0.2f=%0.2f\n' %(a,b,a +b)
#     txt.insert(END,s)
#     inp1.delete(0,END)
#     inp2.delete(0,END)
#
# def run2(x,y):
#     a = float(x)
#     b = float(y)
#     s = "%0.2f+%0.2f=%0.2f\n" %(a,b,a+b)
#     txt.insert(END,s)
#     inp1.delete(0,END)
#     inp2.delete(0,END)
#
# win = Tk()
# win.geometry('460x240')
# win.title("简单加法器")
# lb1  = Label(win,text="请输入两个数，按下面两个按钮之一进行加法计算")
# lb1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)
# inp1 = Entry(win)
# inp1.place(relx=0.1,rely=0.2,relwidth=0.3,relheight=0.1)
# inp2 = Entry(win)
# inp2.place(relx=0.6,rely=0.2,relwidth=0.3,relheight=0.1)
#
# # 方法-直接调用run1()
# btn1 = Button(win,text="方法一",command=run1)
# btn1.place(relx=0.1,rely=0.4,relwidth=0.3,relheight=0.1)
#
# # 方法二利用Lambda传参数调用run2（）
# btn2 = Button(win,text="方法二",command=lambda:run2(inp1.get(),inp2.get()))
# btn2.place(relx=0.6,rely=0.4,relwidth=0.3,relheight=0.1)
#
# # 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
# txt = Text(win)
# txt.place(rely=0.6,relheight=0.4)
#
# win.mainloop()

if __name__ == '__main__':
    # lock_gui()
    win.mainloop()
