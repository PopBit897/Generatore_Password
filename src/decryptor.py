# decryptor for main.py
from imghdr import what
import tkinter as tk 

from ead import decryptor_cesare
class windows:
    def __init__(self) -> None:
        
        root=tk.Tk()
        root.geometry('300x300')
        root.resizable(False,False)
        # file name 
        name=tk.Entry(root,borderwidth=0)
        name.place(x=40,y=100,height=30, width=190)
    
        def you_file():
           file= name.get()
           decryptor= decryptor_cesare(file)
        
           print(decryptor)
    
        ok_bt=tk.Button(root,text='OK',command=you_file)
        ok_bt.place(x=230,y=100)
  
  
        root.mainloop()
