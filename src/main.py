# Creato da pop mario denis 
# sopranome rda(RedAnonymusITA2)
# nome app :generatore di password 
# maker by pop mario denis
# nikname is rda(RedAnonymusITA2)
#app name  is:password generator
import os
from tkinter import Menu

import tkinter as tk
import random
import time
from string import ascii_letters,punctuation,digits
from other import w_other
# info  debug
os.system('clear')
print('Qui vedrai il password e il nome del file in temporeale (debug)')

# windows config 
class windows:
    def __init__(self):
        root = tk.Tk()
        root.geometry('300x160')
        root.title('GeneratorePassword')
        root.resizable(False,False)
       
       
        root.configure(bg='white')
        # label text info user
        self.text=tk.Label(root,text='Inserire Lunghezza password:',background='white')
        self.text.place(x=10,y=10)
        # input 
        self.lunghezza=tk.Entry(root,borderwidth=2)
        self.lunghezza.place(x=90,y=38,height=30, width=120)
        # version label and rda name
        self.txt_version=tk.Label(root,text='version:V0.1-alpha',bg='white')
        self.txt_version.place(x=1,y=140)
        self.txt_rda=tk.Label(root,text='by RDA',bg='white')
        self.txt_rda.place(x=228,y=140)

        # def g_password and other for button command 

        def info():
            root = tk.Tk()
            root.geometry('300x260')
            root.title('INFO')
            root.resizable(False,False)
            root.configure(bg='white')
            self.info_txt =tk.Label(root,text="""Autore : Pop Mario Denis
        Nome D'Arte: RDA(RedAnonymusITA2)
        Nome App : GeneratorePassword
    licenzza : MIT
    ATTENZI0NE:
            una volta scelto come salvare
            chiudere la pagina :
        (come voi salvare password 
        e poi anteprima)
        per evitare bug
    ---------------------------------------------------
Per altri software clicca sul bottone qui sotto

            """,bg='white')
            def other():
                w_other()
                pass
            self.info_txt.place(x=1,y=2)
            self.bt_altri=tk.Button(root,text='ALTRO',command=other,bg='white',activebackground='white',relief='flat')
            self.bt_altri.place(x=100,y=210)
            
     

        def g_password():
                try:
                    def save_password():
                        text =str(self.text1.get())
                        src =open('%s.txt'%(text),'w')
                        src.write(password)
                        src.close()
                        print('file salvato con nome:%s.txt'%(text))
                        self.txt_file=tk.Label(root5,text='file salvato con nome: %s.txt'%(text),bg='white')
                        self.txt_file.place(x=1,y=47)
                        
                      
                            
                    def swnf():
                       
                        root = tk.Tk()
                        root.geometry('330x100')
                        root.title('Salva_con_nome')
                        root.resizable(False,False)
                        root.configure(bg='white')
                        # entry 
                        self.text1=tk.Entry(root,borderwidth=2)
                        self.text1.place(x=20,y=20,height=30, width=190)
                        #button save 
                        self.bt_ok2=tk.Button(root,text='OK',command=save_password,bg='white',activebackground='white',relief='flat')
                        self.bt_ok2.place(x=220,y=20,height=30, width=110)

                        pass
                    def rnfs():
                        random_number =tuple(digits)
                        name= ""
                        for x in range(9):
                            name+=random.choice(random_number)
                        src =open('password%s.txt'%(name),'w')
                        src.write(password)
                        src.close()
                        
                        self.txt_file=tk.Label(root5,text='file salvato con nome: password%s.txt'%(name),bg='white')
                        self.txt_file.place(x=1,y=47)
                       
                    #------------------------
                    c =tuple(ascii_letters)+tuple(punctuation)+tuple(digits)
                    password= ""
                    l = int(self.lunghezza.get())
                    for x in range(l):
                        password+=random.choice(c)
                    
                    print('Il tuo password e: %s'%(password))
                    root5=tk.Tk()
                    root5.geometry('600x600')
                    root5.title('preview')
                    root5.configure(bg='white')
                    # label info user 
                    self.text1=tk.Label(root5,text='Qui vedrai in anteprima password e la EAD:',bg='white')
                    self.text1.place(x=1,y=1)
                    self.txt_password=tk.Label(root5,text='Il tuo password è: %s'%(password),bg='white')
                    self.txt_password.place(x=1,y=25)
                    

    
                    # new windows for save password
                    root = tk.Tk()
                    root.geometry('340x100')
                    root.title('Come vuoi salvare il password?')
                    root.resizable(False,False)
                    root.configure(bg='white')
                    
                    # button rnfs(random_name_file_save)
                    self.bt_rnfs =tk.Button(root,text='random_name_file_save',command=rnfs,bg='white',activebackground='white',relief='flat')
                    self.bt_rnfs.place(x=10,y=20)
                    # button  save whit name file (swnf)
                    self.bt_swnf=tk.Button(root,text='salva con nome ',command=swnf,bg='white',activebackground='white',relief='flat')
                    self.bt_swnf.place(x=200,y=20)
                    # encryption_cesare button 
                    def ead():
                        from ead import  encryption_cesare 
                        password2=encryption_cesare(password)
                        random_number =tuple(digits)
                        name= ""
                        for x in range(9):
                            name+=random.choice(random_number)
                        src =open('password%s.txt'%(name),'w')
                        src.write(password2)
                        src.close()
                        print('il password e stato salvato ed criptato')
                        

                    self.bt_en=tk.Button(root,text='encryption + salva',command=ead,bg='white',activebackground='white',relief='flat')
                    self.bt_en.place(x=10,y=50)
                except:
                    pass
        
      
        def de():
            from ead_Gui import main
            main()
        #button ok and info button 
        self.bt_ok=tk.Button(root,text='OK',command=g_password,bg='white',activebackground='white',relief='flat')
        self.bt_ok.place(x=211,y=38)
      
       
        menu1=tk.Menu(root,bg="white")
        root.configure(menu=menu1)
        file_menu=Menu(menu1,bg="white")
        menu1.add_cascade(label="Menu",menu=file_menu)
        
        file_menu.add_command(label="EAD",command=de)
        file_menu.add_separator()
        file_menu.add_command(label="INFO",command=info)
        file_menu.add_command(label="EXIT",command=quit)

        root.mainloop()
        
windows()