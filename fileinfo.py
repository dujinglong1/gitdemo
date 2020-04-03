#dujinglong
#2019.12.18
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def openfile():
    a0=filedialog.askopenfilename()
    b0=open(a0)
    strings=b0.read()
    a_text.insert(tk.INSERT,'\n'+strings)
    print(a0)   

def closefile():
    a_text.delete(1.0,tk.END)

def zong():
    g=a_text.get(1.0,tk.END)
    for i in range(len(g)):
        if ord(g[i])<65 or ord(g[i])>122 or 90<ord(g[i])<97:
            g=g.replace(g[i],' ')
    g=g.lower()
    h=g.split()
    zongji=tk.Tk()
    zongji.geometry('300x200')
    zongji.title('单词总数')
    zj_label=tk.Label(zongji,text='总计'+str(len(h))+'个单词')
    zj_label.grid(row=0,column=0,pady=50,padx=50)
    zj_button=tk.Button(zongji,text='OK',command=lambda:zj_close(zongji))
    zj_button.grid(row=1,column=1,padx=30,pady=30)
    zongji.mainloop()
    
def zj_close(zongji):
    zongji.destroy()