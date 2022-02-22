# -----------------------------------------
# Create window and background and title
# -----------------------------------------

# import tkinter as tk
# root_window = tk.Tk()
# root_window.geometry('450x300')
# root_window["background"] = "#C9C9C9"
# text=tk.Label(root_window,text="C语言中文网，欢迎您",bg="yellow",fg="red",font=('Times', 20, 'bold italic'))
# text.pack()
# button=tk.Button(root_window,text="关闭",command=root_window.quit)
# button.pack(side="bottom")
# #进入主循环，显示主窗口
# root_window.mainloop()

# # Create window and boader width accordingly

# import tkinter as tk
# win = tk.Tk()
# win.title("C语言中文网")
# win.geometry('400x200')
# # 若内容是文字则以字符为单位，图像则以像素为单位
# label = tk.Label(win, text="网址：c.biancheng.net",font=('宋体',20, 'bold italic'),bg="#7CCD7C",
#                  # 设置标签内容区大小
#                  width=30,height=5,
#                  # 设置填充区距离、边框宽度和其样式（凹陷式）
#                  padx=10, pady=15, borderwidth=10, relief="sunken")
# label.pack()
# win.mainloop()

# -----------------------------------------
# Show figure
# -----------------------------------------

# import tkinter as  tk
# win = tk.Tk()
# win.title("Show figure")
# # win.iconbitmap('/home/gami-aiif/Pictures/05.02.2022/Screenshot from 2022-02-02 17-37-22.png')
# #显示图片(注意这里默认支持的图片格式为GIF)
# photo = tk.PhotoImage(file = '/home/gami-aiif/Pictures/05.02.2022/Screenshot from 2022-02-02 17-37-22.png')
# # print(type(photo))
# # 将图片放在主窗口的右边
# lab =tk.Label(win,image=photo).pack(side="right")
# # 显示文字，设置文本格式
# text = "I bet this can't have Chinese input"
# lab_text =tk.Label(win,text=text,fg ='#7CCD7C',font=('微软雅黑',15,'italic'),justify='left',padx=10).pack(side='left')
# button=tk.Button(win,text="关闭",command=win.quit)
# button.pack(side="bottom")
# win.mainloop()

# -----------------------------------------
# Message
# -----------------------------------------

# from tkinter import *
# #创建主窗口
# win = Tk()
# win.config(bg='#8DB6CD')
# win.title("C语言中文网")
# win.geometry('400x300')
# # win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# txt = "This text will be shown on the left side of main window"
# msg = Message (win, text=txt,width =60,font=('Times',10,'bold'))
# msg .pack (side=LEFT)
# #开始程序循环
# win .mainloop ()

# -----------------------------------------
# Botton
# -----------------------------------------

# import tkinter as tk
# # 创建窗口
# window =tk.Tk()
# # 设置回调函数
# def callback():
#     print ("click me!")
# # 使用按钮控件调用函数
# b = tk.Button(window, activebackground='pink', activeforeground='red', fg='blue', text="点击执行回调函数", font =('微软雅黑',15,'italic'), command=callback).pack() # Command uses the callback function in here
# # 显示窗口
# tk.mainloop()

# -----------------------------------------
# Botton example: Add function to botton
# -----------------------------------------

# import tkinter as tk
# from tkinter import messagebox
# window = tk.Tk()
# # 设置窗口的标题
# window.title('C语言中文网')
# # 设置并调整窗口的大小、位置
# window.geometry('400x300+300+200')
# # 当按钮被点击的时候执行click_button()函数
# def click_button():
#     # 使用消息对话框控件，showinfo()表示温馨提示
#     messagebox.showinfo(title='温馨提示', message='欢迎使用C语言中文网')
# # 点击按钮时执行的函数
# button = tk.Button(window,text='点击前往',bg='#7CCD7C',width=20, height=5,command=click_button).pack()
# button=tk.Button(window,text="关闭",command=window.quit)
# button.pack(side="bottom") 
# # 显示窗口
# window.mainloop()

# -----------------------------------------
# Botton example: Add figure to the botton
# -----------------------------------------

# import tkinter as tk
# from tkinter import messagebox
# window = tk.Tk()
# # 设置窗口的标题
# window.title('C语言中文网')
# # 设置窗口的大小
# window.geometry('400x300+300+200')
# # 当按钮被点击的时候执行click_button()函数
# def click_button():
#     # 使用消息对话框控件，showinfo()表示温馨提示
#     messagebox.showinfo(title='温馨提示', message='欢迎使用C语言中文网')
# # 创建图片对象
# im = tk.PhotoImage(file='/home/gami-aiif/Pictures/05.02.2022/Screenshot from 2022-02-02 17-37-22.png')
# # 通过image参数传递图片对象
# button = tk.Button(window,image=im,command=click_button).pack()
# # 启动窗口
# window.mainloop()

# -----------------------------------------
# Botton example: Grid function
# -----------------------------------------
# Generated row number will stack to below following the order, for example row = 1 3 5 9 doesn't mean putting text at position row 1 3 5 9, but row 0 1 2 3.
# 值得大家注意的是 grid() 布局方法不能与 pack() 混合在一起使用
# import tkinter as tk
# from tkinter import messagebox
# win = tk.Tk()
# win.title("C语言中文网")
# # win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# win.geometry('400x200+100+100')
# win.resizable(0,0)
# # 将俩个标签分别布置在第一行、第二行
# tk.Label(win, text="账号：").grid(row=0)
# tk.Label(win, text="密码：").grid(row=1)
# # 创建输入框控件
# e1 = tk.Entry(win)
# # 以 * 的形式显示密码
# e2 = tk.Entry(win,show='*')
# e1.grid(row=0, column=1, padx=10, pady=5)
# e2.grid(row=1, column=1, padx=10, pady=5)
# # 编写一个简单的回调函数
# def login():
#     messagebox.showinfo('欢迎您到来')
# # 使用 grid()的函数来布局，并控制按钮的显示位置
# tk.Button(win, text="登录", width=10, command=login).grid(row=3, column=0, sticky="w", padx=10, pady=5)
# tk.Button(win, text="退出", width=10, command=win.quit).grid(row=3, column=1, sticky="e", padx=10, pady=5)
# win.mainloop()

# -----------------------------------------
# Entry example: Dynamic text
# -----------------------------------------

# import tkinter as tk
# import time
# root = tk.Tk()
# root.title("C语言中文网")
# root.geometry('450x150+100+100')
# root.resizable(0,0)
# root.title('我们的时钟')
# # 获取时间的函数
# def gettime():
#     # 获取当前时间
#     dstr.set(time.strftime("%H:%M:%S"))
#     # 每隔 1s 调用一次 gettime()函数来获取时间
#     root.after(1000, gettime)
# # 生成动态字符串
# dstr = tk.StringVar()
# # 利用 textvariable 来实现文本变化
# lb = tk.Label(root,textvariable=dstr,fg='green',font=("微软雅黑",85))
# lb.pack()
# # 调用生成时间的函数
# gettime()
# # 显示窗口
# root.mainloop()

