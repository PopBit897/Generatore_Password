import tkinter as tk 
import os
import time 
import webbrowser
class w_other :
    def __init__(self) -> None:
            
        root = tk.Tk()
        root.geometry('400x100')
        root.title('Scarica altri software ')
        root.configure(bg='white')
        root.resizable(False,False)

        def no1():
            print("Chiusura del software in corso ....")
            time.sleep(5)
            

            exit()
        def yes1():
            print('Mi sto colegando al server ...')
            time.sleep(0.5)
            print('Sto scaricando ....')
            time.sleep(5)
            os.system('git clone https://github.com/RedAnonymusITA/ip_tools_GUI.git')
            time.sleep(0.2)
            print('Lo trovi ne cartella del software password/cod ')
            time.sleep(5)
            os.system('clear')
        # button ip_tools-gui
        def gui():
                      
            root = tk.Tk()
            root.geometry('400x100')
            root.title('INFO')
            root.configure(background='white')
            # def button 
           
            self.w =tk.Label(root,text="""Vuoi scaricarlo, vera salvato nella cartella cod """,bg='white')
            self.w.place(x=1,y=1)
            self.bt_no =tk.Button(root,text='NO',command= no1,bg='white',activebackground='white',relief='flat')
            self.bt_no.place(x=1,y=30)
            self.bt_yes =tk.Button(root,text='SI',command= yes1,bg='white',activebackground='white',relief='flat')
            self.bt_yes.place(x=78,y=30)
            root.resizable(False,False)
        def yes3():
            url = 'https://github.com/RedAnonymusITA/ip-tools/releases/tag/v0.0.1'
            print('Sto aprendo il tuo browser ...')
            time.sleep(5)
            webbrowser.open(url)
            
            


        def ip_0():
            root = tk.Tk()
            root.geometry('400x100')
            root.title('INFO')
            root.configure(bg='white')
            # def button 
           
            self.w =tk.Label(root,text="""Vuoi scaricarlo, vera salvato nella cartella cod """,bg='white')
            self.w.place(x=1,y=1)
            self.bt_no =tk.Button(root,text='NO',command= no1,bg='white',activebackground='white',relief='flat')
            self.bt_no.place(x=1,y=30)
            self.bt_yes =tk.Button(root,text='SI',command= yes3,bg='white',activebackground='white',relief='flat')
            
            self.bt_yes.place(x=78,y=30)
            root.resizable(False,False)

        def yes2():
            print('Mi sto colegando al server ...')
            time.sleep(0.5)
            print('Sto scaricando ....')
            time.sleep(5)
            os.system('git clone https://github.com/RedAnonymusITA/ip-tools.git')
            time.sleep(0.2)
            print('Lo trovi ne cartella del software password/cod ')
            time.sleep(5)
            os.system('clear')
        def ip_1():
            root = tk.Tk()
            root.geometry('400x100')
            root.title('INFO')
            root.configure(bg='white')
            # def button 
           
            self.w =tk.Label(root,text="""Vuoi scaricarlo, vera salvato nella cartella cod """,bg='white',activebackground='white')
            self.w.place(x=1,y=1)
            self.bt_no =tk.Button(root,text='NO',command= no1,bg='white',activebackground='white',relief='flat')
            self.bt_no.place(x=1,y=30)
            self.bt_yes =tk.Button(root,text='SI',command= yes2,bg='white',activebackground='white',relief='flat')
            self.bt_yes.place(x=78,y=30)
            root.resizable(False,False)

      


            pass
        self.bt_gui=tk.Button(root,text='ip_tools-Gui',command=gui,bg='white',activebackground='white',relief='flat')
        self.bt_gui.place(x=20,y=10)
        # button ip_tools-terminale amd cmd  v0.0.1
        self.bt_ip_0=tk.Button(root,text='ip_tools-terminale and cmd v0.0.1',command=ip_0,bg='white',activebackground='white',relief='flat')
        self.bt_ip_0.place(x=140,y=10)
        # button ip_tools-terminale and cmd v0.1.1
        self.bt_ip_1=tk.Button(root,text='ip_tools-terminale and cmd v0.1.1',command=ip_1,bg='white',activebackground='white',relief='flat')
        self.bt_ip_1.place(x=10,y=43)


        root.mainloop()
# info :
# other is librery for passwordgenerator 
# librery by RDA
# author name is Pop Mario Denis 
# made italy 
# cod enghlis end italy
# altro e una libreria per passwordgeneratore
#libreria di RDA
#nome autore Pop Mario Denis
# creato in italia
#codice inglese e italiano