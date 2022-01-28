from encryptor_gui import main_1
from decryptor import windows
import tkinter as tk
from ead import decryptor_cesare,encryption_cesare
class main:
    def __init__(self) -> None:
        
        root=tk.Tk()
        root.geometry('300x200')
        root.title('EAD_GUI')
        root.configure(bg='white')
        root.resizable(False,False)
        # button 
        def bt1():
            windows()
        def bt2():
            main_1()

        
            pass
        self.bt_decryptor=tk.Button(root,text='decryptor',command=bt1)
        self.bt_decryptor.place(x=1,y=1)

        self.bt_encryption=tk.Button(root,text='encryption',command=bt2)
        self.bt_encryption.place(x=101,y=1)

        root.mainloop()
        pass
