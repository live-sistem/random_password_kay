from tkinter import * 
import tkinter as tk 
from tkinter.messagebox import showinfo
from main import fmain

def def_main():
    pres_kay = intager_entry.get()
    try:
        passs = fmain(int(pres_kay))
        if passs == False:
            showinfo(title="Erorr", message="слишком мало min 4")
        else:
            text1.delete("1.0", tk.END)
            text1.insert("1.0", passs)
    except:
        showinfo(title="Erorr", message="только цыфры")

def auto_insert_10():
    int_10 = button_entry_10['text']
    intager_entry.delete(0,tk.END)
    intager_entry.insert(0,int_10)

def auto_insert_15():
    int_15 = button_entry_15['text']
    intager_entry.delete(0,tk.END)
    intager_entry.insert(0,int_15)

def auto_insert_20():
    int_20 = button_entry_20['text']
    intager_entry.delete(0,tk.END)
    intager_entry.insert(0,int_20)

if __name__ == '__main__':        
    root = Tk()
    root.title("DEV")
    root.geometry("400x300")

    intager_entry = Entry(validate="key") 
    intager_entry.grid(row=0, column=0)

    button1=Button(root,text='ok',width=11,height=2, command=def_main)
    button1.grid(row=0, column=1)
    
    button_entry_10=Button(root,text="10",width=10,height=2, command=auto_insert_10)
    button_entry_10.grid(row=1, column=2)

    button_entry_15=Button(root,text="15",width=10,height=2, command=auto_insert_15)
    button_entry_15.grid(row=2, column=2)

    button_entry_20=Button(root,text="20",width=10,height=2, command=auto_insert_20)
    button_entry_20.grid(row=3, column=2)

    

    text1=Text(root,height=7,width=25,font='Arial 14',wrap=WORD)
    text1.grid(row=4, columnspan=3, sticky='ew')

    
    root.mainloop()