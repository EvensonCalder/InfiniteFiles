from tkinter import *
import webbrowser
import pickle
Links = []
Lab= []
last_operation="https://tntfiles.com/"
def Init():
    f=open("Data.dat","r")
    for link in f:
        Links.append(link)        
def Upload():
    url="https://tntfiles.com/"
    webbrowser.open(url, new=0, autoraise=True)
def Store():
    f=open("Data.dat","a")
    f.write(inp1.get()+" "+inp3.get()+"\n")
    Links.append(inp1.get()+" "+inp3.get())
def Search():
    for link in Links:
        for part in range(1,len(link)-len(inp2.get())):
            if link[part:part+len(inp2.get())]==inp2.get():
                txt = Text(root)
                txt.place(relx=0.5,rely=0.6,relwidth=0.3,relheight=0.15)
                txt.insert(END,link.split(' ')[0]+"\n")
                global last_operation
                last_operation=link.split(' ')[0]
                
def Get():
    url=last_operation
    webbrowser.open(url, new=0, autoraise=True)
root=Tk()
Init()
root.title('InfuniteFiles')
root.geometry('720x480')
lb1 = Label(root,text='Infinite Files')
lb1.place(relx=0.1, rely=0, relwidth=0.7, relheight=0.1)
lb2 = Label(root,text='Enter Download Link Here')
lb2.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)
lb3 = Label(root,text='Search For Links')
lb3.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.1)
lb4 = Label(root,text='Add Tags')
lb4.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.1)
btn1 = Button(root, text='Upload', command=Upload)
btn1.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.1)
btn2 = Button(root, text='Store Link', command=Store)
btn2.place(relx=0.1, rely=0.8, relwidth=0.3, relheight=0.1)
btn3 = Button(root, text='Search', command=Search)
btn3.place(relx=0.5, rely=0.4, relwidth=0.3, relheight=0.1)
btn4 = Button(root, text='Get', command=Get)
btn4.place(relx=0.5, rely=0.8, relwidth=0.3, relheight=0.1)
inp1 = Entry(root) #link
inp1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
inp2 = Entry(root) #search
inp2.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.1)
inp3 = Entry(root) #tag
inp3.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)
root.mainloop()
