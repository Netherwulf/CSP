import numpy as np


class CSP(object):
    def __init__(self, forward_checking=False, size=5, choose_random_color=False, choose_vertical_variable=False):
        self.forward_checking = forward_checking
        self.size = size
        self.color_matrix = np.zeros((self.size, self.size), int)
        self.domain = np.arange(2) + 1
        self.chosen_colors_matrix = np.zeros([self.size, self.size, self.domain.size], dtype=int)
        self.choose_random_color = choose_random_color
        self.choose_vertical_variable = choose_vertical_variable
        self.step_number = 0
        self.return_number = 0
        # POSZUKAC JAK UTWORZYC TABELE DWUWYMIAROWA Z TABELAMI W KAZDEJ KMORCE (TAKA SAMA TABELA W KAZDEJ KOMORCE)
        pass

    def validate(self, row, column, value):
        # sprawdzanie wartości na sąsiednich polach w pionie
        if (self.size - 1) > row > 0:
            if np.absolute(self.color_matrix[row - 1][column] - value) < 2 or np.absolute(
                    self.color_matrix[row + 1][column] - value) < 2:
                return False
        if row == (self.size - 1):
            if np.absolute(self.color_matrix[row - 1][column] - value) < 2:
                return False
        if row == 0:
            if np.absolute(self.color_matrix[row + 1][column] - value) < 2:
                return False
        # sprawdzenie wartości na sąsiednich polach w poziomie
        if (self.size - 1) > column > 0:
            if np.absolute(self.color_matrix[row][column - 1] - value) < 2 or np.absolute(
                    self.color_matrix[row][column + 1] - value) < 2:
                return False
        if column == self.size - 1:
            if np.absolute(self.color_matrix[row][column - 1] - value) < 2:
                return False
        if column == 0:
            if np.absolute(self.color_matrix[row][column + 1] - value) < 2:
                return False
        # sprawdzenie po skosie
        if row > 0 and column > 0:
            if np.absolute(self.color_matrix[row - 1][column - 1] - value) < 1:
                return False
        if row < self.size - 1 and column < self.size - 1:
            if np.absolute(self.color_matrix[row + 1][column + 1] - value) < 1:
                return False
        return True

    def solve_graph_colorization_backtracking(self):
        row = 0
        column = 0
        while row < self.size:
            while column < self.size:
                # print("Domena: " + str(self.domain))
                # print("Wybrane kolory" + str(self.chosen_colors_matrix[0][0]))
                print("Wiersz: " + str(row) + " Kolumna: " + str(column))
                for color in np.setdiff1d(self.domain, self.chosen_colors_matrix[row][column]):
                    self.chosen_colors_matrix[row][column][color-1] = color
                    if self.validate(row, column, color):
                        self.color_matrix[row][column] = color
                        break
                if self.color_matrix[row][column] == 0:
                    if column >= 1:
                        column -= 2
                    else:
                        row -= 2
                        column = self.size-1
                        break
                column += 1
            if row == 0 and np.array_equal(self.domain, self.chosen_colors_matrix[0][0]):
                print("Nie udało się rozwiązać dla dziedziny: " + str(self.domain))
                self.domain = np.append(self.domain, self.domain.size+1)
                self.chosen_colors_matrix[0][0] = np.zeros(self.domain.size)
            else:
                row += 1
        print(self.color_matrix)
