import numpy as np


class CSP(object):
    def __init__(self, size=5, choose_random_color=False, choose_vertical_variable=False):
        self.size = size
        self.color_matrix = np.zeros((self.size, self.size), int)
        self.domain = np.arange(6) + 1
        self.chosen_colors_matrix = np.zeros([self.size, self.size, self.domain.size], dtype=int)
        self.available_domains = np.array([np.array([self.domain for i in range(self.size)]) for j in range(self.size)])
        self.choose_random_color = choose_random_color
        self.choose_vertical_variable = choose_vertical_variable
        self.step_number = 0
        self.recurrence_number = 0
        self.domain_change = False
        # POSZUKAC JAK UTWORZYC TABELE DWUWYMIAROWA Z TABELAMI W KAZDEJ KMORCE (TAKA SAMA TABELA W KAZDEJ KOMORCE)
        pass

    def validate(self, row, column, value):
        # sprawdzanie wartości na sąsiednich polach w pionie
        if (self.size - 1) > row > 0:
            if (np.absolute(self.color_matrix[row - 1][column] - value) < 2 and self.color_matrix[row - 1][column] != 0) or (np.absolute(
                    self.color_matrix[row + 1][column] - value) < 2 and self.color_matrix[row + 1][column] != 0):
                # print("Zła wartość w pionie")
                return False
        # dla ostatniego rzędu
        if row == (self.size - 1):
            if np.absolute(self.color_matrix[row - 1][column] - value) < 2 and self.color_matrix[row - 1][column] != 0:
                # print("Zła wartość w pionie dla ostatniego rzędu")
                return False
        # dla pierwszego rzędu
        if row == 0:
            if np.absolute(self.color_matrix[row + 1][column] - value) < 2 and self.color_matrix[row + 1][column] != 0:
                # print("Zła wartość w pionie dla pierwszego rzędu")
                return False
        # sprawdzenie wartości na sąsiednich polach w poziomie
        if (self.size - 1) > column > 0:
            if (np.absolute(self.color_matrix[row][column - 1] - value) < 2 and self.color_matrix[row][column - 1] != 0) or (np.absolute(
                    self.color_matrix[row][column + 1] - value) < 2 and self.color_matrix[row][column + 1] != 0):
                # print("Zła wartość w poziomie")
                return False
        # dla ostatniej kolumny
        if column == self.size - 1:
            if np.absolute(self.color_matrix[row][column - 1] - value) < 2 and self.color_matrix[row][column - 1] != 0:
                # print("Zła wartość w poziomie dla ostatniej kolumny")
                return False
        # dla pierwszej kolumny
        if column == 0:
            if np.absolute(self.color_matrix[row][column + 1] - value) < 2 and self.color_matrix[row][column + 1] != 0:
                # print("Zła wartość w poziomie dla pierwszej kolumny")
                return False
        # sprawdzenie po skosie
        # lewy górny
        if row > 0 and column > 0:
            if np.absolute(self.color_matrix[row - 1][column - 1] - value) < 1 and self.color_matrix[row - 1][column - 1] != 0:
                # print("Zła wartość po skosie - lewy górny")
                return False
        # lewy dolny
        if row < self.size-1 and column > 0:
            if np.absolute(self.color_matrix[row + 1][column - 1] - value) < 1 and self.color_matrix[row + 1][column - 1] != 0:
                # print("Zła wartość po skosie - lewy dolny")
                return False
        # prawy górny
        if row > 0 and column < self.size - 1:
            if np.absolute(self.color_matrix[row - 1][column + 1] - value) < 1 and self.color_matrix[row - 1][column + 1] != 0:
                # print("Zła wartość po skosie - prawy górny")
                return False
        # prawy dolny
        if row < self.size - 1 and column < self.size - 1:
            if np.absolute(self.color_matrix[row + 1][column + 1] - value) < 1 and self.color_matrix[row + 1][column + 1] != 0:
                # print("Zła wartość po skosie - prawy dolny")
                return False
        return True

    row = 0
    column = 0
    change = False

    def backtracking_map_horizontal(self):
        global row
        row = 0
        global column
        column = 0
        global change
        change = False
        while row < self.size:
            while column < self.size:
                change = False
                # print("Wiersz: " + str(row) + " Kolumna: " + str(column))
                # print("Dziedzina: " + str(self.domain))
                # print("Wybrane kolory: " + str(self.chosen_colors_matrix[row][column]))
                for color in np.setdiff1d(self.domain, self.chosen_colors_matrix[row][column]):
                    self.chosen_colors_matrix[row][column][color-1] = color
                    if self.validate(row, column, color):
                        # print("Dobry kolor dla: " + str(row) + " " + str(column) + " kolor: " + str(color))
                        change = True
                        self.step_number += 1
                        self.color_matrix[row][column] = color
                        break
                if self.color_matrix[row][column] == 0 or change is False:
                    # print("Nawrót dla: " + str(row) + " " + str(column))
                    self.recurrence_number += 1
                    self.chosen_colors_matrix[row][column] = np.zeros(self.domain.size, dtype=int)
                    if row == 0 and column == 0:
                        print("Nie udało się rozwiązać dla dziedziny: " + str(self.domain))
                        self.domain = np.append(self.domain, self.domain.size + 1)
                        self.domain_change = True
                        self.chosen_colors_matrix = np.zeros([self.size, self.size, self.domain.size], dtype=int)
                        column -= 1
                    else:
                        if column >= 1:
                            column -= 2
                        else:
                            if column == 0:
                                row -= 1
                                column = self.size - 2
                column += 1
            row += 1
            column = 0
        print(self.color_matrix)
        print("Dziedzina: " + str(self.domain))
        print("Ilość kroków: " + str(self.step_number))
        print("Ilość nawrotów: " + str(self.recurrence_number))
        print("Dziedzina BYLA zmieniana" if self.domain_change else "Dziedzina NIE była zmieniana")

    def validate_domains(self, row, column, value):
        if value != 0:
            # aktualizacja dziedzin na sąsiednich polach w pionie
            if (self.size - 1) > row > 0:
                for i in range(self.domain.size):
                    if np.absolute(self.available_domains[row - 1][column][i] - value) < 2:
                        self.available_domains[row - 1][column][i] = 0
                    if np.absolute(self.available_domains[row + 1][column][i] - value) < 2:
                        self.available_domains[row + 1][column][i] = 0
                # print("Zła wartość w pionie")
            # dla ostatniego rzędu
            if row == (self.size - 1):
                for i in range(self.domain.size):
                    if np.absolute(self.available_domains[row - 1][column][i] - value) < 2:
                        self.available_domains[row - 1][column][i] = 0
                    # print("Zła wartość w pionie dla ostatniego rzędu")
            # dla pierwszego rzędu
            if row == 0:
                for i in range(self.domain.size):
                    if np.absolute(self.available_domains[row + 1][column][i] - value) < 2:
                        self.available_domains[row + 1][column][i] = 0
                # print("Zła wartość w pionie dla pierwszego rzędu")
            # sprawdzenie wartości na sąsiednich polach w poziomie
            if (self.size - 1) > column > 0:
                for i in range(self.domain.size):
                    if np.absolute(self.available_domains[row][column - 1][i] - value) < 2:
                        self.available_domains[row][column - 1][i] = 0
                    if np.absolute(self.available_domains[row][column + 1][i] - value) < 2:
                        self.available_domains[row][column + 1][i] = 0
                # print("Zła wartość w poziomie")
            # dla ostatniej kolumny
            if column == self.size - 1:
                for i in range(self.domain.size):
                    if np.absolute(self.available_domains[row][column - 1][i] - value) < 2:
                        self.available_domains[row][column - 1][i] = 0
                # print("Zła wartość w poziomie dla ostatniej kolumny")
            # dla pierwszej kolumny
            if column == 0:
                for i in range(self.domain.size):
                    if np.absolute(self.available_domains[row][column + 1][i] - value) < 2:
                        self.available_domains[row][column + 1][i] = 0
                # print("Zła wartość w poziomie dla pierwszej kolumny")
            # sprawdzenie po skosie
            # lewy górny
            if row > 0 and column > 0:
                for i in range(self.domain.size):
                    if np.absolute(self.available_domains[row - 1][column - 1][i] - value) < 1:
                        self.available_domains[row - 1][column - 1][i] = 0
                # print("Zła wartość po skosie - lewy górny")
            # lewy dolny
            if row < self.size - 1 and column > 0:
                for i in range(self.domain.size):
                    if np.absolute(self.available_domains[row + 1][column - 1][i] - value) < 1:
                        self.available_domains[row + 1][column - 1][i] = 0
                # print("Zła wartość po skosie - lewy dolny")
            # prawy górny
            if row > 0 and column < self.size - 1:
                for i in range(self.domain.size):
                    if np.absolute(self.available_domains[row - 1][column + 1][i] - value) < 1:
                        self.available_domains[row - 1][column + 1][i] = 0
                # print("Zła wartość po skosie - prawy górny")
            # prawy dolny
            if row < self.size - 1 and column < self.size - 1:
                for i in range(self.domain.size):
                    if np.absolute(self.available_domains[row + 1][column + 1][i] - value) < 1:
                        self.available_domains[row + 1][column + 1][i] = 0
                # print("Zła wartość po skosie - prawy dolny")

    def forward_checking_map_horizontal(self):
        global row
        row = 0
        global column
        column = 0
        global change
        change = False
        while row < self.size:
            while column < self.size:
                change = False
                print("Wiersz: " + str(row) + " Kolumna: " + str(column))
                # print("Dziedzina: " + str(self.domain))
                # print("Wybrane kolory: " + str(self.chosen_colors_matrix[row][column]))
                for color in np.setdiff1d(np.setdiff1d(self.available_domains[row][column], np.zeros(self.domain.size, dtype=int)), self.chosen_colors_matrix[row][column]):
                    self.chosen_colors_matrix[row][column][color-1] = color
                    # print("Dobry kolor dla: " + str(row) + " " + str(column) + " kolor: " + str(color))
                    change = True
                    self.step_number += 1
                    self.color_matrix[row][column] = color
                    # aktualizacja dziedzin innych pól
                    for i in range(row + 1):
                        for j in range(column + 1):
                            self.validate_domains(i, j, self.color_matrix[i][j])
                    break
                if self.color_matrix[row][column] == 0 or change is False:
                    # print("Nawrót dla: " + str(row) + " " + str(column))
                    self.recurrence_number += 1
                    self.chosen_colors_matrix[row][column] = np.zeros(self.domain.size, dtype=int)
                    self.color_matrix[row][column] = 0
                    for i in range(row + 1):
                        for j in range(column + 1):
                            self.validate_domains(i, j, self.color_matrix[i][j])
                    if row == 0 and column == 0:
                        print("Nie udało się rozwiązać dla dziedziny: " + str(self.domain))
                        self.domain = np.append(self.domain, self.domain.size + 1)
                        self.domain_change = True
                        self.chosen_colors_matrix = np.zeros([self.size, self.size, self.domain.size], dtype=int)
                        self.available_domains = np.array(
                            [np.array([self.domain for i in range(self.size)]) for j in range(self.size)])
                        column -= 1
                    else:
                        if column >= 1:
                            column -= 2
                        else:
                            if column == 0:
                                row -= 1
                                column = self.size - 2
                column += 1
            row += 1
            column = 0
        print(self.color_matrix)
        print("Dziedzina: " + str(self.domain))
        print("Ilość kroków: " + str(self.step_number))
        print("Ilość nawrotów: " + str(self.recurrence_number))
        print("Dziedzina BYLA zmieniana" if self.domain_change else "Dziedzina NIE była zmieniana")
