# -*- coding: utf-8 -*-

import random
import tkinter
from tkinter import messagebox

# num初始值，作为随机数  
randomNumber = 0

def resetRandom():
    global randomNumber
    randomNumber = random.randint(0, 100)
    print(randomNumber)
  

resetRandom()


def Guess():
    try:
        inputValue = var.get()    #获得输入的值

        isinstance(inputValue, int)   #判断是不是int型
    except Exception:
        messagebox.showwarning("错误提示",'请输入纯数字!')#不是int型弹出警告弹框
    else:
        if inputValue != randomNumber: #判断输入值和随机数的大小
            if inputValue > randomNumber:
                messagebox.showinfo("猜错了","请输入一个更小的数字!")
            elif inputValue < randomNumber:
                messagebox.showinfo("猜错了","请输入一个更大的数字!")
        else:   #相等时，完成
            messagebox.showinfo("提示","恭喜你，猜到正确答案!")
            



def cancelInput():
    createInput.delete(0,100000000)





tk=tkinter.Tk()

tk.title("数字猜谜游戏")

#创建一个画布，声明宽和高
background = tkinter.Canvas(tk,width=350,height=350)

# 创建提示文字，且为红色
background.create_text(170,150,text="数字猜谜游戏",fill="red")

# 包装
background.pack()

var = tkinter.IntVar()

createInput = tkinter.Entry(tk,textvariable = var)   #创建一个输入框
createInput.place(relx=0.32,rely=0.5)


inputHeight = 2
inputWidth = 10

comfirm = tkinter.Button(text="Ok", width=inputWidth, height=inputHeight, command=Guess)  #创建一个button，调用guess函数
comfirm.place(relx=0.2, rely=0.7)

cancel = tkinter.Button(text="Cancel",width=inputWidth,height=inputHeight,command=cancelInput)
cancel.place(relx=0.45,rely=0.7);

reset = tkinter.Button(text="Reset",width=inputWidth,height=inputHeight,command=resetRandom)
reset.place(relx=0.7,rely=0.7);




tk.mainloop()