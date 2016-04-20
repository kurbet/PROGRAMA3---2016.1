# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:52:07 2016

@author: Nathan
"""

import tkinter as tk

class tabuleiro:
    def __init__(self):
        self.window= tk.Tk()
      
    def cb(self,event):
       botao1.configure()
        
    
        botao1 = tk.Button(self.window,width=15,height=10)
        botao1.grid(row=0,column=0)
        botao1.configure(command=)
        
        botao2 = tk.Button(self.window,width=15,height=10)
        botao2.grid(row=0,column=1)
        botao2.configure(command=)
        
        botao3 = tk.Button(self.window,width=15,height=10)
        botao3.grid(row = 0,column=2)
        botao3.configure(command=)
        
        botao4 = tk.Button(self.window,width=15,height=10)
        botao4.grid(row =1,column =0)
        botao4.configure(command=)
        
        botao5 = tk.Button(self.window,width=15,height=10)
        botao5.grid(row =1, column = 1)
        botao5.configure(command=)
        
        botao6 = tk.Button(self.window,width=15,height=10)
        botao6.grid(row = 1, column= 2)
       botao6.configure(command=)
        
        botao7 = tk.Button(self.window,width=15,height=10)
        botao7.grid(row = 2,column=0)
       botao7.configure(command=)
        
        botao8 = tk.Button(self.window,width=15,height=10)
        botao8.grid(row = 2, column = 1)
       botao8.configure(command=)
        
        botao9 = tk.Button(self.window,width=15,height=10)
        botao9.grid(row = 2,column = 2)
        botao9.configure(command=)
        
        label = tk.Label(self.window,text= "Proxíma jogada:")
        label.grid( row = 3)
        
    def iniciar(self):
        self.window.mainloop()
t = tabuleiro()
t.iniciar()
t.cb()
