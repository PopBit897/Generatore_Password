from ead import encryption_cesare
import tkinter as tk
class main_1():
    def __init__(self) -> None:
        root=tk.Tk()
        root.resizable(False,False)
        root.geometry('500x300')
        name=tk.Entry(root,borderwidth=2)
        name.place(x=140,y=100,height=30, width=200)
        def you_file1():
           file1= name.get()
           encryption= encryption_cesare(file1)
           print(encryption)
        self.text=tk.Label(root,text="Il testo o password deve essere scritto in maiuscolo")
        self.text.place(x=101,y=60)
        ok_bt=tk.Button(root,text='OK',command=you_file1)
        ok_bt.place(x=400,y=100)
        root.mainloop()

        pass
