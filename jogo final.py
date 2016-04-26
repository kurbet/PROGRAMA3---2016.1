import tkinter
import random
from itertools import permutations

class Player:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.selected_sq = set()

class Tabuleiro:
    """
    Cria o tabuleiro

    Atributos:
    sq_size: define o tamanho dos quadrados
    color: codigo de cores
    """

    def __init__(self, parent, sq_size, color):
        self.parent = parent   
        self.sq_size = sq_size
        self.color = color

        # define as sequencias vencedoras na matriz
        self._winning_combos = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},
                      {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
                      {1, 5, 9}, {3, 5, 7}]

        # define o tabuleiro p o tkinter
        self.unused_squares_dict = { '00': 1, '10': 2, '20': 3,
                                     '01': 4, '11': 5, '21': 6,
                                     '02': 7, '12': 8, '22': 9  }

        # cria o tabuleiro no tkinter
        self.container = tkinter.Frame(self.parent)
        self.container.pack()

        # uso do canvas p criar cada quadrado do tabuleiro
        self.canvas = tkinter.Canvas(self.container,
                                     width= self.sq_size * 3,
                                     height= self.sq_size * 3)
        # define o canvas
        self.canvas.grid()
        
        #quadrados n utilizados
    def get_unused_squares_dict(self):
        return self.unused_squares_dict
        
        # reseta os quadrados n utilizados
    def reset_unused_squares_dict(self):
        self.unused_squares_dict = { '00': 1, '10': 2, '20': 3,
                                     '01': 4, '11': 5, '21': 6,
                                     '02': 7, '12': 8, '22': 9  }
     # desenha o tabuleiro                                
    def draw_board(self):
        for row in range(3):
            for column in range(3):
                self.canvas.create_rectangle(self.sq_size  * column,
                                        self.sq_size  * row,
                                        self.sq_size  * (column + 1),
                                        self.sq_size  * (row + 1),
                                        fill = self.color)

    def get_row_col(self, evt):
        # pega a linha e coluna de cada evento em x e y
        return evt.x, evt.y

    def floor_of_row_col(self, col, rw):
       
        col_flr = col // self.sq_size
        rw_flr = rw // self.sq_size
        return col_flr, rw_flr
        #transforma a coluna e linha selecionada em string
    def convert_to_key(self, col_floor, row_floor):
        return str(col_floor) + str(row_floor)

    def find_coords_of_selected_sq(self, evt):
        # salva a coluna e linha em 2 variaveis
        column, row = self.get_row_col(evt)
        column_floor, row_floor = self.floor_of_row_col(column, row)
        # define aonde do tabuleiro estará o clique
        rowcol_key_str = self.convert_to_key(column_floor, row_floor)
        corner_column = (column_floor * self.sq_size) + self.sq_size
        corner_row =  (row_floor  * self.sq_size) + self.sq_size
        print("rowcol_key_str: " + str(rowcol_key_str))
        return corner_column, corner_row
        
    # define a cor dos quadrados
    def color_selected_sq(self, evt, second_corner_col,
                          second_corner_row, player_color):

        print(" ---- inside color_selected_sq method ----")
        self.canvas.create_rectangle(
            (evt.x // self.sq_size) * self.sq_size,
            (evt.y // self.sq_size) * self.sq_size,
            second_corner_col,
            second_corner_row,
            fill = player_color)

    @property
    # define as posicoes que vencem o jogo
    def winning_combos(self):
        return self._winning_combos

class Jogo(object):
    """
    Controla o tabuleiro e os jogadores

    Atributos:
    parent: janela do tkinter
    board: tabuleiro do jogo
    unused_squares_dict:monitora os quadrados n usados ainda
    player1: cuida da classe player(no caso P1)
    player2: cuida da classe player(no caso P2)
    """

    def __init__(self, parent):
        self.parent = parent  

        # cria o tabuleiro
        self.board = Tabuleiro(self.parent, 100, "#ECECEC")  # cor do tabuleiro cinza
        self.board.draw_board()

        self.unused_squares_dict = self.board.get_unused_squares_dict()

        # Cria os jogadores
        self.player1 = Player("Player 1", "#446CB3") # jogador 1 é azul
        self.player2 = Player("Player 2", "#F4D03F") # jogador 2 é amarelo


        self.initialize_buttons()
        # cria um menu
        self.show_menu()
        # botoes inicias
    def initialize_buttons(self):
        #  --- cria os botoes p o menu ---
        
        self.two_players_button = tkinter.Button(self.board.container,
                                text = "JOGAR(o Azul começa)",
                                width = 25,
                                command = self.init_two_players_game)# botao JOGAR

       
        

        self.reset_button = tkinter.Button(self.board.container,
                                           text = "RESET",
                                           width = 25,
                                           command = self.limpa_jogadas)#botao RESET
   

    def show_menu(self):
         # adiciona os botoes ao tabuleiro
        self.two_players_button.grid()

    #define o jogo p 2 jogadores
    def init_two_players_game(self):
        # reseta o tabuleiro
        self.board.reset_unused_squares_dict()
        # reseta as escolhas anteriores dos jogadores
        self.player1.selected_sq = set()
        self.player2.selected_sq = set()
        # checa os turnos
        self.player1_turn = True
        # mostra botao de reset
        self.reset_button.grid()
        #bota p jogar
        self.board.canvas.bind("<Button-1>", self.recebe_jogada)
    # funcao p resetar o jogo
    def limpa_jogadas(self):
        self.board.container.destroy()
        # cria novo tabuleiro e botoes
        self.board = Tabuleiro(self.parent, 100, "#ECECEC")# define tamanho e cor do tabuleiro
        self.board.draw_board()
        self.initialize_buttons()
        self.show_menu()
        
        #adiciona o jogador
    def add_to_player_sq(self, key, player_sq):
        current_selected_sq = self.board.unused_squares_dict[key]
        print("current selected sq  ---->", current_selected_sq)
        print("BEFORE player selected_sq: ", player_sq)
        player_sq.add(current_selected_sq)   # player 1 = {1}
        print("AFTER player selected_sq: ", player_sq)
        
        #modifica o quadrado n usado pela cor do jogador
    def delete_used_sq(self, key):
        print(" ---- square to delete ---: ", self.board.unused_squares_dict[key])
        print("unused squares dictionary before: ", self.board.unused_squares_dict)
        del self.board.unused_squares_dict[key]
        print("unused squares dictionary after: ", self.board.unused_squares_dict)
        
        #funcao jogar
    def recebe_jogada(self, event):
        # localiza a linha e coluna que o jogador clicou
        colrow_tuple = self.board.find_coords_of_selected_sq(event)
        # salva a linha e coluna como variavel
        corner_two_col, corner_two_row = colrow_tuple[0], colrow_tuple[1]
        # calcula quais quadrados ainda estao disponiveis p jogar
        col_fl, row_fl = self.board.floor_of_row_col(event.x, event.y)
        rowcol_key = self.board.convert_to_key(col_fl, row_fl)

        try:
            self.unused_squares_dict[rowcol_key]
        except KeyError:
            return

        if self.player1_turn == True:
            self.add_to_player_sq(rowcol_key, self.player1.selected_sq)

            # deleta do jogo um dicionario n utilizado
            self.delete_used_sq(rowcol_key)

            self.board.color_selected_sq(event,
                                   corner_two_col,
                                   corner_two_row,
                                   self.player1.color)

            # checa se foi vitoria do P1,P2 ou empate
            self.verifica_ganhador(self.player1.selected_sq, self.player1.name)

            # muda de turno
            self.player1_turn = False

        else:  # rodada do P2
            self.board.color_selected_sq(event,
                                   corner_two_col,
                                   corner_two_row,
                                   self.player2.color)

            self.add_to_player_sq(rowcol_key, self.player2.selected_sq)
            self.delete_used_sq(rowcol_key)
            self.verifica_ganhador(self.player2.selected_sq, self.player2.name)
            self.player1_turn = True
    # checa o vencedor
    def verifica_ganhador(self, player_sq, player_name):

        if len(self.board.unused_squares_dict) > 0:
            # caso jogador tenha escolhido ao minimo 3 quadrados
            if len(player_sq) > 2:
                # checa sobre estes 3 quadrados
                for combo in permutations(player_sq, 3):
                    
                    for wc in self.board.winning_combos:
                        if set(combo) == wc :
                            self.show_game_result(" Vitoria do " + player_name+ "!")
                            self.limpa_jogadas

        if len(self.board.unused_squares_dict) == 0:
            self.show_game_result("Poxa é empate")
            self.limpa_jogadas
    #mostra quem venceu o jogo
    def show_game_result(self, txt):
        
        # label do resultado do jogo
        result_label = tkinter.Label(self.board.container,
                                            text= txt,
                                            width = 32,
                                            height = 10,
                                            foreground = "red",
                                            background = "gray",
                                            borderwidth = 3)

        result_label.grid(row = 0, column = 0)
        
        self.board.canvas.unbind("<Button-1>", self.recebe_jogada)

def main():
    root = tkinter.Tk()
    root.title("Jogo da Velha")
    tictac_game = Jogo(root)  # root is parent
    root.mainloop()

if __name__ == '__main__':
    main()