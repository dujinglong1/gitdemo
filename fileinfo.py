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

def pin():
    a1=a_text.get(1.0,tk.END)
    for i in range(len(a1)):
        if ord(a1[i])<65 or ord(a1[i])>122 or 90<ord(a1[i])<97:
            a1=a1.replace(a1[i],' ')
    a1=a1.lower()
    b1=a1.split()
    m=[]
    n=[]
    for i in range(len(b1)):
        m1=b1[i]
        n1=b1.count(m1)
        if m1 not in m:
            m.append(m1)
            n.append(n1)
    cipin_print=[]
    for i in range(len(m)):
        c1=str(m[i])+':'+str(n[i])+'次'
        cipin_print.append(c1)
    cipin_print.sort()
    cipin=tk.Tk()
    cipin.geometry('500x400')
    cipin.title('单词词频')
    cipin_text=tk.Text(cipin,width=70,height=35)
    for i in cipin_print:
        cipin_text.insert(tk.INSERT,i)
        cipin_text.insert(tk.INSERT,'\n')

    cipin_text.grid(row=0,column=0,padx=10,pady=10)
    
    ybar=tk.Scrollbar(cipin,orient=tk.VERTICAL,relief=tk.GROOVE)
    ybar.grid(row=0,column=1,sticky=tk.NS)
    ybar.config(command=cipin_text.yview)
    cipin_text.config(yscrollcommand=ybar.set)
    
    cipin.mainloop()

def keywords():
    a2=a_text.get(1.0,tk.END)
    for i in range(len(a2)):
        if ord(a2[i])<65 or ord(a2[i])>122 or 90<ord(a2[i])<97:
            a2=a2.replace(a2[i],' ')
    a2=a2.lower()
    b2=a2.split()
    tyc=open('英文停用词表.txt')
    tyc_list=tyc.readlines()
    for i in range(len(tyc_list)):
        k=list(tyc_list[i])
        k.remove(k[-1])
        k.remove(k[-1])
        tyc_list[i]=''.join(k)
    for i in range(len(b2)):
        if b2[i] in tyc_list:
            b2[i]='a'
    while 'a' in b2:
        b2.remove('a')
    c2=[]
    c0=[]
    d=[]
    d0=[]
    for i in range(len(b2)):
        p=b2[i]
        q=b2.count(p)
        if p not in c2:
            c2.append(p)
            d.append(q)
    for i in range(6):
        q=max(d)
        n=d.index(q)
        p=c2[n]
        c0.append(p)
        d0.append(q)
        c2.remove(p)
        d.remove(q)
    gjc=tk.Tk()
    gjc.geometry('500x400')
    gjc.title('关键词')
    gjc_text=tk.Text(gjc,width=70,height=35)
    for i in range(len(c0)):
        gjc_text.insert(tk.INSERT,str(c0[i])+':'+str(d0[i]))
        gjc_text.insert(tk.INSERT,'\n')
    gjc_text.grid(row=0,column=0,padx=10,pady=10)
    
    ind=np.arange(6)
    fig,ax=plt.subplots()
    rects1=ax.bar(ind,d0,width=0.3,color='green')
    ax.set_xticklabels(c0)
    ax.set_xticks(ind)
    ax.set_xlabel(u'关键词')
    ax.set_ylabel(u'频率')
    mpl.rcParams['font.sans-serif']=['SimHei']
    plt.show()
    
    gjc.mainloop()    

def th():
    a4=a_text.get(1.0,tk.END)
    b4=a4.split()
    c4=tk.Tk()
    c4.geometry('200x150')
    c4_label_1=tk.Label(c4,text='请输入您想替换的词：',width=20,height=1)
    c4_label_1.grid(row=0,column=0,padx=20,pady=3)
    c4_text_1=tk.Text(c4,width=20,height=1)
    c4_text_1.grid(row=1,column=0,padx=20,pady=3)
    c4_label_2=tk.Label(c4,text='请输入您替换后的词：',width=20,height=1)
    c4_label_2.grid(row=2,column=0,padx=20,pady=3)
    c4_text_2=tk.Text(c4,width=20,height=1)
    c4_text_2.grid(row=3,column=0,padx=20,pady=3)
    c4_button=tk.Button(c4,text='开始替换',command=lambda:ksth(c4_text_1,c4_text_2,b4,c4))
    c4_button.grid(row=4,column=0,padx=20,pady=3,sticky=tk.E)
    c4.mainloop()

def ksth(c5_text_1,c5_text_2,b5,c5):
    w1=c5_text_1.get(1.0,tk.END)
    w2=c5_text_2.get(1.0,tk.END)
    w1_list=list(w1)
    w2_list=list(w2)
    w1_list.remove(w1_list[-1])
    w2_list.remove(w2_list[-1])
    w1=''.join(w1_list)
    w2=''.join(w2_list)
    if w1 in b5 or w1+',' in b5 or w1+'.' in b5 or w1+'?' in b5 or w1+'!' in b5:
        while w1 in b5:
            b5[b5.index(w1)]=w2
        while w1+',' in b5:
            b5[b5.index(w1+',')]=w2+','
        while w1+'.' in b5:
            b5[b5.index(w1+'.')]=w2+'.'
        while w1+'?' in b5:
            b5[b5.index(w1+'?')]=w2+"?"
        while w1+'!' in b5:
            b5[b5.index(w1+'!')]=w2+'!'
        a_text.delete(1.0,tk.END)
        a_text.insert(tk.INSERT,' '.join(b5))
        c5.destroy()
    else:
        wrong=tk.Tk()
        wrong.geometry('230x150')
        wrong_label=tk.Label(wrong,text='错误：您需要替换的词不在文本中！')
        wrong_label.grid(row=0,column=0,padx=10,pady=10)
        wrong_button=tk.Button(wrong,text='OK',command=lambda:wrong.destroy())
        wrong_button.grid(row=1,column=0,padx=10,pady=30,sticky=tk.E)
        wrong.mainloop()
        


def chai():
    g=a_text.get(1.0,tk.END)
    for i in range(len(g)):
        if ord(g[i])<65 or ord(g[i])>122 or 90<ord(g[i])<97:
            g=g.replace(g[i],' ')
    g=g.lower()
    dt=tk.Tk()
    dt.geometry('800x600')
    dt_text=tk.Text(dt,width=107,height=46)
    dt_text.grid(row=0,column=0,padx=10,pady=10)
    dt_text.insert(tk.INSERT,g)
    ybar=tk.Scrollbar(dt,orient=tk.VERTICAL,relief=tk.GROOVE)
    ybar.grid(row=0,column=1,sticky=tk.NS)
    ybar.config(command=a_text.yview)
    a_text.config(yscrollcommand=ybar.set)
    dt.mainloop()           