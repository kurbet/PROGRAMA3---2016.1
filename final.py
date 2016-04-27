# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 00:58:57 2016

@author: andre_000
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:43:56 2016

@author: andre_000
"""

import tkinter as tk
from Jogo import Jogo
from numpy import zeros
import tkinter.messagebox

class tabuleiro:
    def __init__(self):
        self.window= tk.Tk()
        self.window.title("Tic Tac Toe - André e Nathan")
        objeto_jogo = Jogo(zeros((3,3), 1, 0)
        self.jogo = objeto_jogo
      
        botao_1 = tk.Button(self.window,width=15,height=10)
        botao_1.grid(row=0,column=0)
        botao_1.configure(command=self.bt1)
        
        botao_2 = tk.Button(self.window,width=15,height=10)
        botao_2.grid(row=0,column=1)
        botao_2.configure(command=self.bt2)
        
        botao_3 = tk.Button(self.window,width=15,height=10)
        botao_3.grid(row = 0,column=2)
        botao_3.configure(command=self.bt3)
        
        botao_4 = tk.Button(self.window,width=15,height=10)
        botao_4.grid(row =1,column =0)
        botao_4.configure(command=self.bt4)
        
        botao_5 = tk.Button(self.window,width=15,height=10)
        botao_5.grid(row =1, column = 1)
        botao_5.configure(command=self.bt5)
        
        botao_6 = tk.Button(self.window,width=15,height=10)
        botao_6.grid(row = 1, column= 2)
        botao_6.configure(command=self.bt6)
        
        botao_7 = tk.Button(self.window,width=15,height=10)
        botao_7.grid(row = 2,column=0)
        botao_7.configure(command=self.bt7)
        
        botao_8 = tk.Button(self.window,width=15,height=10)
        botao_8.grid(row = 2, column = 1)
        botao_8.configure(command=self.bt8)
        
        botao_9 = tk.Button(self.window,width=15,height=10)
        botao_9.grid(row = 2,column = 2)
        botao_9.configure(command=self.bt9)
        
        label = tk.Label(self.window,text= "Proxíma jogada:")
        label.grid( row = 3, column = 0)
        
    def iniciar(self):
        self.window.mainloop()
        
    def estado_botao(self):             #função que ativa o botão e permite texto
        self.botao_1.configure(text = "", state = "active")
        self.botao_2.configure(text = "", state = "active")
        self.botao_3.configure(text = "", state = "active")
        self.botao_4.configure(text = "", state = "active")
        self.botao_5.configure(text = "", state = "active")
        self.botao_6.configure(text = "", state = "active")
        self.botao_7.configure(text = "", state = "active")
        self.botao_8.configure(text = "", state = "active")
        self.botao_9.configure(text = "", state = "active")
    
    def bt1(self):                  #atividade do botão 1
        if self.Jogo.turno == 1:
            self.botao_1.configure(text = "X")           #se o turno 1 selecionar o botão 1, marca X
        else:
            self.botao_1.configure(text = "O")           #se o turno 2 selecionar o botão 1, marca O
        if self.Jogo.rodada % 2 == 1:               #se a rodada for ímpar, X é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: X")
        else:               #se a rodada for par, O é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: O")
        self.Jogo.recebe_jogada(0,0)        #marca a jogada       
        x = self.Jogo.verifica_ganhador()           #pega o resultado da função "verifica_ganhador" na classe "Jogo"
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if (x == 2) or (x == 1) or (x == 0):
            self.Jogo.limpa_jogadas()           #limpa tabuleiro
            self.limpa() 
        else:
            self.botao_1.configure(state="disabled")         #desativa o botão
            
    def bt2(self):                  #atividade do botão 2
        if self.Jogo.turno == 1:
            self.botao_2.configure(text = "X")       #se o turno 1 selecionar o botão 2, marca X
        else:
            self.botao_2.configure(text = "O")       #se o turno 2 selecionar o botão 2, marca O
        if self.Jogo.rodada % 2 == 1:           #se a rodada for ímpar, X é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: X")
        else:               #se a rodada for par, O é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: O")
        self.Jogo.recebe_jogada(0,0)            #marca a jogada
        x = self.Jogo.verifica_ganhador()       #pega o resultado da função "verifica_ganhador" na classe "Jogo"
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if (x == 2) or (x == 1) or (x == 0):
            self.Jogo.limpa_jogadas()       #limpa tabuleiro
            self.limpa() 
        else:
            self.botao_2.configure(state="disabled")          #desativa o botão
                
    
    def bt3(self):              #atividade do botão 3
        if self.Jogo.turno == 1:
            self.botao_3.configure(text = "X")           #se o turno 1 selecionar o botão 3, marca X
        else:
            self.botao_3.configure(text = "O")           #se o turno 2 selecionar o botão 3, marca O
        if self.Jogo.rodada % 2 == 1:               #se a rodada for ímpar, X é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: X")
        else:                                       #se a rodada for par, O é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: O")
        self.Jogo.recebe_jogada(0,2)                #marca a jogada
        x = self.Jogo.verifica_ganhador()           #pega o resultado da função "verifica_ganhador" na classe "Jogo"
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if (x == 2) or (x == 1) or (x == 0):
            self.Jogo.limpa_jogadas()               #limpa tabuleiro
            self.limpa()
        else:
            self.botao_3.configure(state="disabled")         #desativa o botão
        
    def bt4(self):                  #atividade do botão 4
        if self.Jogo.turno == 1:
            self.botao_4.configure(text = "X")       #se o turno 1 selecionar o botão 4, marca X
        else:
            self.botao_4.configure(text = "O")       #se o turno 2 selecionar o botão 4, marca O
        if self.Jogo.rodada % 2 == 1:           #se a rodada for ímpar, X é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: X")
        else:                #se a rodada for par, O é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: O")
        self.Jogo.recebe_jogada(1,0)        #marca a jogada
        x = self.Jogo.verifica_ganhador()   #pega o resultado da função "verifica_ganhador" na classe "Jogo"
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if (x == 2) or (x == 1) or (x == 0):
            self.Jogo.limpa_jogadas()       #limpa tabuleiro
            self.limpa() 
        else:
            self.botao_4.configure(state="disabled")     #desativa o botão
            
    def bt5(self):                  #atividade do botão 5
        if self.Jogo.turno == 1:
            self.botao_5.configure(text = "X")           ##se o turno 1 selecionar o botão 5, marca X
        else:
            self.botao_5.configure(text = "O")           #se o turno 2 selecionar o botão 5, marca O
        if self.Jogo.rodada % 2 == 1:               #se a rodada for ímpar, X é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: X")
        else:                #se a rodada for par, O é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: O")
        self.Jogo.recebe_jogada(1,1)            #marca a jogada
        x = self.Jogo.verifica_ganhador()   #pega o resultado da função "verifica_ganhador" na classe "Jogo"
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if (x == 2) or (x == 1) or (x == 0):
            self.Jogo.limpa_jogadas()           #limpa tabuleiro
            self.limpa() 
        else:
            self.botao_5.configure(state="disabled")     #desativa o botão
            
    def bt6(self):                  #atividade do botão 6
        if self.Jogo.turno == 1:
            self.botao_6.configure(text = "X")               ##se o turno 1 selecionar o botão 6, marca X
        else:
            self.botao_6.configure(text = "O")               #se o turno 2 selecionar o botão 6, marca O
        if self.Jogo.rodada % 2 == 1:                   #se a rodada for ímpar, X é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: X")
        else:                    #se a rodada for par, O é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: O")
        self.Jogo.recebe_jogada(1,2)            #marca a jogada
        x = self.Jogo.verifica_ganhador()       #pega o resultado da função "verifica_ganhador" na classe "Jogo"
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if (x == 2) or (x == 1) or (x == 0):
            self.Jogo.limpa_jogadas()           #limpa tabuleiro
            self.limpa() 
        else:
            self.botao_6.configure(state="disabled")         #desativa o botão
        
    def bt7(self):              #atividade do botão 7
        if self.Jogo.turno == 1:
            self.botao_7.configure(text = "X")           ##se o turno 1 selecionar o botão 7, marca X
        else:
            self.botao_7.configure(text = "O")           #se o turno 2 selecionar o botão 7, marca O
        if self.Jogo.rodada % 2 == 1:               #se a rodada for ímpar, X é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: X")
        else:                #se a rodada for par, O é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: O")
        self.Jogo.recebe_jogada(2,0)            #marca a jogada
        x = self.Jogo.verifica_ganhador()       #pega o resultado da função "verifica_ganhador" na classe "Jogo"
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if (x == 2) or (x == 1) or (x == 0):
            self.Jogo.limpa_jogadas()           #limpa tabuleiro
            self.limpa()
        else:
            self.botao_7.configure(state="disabled")         #desativa o botão
            
    def bt8(self):                  #atividade do botão 8
        if self.Jogo.turno == 1:
            self.botao_8.configure(text = "X")               ##se o turno 1 selecionar o botão 8, marca X
        else:
            self.botao_8.configure(text = "O")               #se o turno 2 selecionar o botão 8, marca O
        if self.Jogo.rodada % 2 == 1:                   #se a rodada for ímpar, X é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: X")
        else:                        #se a rodada for par, O é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: O")
        self.Jogo.recebe_jogada(2,1)            #marca a jogada
        x = self.Jogo.verifica_ganhador()       #pega o resultado da função "verifica_ganhador" na classe "Jogo"
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if (x == 2) or (x == 1) or (x == 0):
            self.Jogo.limpa_jogadas()           #limpa tabuleiro
            self.limpa()  
        else:
            self.botao_8.configure(state="disabled")         #desativa o botão
        
    def bt9(self):          #atividade do botão 9
        if self.Jogo.turno == 1:
            self.botao_9.configure(text = "X")              ##se o turno 1 selecionar o botão 9, marca X
        else:
            self.botao_9.configure(text = "O")              #se o turno 2 selecionar o botão 9, marca O
        if self.Jogo.rodada % 2 == 1:                   #se a rodada for ímpar, X é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: X")
        else:                    #se a rodada for par, O é a próxima jogada
            self.proxima.configure(text = "Proxima jogada: O")
        self.Jogo.recebe_jogada(2,2)            #marca a jogada
        x = self.Jogo.verifica_ganhador()           #pega o resultado da função "verifica_ganhador" na classe "Jogo"
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if (x == 2) or (x == 1) or (x == 0):
            self.Jogo.limpa_jogadas()           #limpa tabuleiro
            self.limpa()   
        else:
            self.botao_9.configure(state="disabled")         #desativa o botão
    
    
    
t = tabuleiro()
t.iniciar()
