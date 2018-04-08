import numpy as np
import time


class CSP(object):
    def __init__(self, size=5, domain_size=5):
        self.size = size
        self.color_matrix = np.zeros((self.size, self.size), int)
        self.domain = np.arange(domain_size) + 1
        self.chosen_colors_matrix = np.zeros([self.size, self.size, self.domain.size], dtype=int)
        self.available_domains = np.array([np.array([self.domain for i in range(self.size)]) for j in range(self.size)])
        self.domain_history = np.array([self.available_domains])
        self.step_number = 0
        self.recurrence_number = 0
        self.domain_change = False
        pass

########################################################################################################################
# --------------------------------------------- KOLOROWANIE GRAFU ------------------------------------------------------
########################################################################################################################

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

    row = 0
    column = 0
    change = False

    def backtracking_map(self, choose_random_color=False):
        start_time = time.time()
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
                color_set = np.setdiff1d(self.domain, self.chosen_colors_matrix[row][column])
                if choose_random_color is True:
                    np.random.shuffle(color_set)
                for color in color_set:
                    self.chosen_colors_matrix[row][column][color-1] = color
                    if self.validate(row, column, color):
                        # print("Dobry kolor dla: " + str(row) + " " + str(column) + " kolor: " + str(color))
                        change = True
                        self.step_number += 1
                        self.color_matrix[row][column] = color
                        break
                if self.color_matrix[row][column] == 0 or change is False:
                    # print("Nawrót dla: " + str(row) + " " + str(column))
                    self.color_matrix[row][column] = 0
                    self.recurrence_number += 1
                    self.chosen_colors_matrix[row][column] = np.zeros(self.domain.size, dtype=int)
                    if row == 0 and column == 0:
                        print("Nie udało się rozwiązać dla dziedziny: " + str(self.domain))
                        self.color_matrix = np.zeros((self.size, self.size), int)
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
        print("Czas wykonania: " + "%s sekund" % (time.time() - start_time))
        print("Dziedzina BYLA zmieniana" if self.domain_change else "Dziedzina NIE była zmieniana")
        return (time.time() - start_time), self.step_number, self.recurrence_number

    def forward_checking_map(self, choose_random_color=False):
        start_time = time.time()
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
                color_set = np.setdiff1d(np.setdiff1d(self.available_domains[row][column], np.zeros(self.domain.size, dtype=int)), self.chosen_colors_matrix[row][column])
                if choose_random_color is True:
                    np.random.shuffle(color_set)
                for color in color_set:
                    self.chosen_colors_matrix[row][column][color-1] = color
                    # print("Dobry kolor dla: " + str(row) + " " + str(column) + " kolor: " + str(color))
                    change = True
                    self.step_number += 1
                    self.color_matrix[row][column] = color
                    # zapamiętanie aktualnego stanu dziedzin sprzed zmiany koloru
                    self.domain_history = np.append(self.domain_history, [self.available_domains], axis=0)
                    # aktualizacja dziedzin
                    self.validate_domains(row, column, self.color_matrix[row][column])
                    break
                if self.color_matrix[row][column] == 0 or change is False:
                    # Wykonanie nawrotu
                    # print("Nawrót dla: " + str(row) + " " + str(column))
                    self.recurrence_number += 1
                    self.chosen_colors_matrix[row][column] = np.zeros(self.domain.size, dtype=int)
                    self.color_matrix[row][column] = 0
                    # Aktualizacja domen do stanu sprzed ustawienia wartości
                    self.available_domains = self.domain_history[-1]
                    self.domain_history = np.delete(self.domain_history, -1, 0)
                    if row == 0 and column == 0:
                        # Odkrycie, że nie ma rozwiazan dla zadanej dziedziny i dodanie do niej kolejnej wartości
                        print("Nie udało się rozwiązać dla dziedziny: " + str(self.domain))
                        self.color_matrix = np.zeros((self.size, self.size), int)
                        self.domain = np.append(self.domain, self.domain.size + 1)
                        self.domain_change = True
                        self.chosen_colors_matrix = np.zeros([self.size, self.size, self.domain.size], dtype=int)
                        self.available_domains = np.array(
                            [np.array([self.domain for i in range(self.size)]) for j in range(self.size)])
                        column -= 1
                        self.domain_history = np.array([self.available_domains])
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
        print("Czas wykonania: " + "%s sekund" % (time.time() - start_time))
        print("Dziedzina BYLA zmieniana" if self.domain_change else "Dziedzina NIE była zmieniana")
        return (time.time() - start_time), self.step_number, self.recurrence_number

########################################################################################################################
# --------------------------------------------- KWADRAT LACINSKI -------------------------------------------------------
########################################################################################################################

    def validate_latin(self, row, column, value):
        # sprawdzanie unikalności wartości w kolumnie
        if value in self.color_matrix[:, column]:
            # print("Powtarzajaca się wartość w kolumnie")
            return False
        # sprawdzanie unikalności wartości w wierszu
        if value in self.color_matrix[row, :]:
            # print("Powtarzajaca się wartość w wierszu")
            return False
        return True

    def validate_domains_latin(self, row, column, value):
        if value != 0:
            # aktualizacja dziedzin pól w kolumnie
            for row_number in range(self.size):
                for i in range(self.domain.size):
                    if self.available_domains[row_number][column][i] in self.color_matrix[:, column]:
                        self.available_domains[row_number][column][i] = 0
                        # print("Powtarzajaca sie wartość w kolumnie")
            # aktualizacja dziedzin pól w wierszu
            for column_number in range(self.size):
                for i in range(self.domain.size):
                    if self.available_domains[row][column_number][i] in self.color_matrix[row, :]:
                        self.available_domains[row][column_number][i] = 0
                        # print("Powtarzajaca sie wartość w kolumnie")

    def backtracking_latin(self, choose_random_color=False):
        start_time = time.time()
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
                color_set = np.setdiff1d(self.domain, self.chosen_colors_matrix[row][column])
                if choose_random_color is True:
                    np.random.shuffle(color_set)
                for color in color_set:
                    self.chosen_colors_matrix[row][column][color-1] = color
                    if self.validate_latin(row, column, color):
                        # print("Dobry kolor dla: " + str(row) + " " + str(column) + " kolor: " + str(color))
                        change = True
                        self.step_number += 1
                        self.color_matrix[row][column] = color
                        break
                if self.color_matrix[row][column] == 0 or change is False:
                    # print("Nawrót dla: " + str(row) + " " + str(column))
                    self.color_matrix[row][column] = 0
                    self.recurrence_number += 1
                    self.chosen_colors_matrix[row][column] = np.zeros(self.domain.size, dtype=int)
                    if row == 0 and column == 0:
                        print("Nie udało się rozwiązać dla dziedziny: " + str(self.domain))
                        self.color_matrix = np.zeros((self.size, self.size), int)
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
        print("Czas wykonania: " + "%s sekund" % (time.time() - start_time))
        print("Dziedzina BYLA zmieniana" if self.domain_change else "Dziedzina NIE była zmieniana")
        return (time.time() - start_time), self.step_number, self.recurrence_number

    def forward_checking_latin(self, choose_random_color=False):
        start_time = time.time()
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
                color_set = np.setdiff1d(np.setdiff1d(self.available_domains[row][column], np.zeros(self.domain.size, dtype=int)), self.chosen_colors_matrix[row][column])
                if choose_random_color is True:
                    np.random.shuffle(color_set)
                for color in color_set:
                    self.chosen_colors_matrix[row][column][color-1] = color
                    # print("Dobry kolor dla: " + str(row) + " " + str(column) + " kolor: " + str(color))
                    change = True
                    self.step_number += 1
                    self.color_matrix[row][column] = color
                    # zapamiętanie aktualnego stanu dziedzin sprzed zmiany koloru
                    self.domain_history = np.append(self.domain_history, [self.available_domains], axis=0)
                    # aktualizacja dziedzin
                    self.validate_domains_latin(row, column, self.color_matrix[row][column])
                    break
                if self.color_matrix[row][column] == 0 or change is False:
                    # Wykonanie nawrotu
                    # print("Nawrót dla: " + str(row) + " " + str(column))
                    self.recurrence_number += 1
                    self.chosen_colors_matrix[row][column] = np.zeros(self.domain.size, dtype=int)
                    self.color_matrix[row][column] = 0
                    # Aktualizacja domen do stanu sprzed ustawienia wartości
                    self.available_domains = self.domain_history[-1]
                    self.domain_history = np.delete(self.domain_history, -1, 0)
                    if row == 0 and column == 0:
                        # Odkrycie, że nie ma rozwiazan dla zadanej dziedziny i dodanie do niej kolejnej wartości
                        print("Nie udało się rozwiązać dla dziedziny: " + str(self.domain))
                        self.color_matrix = np.zeros((self.size, self.size), int)
                        self.domain = np.append(self.domain, self.domain.size + 1)
                        self.domain_change = True
                        self.chosen_colors_matrix = np.zeros([self.size, self.size, self.domain.size], dtype=int)
                        self.available_domains = np.array(
                            [np.array([self.domain for i in range(self.size)]) for j in range(self.size)])
                        column -= 1
                        self.domain_history = np.array([self.available_domains])
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
        print("Czas wykonania: " + "%s sekund" % (time.time() - start_time))
        print("Dziedzina BYLA zmieniana" if self.domain_change else "Dziedzina NIE była zmieniana")
        return (time.time() - start_time), self.step_number, self.recurrence_number
