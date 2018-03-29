import numpy as np


class CSP(object):
    def __init__(self, forward_checking=False, size=5, choose_random_color=False, choose_vertical_variable=False):
        self.forward_checking=forward_checking
        self.size=size
        self.color_matrix=np.empty((size, size), int)
        self.chosen_color_matrix = #macierz kolorów jakie już były wybrane
        self.choose_random_color=choose_random_color
        self.choose_vertical_variable=choose_vertical_variable
        self.step_number=0
        self.return_number=0
        self.domain=np.arrange(size)
        #POSZUKAC JAK UTWORZYC TABELE DWUWYMIAROWA Z TABELAMI W KAZDEJ KMORCE (TAKA SAMA TABELA W KAZDEJ KOMORCE)
        pass

    #DOPISAC WARTOSC BEZWZGLEDNA W SPRAWDZANIU ROZNICY
    def validate(self, row, column, value):
        #sprawdzanie wartości na sąsiednich polach w pionie
        if (self.size-1)>row>0:
            if self.color_matrix[row-1][column] - value < 2 or self.color_matrix[row+1][column] - value < 2:
                return False
        if row==(self.size-1):
            if self.color_matrix[row-1][column] - value < 2:
                return False
        if row==0:
            if self.color_matrix[row+1][column] - value < 2:
                return False
        #sprawdzenie wartości na sąsiednich polach w poziomie
        if (self.size-1)>column>0:
            if self.color_matrix[row][column-1] - value < 2 or self.color_matrix[row][column+1] - value < 2:
                return False
        if column==self.size-1:
            if self.color_matrix[row][column-1] - value < 2:
                return False
        if column==0:
            if self.color_matrix[row][column+1] - value < 2:
                return False
        #sprawdzenie po skosie
        if row>0 and column>0:
            if self.color_matrix[row-1][column-1] - value < 1:
                return False
        if row<self.size-1 and column<self.size-1:
            if self.color_matrix[row+1][column+1] - value < 1:
                return False

    def solve_graph_colorization_backtracking(self):
        for row in range(self.size):
            for column in range(self.size):


