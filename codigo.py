# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 16:39:10 2016

@author: andre_000
"""

from numpy import zeros      #importa zeros para futuramente criar a matriz

class Jogo():
    """ Classe que cria o jogo da velha no tabuleiro vindo de outra classe!
        
        1 = X
        2 = O
        
    """
    
    def __init__(self,matriz,turno):            #construtor
        self.matriz = zeros((3,3))      #cria a matriz 3 por 3
        self.turno = 1          #cria os turnos e começa com 1(O)
        
    def recebe_jogada(self,linha,coluna):
        if self.turno == 1:         #saber quem ta jogando
            self.matriz[linha][coluna] = 1      #marca 1(O) na matriz
            self.turno = 2          #alterna turno
        elif self.turno == 2:       #saber quem ta jogando
            self.matriz[linha][coluna] = 2      #marca 2(X) na matriz
            self.turno = 1          #alterna turno
        
    def verifica_ganhador(self):
        linha_0 = 0
        linha_1 = 0
        linha_2 = 0
        coluna_0 = 0
        coluna_1 = 0
        coluna_2 = 0
        diagonal_prin = 0
        diagonal_secu = 0
        
        """Linha 0"""
        linha_0 += self.matriz[0][0]
        linha_0 += self.matriz[0][1]
        linha_0 += self.matriz[0][2]
        """Linha 1"""
        linha_1 += self.matriz[1][0]
        linha_1 += self.matriz[1][1]
        linha_1 += self.matriz[1][2]
        """Linha 2"""
        linha_2 += self.matriz[2][0]
        linha_2 += self.matriz[2][1]
        linha_2 += self.matriz[2][2]
        """Coluna 0"""
        coluna_0 += self.matriz[0][0]
        coluna_0 += self.matriz[1][0]
        coluna_0 += self.matriz[2][0]
        """Coluna 1"""
        coluna_1 += self.matriz[0][1]
        coluna_1 += self.matriz[1][1]
        coluna_1 += self.matriz[2][1]
        """Coluna 2"""
        coluna_2 += self.matriz[0][2]
        coluna_2 += self.matriz[1][2]
        coluna_2 += self.matriz[2][2]
        """Diagonal Principal"""
        diagonal_prin += self.matriz[0][0]
        diagonal_prin += self.matriz[1][1]
        diagonal_prin += self.matriz[2][2]
        """Diagonal Secundária"""
        diagonal_secu += self.matriz[2][0]
        diagonal_secu += self.matriz[1][1]
        diagonal_secu += self.matriz[0][2]
            
        """Bolinha ganhou..."""
        if (linha_0==6) or (linha_1==6) or (linha_2==6) or (coluna_0==6) or (coluna_1==6) or (coluna_2==6) or (diagonal_prin==6) or (diagonal_secu==6):
            return 2
        
        """X ganhou..."""
        if (linha_0==3) or (linha_1==3) or (linha_2==3) or (coluna_0==3) or (coluna_1==3) or (coluna_2==3) or (diagonal_prin==3) or (diagonal_secu==3):
            return 1
        
        """Empate..."""
        if (linha_0==4 or 5) or (linha_1==4 or 5) or (linha_2==4 or 5) or (coluna_0==4 or 5) or (coluna_1==4 or 5) or (coluna_2==4 or 5) or (diagonal_prin==4 or 5) or (diagonal_secu==4 or 5):
            return 0
            
        """Caso contrário..."""
        if (linha_0==0 or 1 or 2) or (linha_1==0 or 1 or 2) or (linha_2==0 or 1 or 2) or (coluna_0==0 or 1 or 2) or (coluna_1==0 or 1 or 2) or (coluna_2==0 or 1 or 2) or (diagonal_prin==0 or 1 or 2) or (diagonal_secu==0 or 1 or 2):
            return -1
            
    
    def limpa_jogadas(self):            #recomeça do "zero"
        self.matriz = zeros((3,3))
        self.turno = 1