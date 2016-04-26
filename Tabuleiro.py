# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:52:07 2016

@author: Nathan
"""

import tkinter as tk
from codigo import Jogo

Jogo.matriz=[[0,0,0],[0,0,0],[0,0,0]]

def recebe_info(label,botao,X,O):
    if c%2 == 1 and Jogo.matriz[X][O]==0:
            botao.config(text="X")
    if c%2==0 and Jogo.matriz[X][O]==0:
            botao.config(text="O")
b = [Jogo.matriz[0][0],Jogo.matriz[0][1],Jogo.matriz[0][2],Jogo.matriz[1][0],Jogo.matriz[1][1],Jogo.matriz[1][2],Jogo.matriz[2][0],Jogo.matriz[2][1],Jogo.matriz[2][2]]
c = b.count(0)

class tabuleiro:
    def __init__(self,matriz):
        self.window= tk.Tk()
        self.matriz=[[0,0,0],[0,0,0],[0,0,0]]
      

        
    
        botao1 = tk.Button(self.window,width=15,height=10,)
        botao1.grid(row=0,column=0)
        botao1.configure(command= lambda:recebe_info(c))
        
        botao2 = tk.Button(self.window,width=15,height=10)
        botao2.grid(row=0,column=1)
        botao2.configure(command= lambda:recebe_info(c))
        
        botao3 = tk.Button(self.window,width=15,height=10)
        botao3.grid(row = 0,column=2)
        botao3.configure(command= lambda:recebe_info(c))
        
        botao4 = tk.Button(self.window,width=15,height=10)
        botao4.grid(row =1,column =0)
        botao4.configure(command= lambda:recebe_info(c))
        
        botao5 = tk.Button(self.window,width=15,height=10)
        botao5.grid(row =1, column = 1)
        botao5.configure(command= lambda:recebe_info(c))
        
        botao6 = tk.Button(self.window,width=15,height=10)
        botao6.grid(row = 1, column= 2)
        botao6.configure(command= lambda:recebe_info(c))
        
        botao7 = tk.Button(self.window,width=15,height=10)
        botao7.grid(row = 2,column=0)
        botao7.configure(command= lambda:recebe_info(c))
        
        botao8 = tk.Button(self.window,width=15,height=10)
        botao8.grid(row = 2, column = 1)
        botao8.configure(command= lambda:recebe_info(c))
        

        
        botao9 = tk.Button(self.window,width=15,height=10)
        botao9.grid(row = 2,column = 2)
        botao9.configure(command= lambda:recebe_info(c))
        
        label = tk.Label(self.window,text= "Proxíma jogada:")
        label.grid( row = 3)
        
    def iniciar(self):
        self.window.mainloop()
    
    
        
            
            



t = tabuleiro(Jogo.matriz)
t.iniciar()

#t.cb()
