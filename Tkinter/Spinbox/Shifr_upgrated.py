import tkinter as tk
import string
from tkinter.ttk import Combobox
class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.enry = None
        self.spinbox_field = None
        self.shifr = None

        self.choice = tk.IntVar()
        self.combo = None
        


    def run(self):
        self.drow_entry()
        self.drow_label()
        self.drow_radiobuttons()
        self.drow_combobox()
        self.drow_button()
        self.spinbox()
        self.root.mainloop()

    def main_shifr(self):
        choice = self.combo.get()
        if choice == "Cesar":
            self.cesar()
        elif choice == "Wilinger":
            self.wilinger()

        self.enry.delete(0, tk.END)
        self.enry.insert(0,self.shifr)            

   
    def wilinger(self):
        choice = self.choice.get()
        key = self.spinbox_field.get()
        word = self.enry.get()
        a = string.ascii_lowercase
        alphabet = a*2
        d = ' ' + key * 10
        self.shifr = ''
        for letter in word:
            position = alphabet.find(letter)
            word = 1
            position2 = alphabet.find(d[word])
            if choice == 0:
                new_position = position + position2
                if letter in alphabet:
                    self.shifr += alphabet[new_position]
                else:
                    self.shifr += letter
                    word += 1
            else:    
                new_position = position - position2
                if letter in alphabet:
                    self.shifr += alphabet[new_position]
                else:
                    self.shifr += letter
                    word += 1
        
        return self.shifr    
        


    def cesar(self):
        choice = self.choice.get()
        word = self.enry.get()
        key = int(self.spinbox_field.get())
        self.shifr = ''
        a = string.ascii_lowercase
        alphabet = a * 2
        for letter in word:
            position = a.find(letter)
            if choice == 0:
                new_position = position + key
                if letter in alphabet:
                    self.shifr += alphabet[new_position]
                else:
                    self.shifr += letter
            else:
                new_position = position - key
                if letter in alphabet:
                    self.shifr += alphabet[new_position]
                else:
                    self.shifr += lette 

        return self.shifr                 
                


    def delete_all(self):

        self.enry.delete(0, tk.END)
        if len(self.enry2.get()) ==0:
            self.enry2.destroy()
        else:    
            self.enry2.delete(0, tk.END)



    def spinbox(self):
        self.spinbox_field = tk.Spinbox(self.root, from_ = 1, to_ =1000, wrap = True) 
                   
        self.spinbox_field.grid(row=0, column = 4)

        return self.spinbox_field



    def drow_label(self):
        self.lab1 = tk.Label(self.root, text = "Your text", bg = "purple", fg = "yellow", width = 20)    
        self.lab1.grid(row =0, column = 0)
        return self.lab1

    def drow_entry(self):
        self.enry = tk.Entry(self.root, width = 30, bg = "pink", fg = "blue",
                        highlightbackground = "red", selectforeground = "yellow",
                         selectbackground = "green", justify = "center" )    
        self.enry.grid(row=0, column = 2)

        return self.enry

    def drow_button(self):

        butt1 = tk.Button(self.root, width = 20, height =2, text = "Shifr your text", command = self.main_shifr)
        butt1.grid(row = 2, column = 2)  
        butt1 = tk.Button(self.root, width = 20, height =2, text = "Delete all",command =  self.delete_all)
        butt1.grid(row = 3, column = 2) 
        butt1 = tk.Button(self.root, width = 20, height =2, text = "Quit",command =  self.root.destroy)
        butt1.grid(row = 5, column = 2, padx = 5, pady = 120)    


    def drow_radiobuttons(self):
        tk.Radiobutton(self.root, text = "Shifr          ", bg = "purple",font = ("Arial", 13),selectcolor = "yellow", activebackground = "yellow", activeforeground = "green", width = 20,variable = self.choice, value = 0).grid(row = 1, column = 3, sticky ="e")
        tk.Radiobutton(self.root, text = "Deshifr       ",bg = "purple",font = ("Arial", 13),selectcolor = "yellow", activebackground = "yellow", activeforeground = "green", width = 20, variable = self.choice, value = 1 ).grid(row = 2, column = 3, sticky ="e")    

    def drow_combobox(self):
        
        self.combo = Combobox(self.root, values = ("Cesar", "Wilinger"),state = "readonly")
        self.combo.current(0)
        self.combo.grid(row = 1, column =4)


        

some = Window("My App", 300, 700, "purple")
some .run()