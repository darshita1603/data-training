import pytube
import tkinter as Tk
from pytube import YouTube
from tkinter import font



m=Tk.Tk()
m.title("Text to Speech")
m.geometry("350x300")

def start():
    text=enter.get()
    print(text) 
    youtube =pytube.YouTube(text)  
    video = youtube.streams.first()  
    video.download()   


def reset():
     enter.set("")

def exit():
    m.destroy()

l1=Tk.Label(m,text="Downloader",font="Helvetica 15 bold")
l1.place(x=110,y=10)

enter=Tk.StringVar()
value_entry=Tk.Entry(m,width=40,highlightbackground="black",textvariable=enter)
value_entry.place(x=35,y=70)

b1=Tk.Button(m,text="Download",height=2,width=8,bd=2,bg="Green",fg="White",command=start)
b1.place(x=50,y=120)

b2=Tk.Button(m,text="Reset",height=2,width=8,bd=2,bg="blue",fg="White",command=reset)
b2.place(x=120,y=120)

b3=Tk.Button(m,text="Exit",height=2,width=8,bd=2,bg="Red",fg="White" ,command=exit)
b3.place(x=190,y=120)

m.mainloop()