import CSP
import numpy as np
import matplotlib.pyplot as plt

# csp_bt_6 = CSP.CSP(size=6, domain_size=3).backtracking_map()[0]
########################################################################################################################
# --------------------------------------------------KOLOROWANIE GRAFU---------------------------------------------------
########################################################################################################################

# ------------------------------------------PORÓWNANIE CZASU DLA 5 ROZMIARÓW--------------------------------------------

objects = ('6 x 6',
           '9 x 9',
           '12 x 12',
           '15 x 15'
           '18 x 18')
y_pos = np.arange(len(objects))

csp_bt_6 = CSP.CSP(size=6, domain_size=5).backtracking_map()[0]
csp_bt_9 = CSP.CSP(size=9, domain_size=5).backtracking_map()[0]
csp_bt_12 = CSP.CSP(size=12, domain_size=5).backtracking_map()[0]
csp_bt_15 = CSP.CSP(size=15, domain_size=5).backtracking_map()[0]
csp_bt_18 = CSP.CSP(size=18, domain_size=5).backtracking_map()[0]

csp_fc_6 = CSP.CSP(size=6, domain_size=5).forward_checking_map()[0]
csp_fc_9 = CSP.CSP(size=9, domain_size=5).forward_checking_map()[0]
csp_fc_12 = CSP.CSP(size=12, domain_size=5).forward_checking_map()[0]
csp_fc_15 = CSP.CSP(size=15, domain_size=5).forward_checking_map()[0]
csp_fc_18 = CSP.CSP(size=18, domain_size=5).forward_checking_map()[0]

backtracking = [csp_bt_6, csp_bt_9, csp_bt_12, csp_bt_15, csp_bt_18]
forward_checking = [csp_fc_6, csp_fc_9, csp_fc_12, csp_fc_15, csp_fc_18]

plt.bar(y_pos, backtracking, align='center', alpha=0.5)
plt.bar(y_pos, forward_checking, align='center', alpha=0.5)

plt.xticks(y_pos, objects)
plt.ylabel('Czas wykonania')
plt.xlabel('Rozmiar kolorowanej kraty')
plt.title('Czas znalezienia pierwszego rozwiązania problemu kolorowania mapy metodą backtracking i forward checking')

plt.show()

# --------------------------------------PORÓWNANIE LICZBY KROKÓW DLA 5 ROZMIARÓW----------------------------------------

# objects = ('6 x 6',
#            '9 x 9',
#            '12 x 12',
#            '15 x 15'
#            '18 x 18')
# y_pos = np.arange(len(objects))
#
# csp_bt_6 = CSP.CSP(size=6, domain_size=5).backtracking_map()[1]
# csp_bt_9 = CSP.CSP(size=9, domain_size=5).backtracking_map()[1]
# csp_bt_12 = CSP.CSP(size=12, domain_size=5).backtracking_map()[1]
# csp_bt_15 = CSP.CSP(size=15, domain_size=5).backtracking_map()[1]
# csp_bt_18 = CSP.CSP(size=18, domain_size=5).backtracking_map()[1]
#
# csp_fc_6 = CSP.CSP(size=6, domain_size=5).forward_checking_map()[0]
# csp_fc_9 = CSP.CSP(size=9, domain_size=5).forward_checking_map()[0]
# csp_fc_12 = CSP.CSP(size=12, domain_size=5).forward_checking_map()[0]
# csp_fc_15 = CSP.CSP(size=15, domain_size=5).forward_checking_map()[0]
# csp_fc_18 = CSP.CSP(size=18, domain_size=5).forward_checking_map()[0]
#
# backtracking = [csp_bt_6, csp_bt_9, csp_bt_12, csp_bt_15, csp_bt_18]
# forward_checking = [csp_fc_6, csp_fc_9, csp_fc_12, csp_fc_15, csp_fc_18]
#
# plt.bar(y_pos, backtracking, align='center', alpha=0.5)
# plt.bar(y_pos, forward_checking, align='center', alpha=0.5)
#
# plt.xticks(y_pos, objects)
# plt.ylabel('Liczba kroków')
# plt.xlabel('Rozmiar kolorowanej kraty')
# plt.title('Liczba kroków do znalezienia pierwszego rozwiązania problemu kolorowania mapy metodą backtracking i forward checking')
#
# plt.show()

# -------------------------------------PORÓWNANIE LICZBY NAWROTÓW DLA 5 ROZMIARÓW---------------------------------------

# objects = ('6 x 6',
#            '9 x 9',
#            '12 x 12',
#            '15 x 15'
#            '18 x 18')
# y_pos = np.arange(len(objects))
#
# csp_bt_6 = CSP.CSP(size=6, domain_size=5).backtracking_map()[2]
# csp_bt_9 = CSP.CSP(size=9, domain_size=5).backtracking_map()[2]
# csp_bt_12 = CSP.CSP(size=12, domain_size=5).backtracking_map()[2]
# csp_bt_15 = CSP.CSP(size=15, domain_size=5).backtracking_map()[2]
# csp_bt_18 = CSP.CSP(size=18, domain_size=5).backtracking_map()[2]
#
# csp_fc_6 = CSP.CSP(size=6, domain_size=5).forward_checking_map()[2]
# csp_fc_9 = CSP.CSP(size=9, domain_size=5).forward_checking_map()[2]
# csp_fc_12 = CSP.CSP(size=12, domain_size=5).forward_checking_map()[2]
# csp_fc_15 = CSP.CSP(size=15, domain_size=5).forward_checking_map()[2]
# csp_fc_18 = CSP.CSP(size=18, domain_size=5).forward_checking_map()[2]
#
# backtracking = [csp_bt_6, csp_bt_9, csp_bt_12, csp_bt_15, csp_bt_18]
# forward_checking = [csp_fc_6, csp_fc_9, csp_fc_12, csp_fc_15, csp_fc_18]
#
# plt.bar(y_pos, backtracking, align='center', alpha=0.5)
# plt.bar(y_pos, forward_checking, align='center', alpha=0.5)
#
# plt.xticks(y_pos, objects)
# plt.ylabel('Czas wykonania')
# plt.xlabel('Rozmiar kolorowanej kraty')
# plt.title('Liczba nawrotów do znalezienia pierwszego rozwiązania problemu kolorowania mapy metodą backtracking i forward checking')
#
# plt.show()
#
# # PORÓWNANIE WPLYWU ZASTOSOWANIA HEURYSTYKI (DOBÓR KOLORÓW OD NAJMNIEJSZEGO DO NAJWIĘKSZEGO I LOSOWY) NA CZAS WYKONANIA
#
# objects = ('backtracking',
#            'forward checking')
# y_pos = np.arange(len(objects))
#
# csp_bt_9 = CSP.CSP(size=9, domain_size=5).backtracking_map()[0]
# csp_bt_9_random = CSP.CSP(size=9, domain_size=5).forward_checking_map(choose_random_color=True)[0]
#
# csp_fc_9 = CSP.CSP(size=9, domain_size=5).forward_checking_map()[0]
# csp_fc_9_random = CSP.CSP(size=9, domain_size=5).forward_checking_map(choose_random_color=True)[0]
#
# backtracking = [csp_bt_9, csp_bt_9_random]
# forward_checking = [csp_fc_9, csp_fc_9_random]
#
# plt.bar(y_pos, backtracking, align='center', alpha=0.5)
# plt.bar(y_pos, forward_checking, align='center', alpha=0.5)
#
# plt.xticks(y_pos, objects)
# plt.ylabel('Czas wykonania')
# plt.xlabel('Użyty algorytm')
# plt.title('Wpływ wyboru heurytstyki na czas znalezienia pierwszego rozwiązania problemu kolorowania mapy metodą backtracking i forward checking')
#
# plt.show()

########################################################################################################################
# --------------------------------------------------KKWADRAT LACINSKI---------------------------------------------------
########################################################################################################################

# ------------------------------------------PORÓWNANIE CZASU DLA 5 ROZMIARÓW--------------------------------------------

# objects = ('6 x 6',
#            '9 x 9',
#            '12 x 12',
#            '15 x 15'
#            '18 x 18')
# y_pos = np.arange(len(objects))
#
# csp_bt_6 = CSP.CSP(size=6, domain_size=6).backtracking_latin()[0]
# csp_bt_9 = CSP.CSP(size=9, domain_size=9).backtracking_latin()[0]
# csp_bt_12 = CSP.CSP(size=12, domain_size=12).backtracking_latin()[0]
# csp_bt_15 = CSP.CSP(size=15, domain_size=15).backtracking_latin()[0]
# csp_bt_18 = CSP.CSP(size=18, domain_size=18).backtracking_latin()[0]
#
# csp_fc_6 = CSP.CSP(size=6, domain_size=6).forward_checking_latin()[0]
# csp_fc_9 = CSP.CSP(size=9, domain_size=9).forward_checking_latin()[0]
# csp_fc_12 = CSP.CSP(size=12, domain_size=12).forward_checking_latin()[0]
# csp_fc_15 = CSP.CSP(size=15, domain_size=15).forward_checking_latin()[0]
# csp_fc_18 = CSP.CSP(size=18, domain_size=18).forward_checking_latin()[0]
#
# backtracking = [csp_bt_6, csp_bt_9, csp_bt_12, csp_bt_15, csp_bt_18]
# forward_checking = [csp_fc_6, csp_fc_9, csp_fc_12, csp_fc_15, csp_fc_18]
#
# plt.bar(y_pos, backtracking, align='center', alpha=0.5)
# plt.bar(y_pos, forward_checking, align='center', alpha=0.5)
#
# plt.xticks(y_pos, objects)
# plt.ylabel('Czas wykonania')
# plt.xlabel('Rozmiar kolorowanej kraty')
# plt.title('Czas znalezienia pierwszego rozwiązania problemu kwadratu łacińskiego metodą backtracking i forward checking')
#
# plt.show()

# --------------------------------------PORÓWNANIE LICZBY KROKÓW DLA 5 ROZMIARÓW----------------------------------------

# objects = ('6 x 6',
#            '9 x 9',
#            '12 x 12',
#            '15 x 15'
#            '18 x 18')
# y_pos = np.arange(len(objects))
#
# csp_bt_6 = CSP.CSP(size=6, domain_size=6).backtracking_latin()[1]
# csp_bt_9 = CSP.CSP(size=9, domain_size=9).backtracking_latin()[1]
# csp_bt_12 = CSP.CSP(size=12, domain_size=12).backtracking_latin()[1]
# csp_bt_15 = CSP.CSP(size=15, domain_size=15).backtracking_latin()[1]
# csp_bt_18 = CSP.CSP(size=18, domain_size=18).backtracking_latin()[1]
#
# csp_fc_6 = CSP.CSP(size=6, domain_size=6).forward_checking_latin()[1]
# csp_fc_9 = CSP.CSP(size=9, domain_size=9).forward_checking_latin()[1]
# csp_fc_12 = CSP.CSP(size=12, domain_size=12).forward_checking_latin()[1]
# csp_fc_15 = CSP.CSP(size=15, domain_size=15).forward_checking_latin()[1]
# csp_fc_18 = CSP.CSP(size=18, domain_size=18).forward_checking_latin()[1]
#
# backtracking = [csp_bt_6, csp_bt_9, csp_bt_12, csp_bt_15, csp_bt_18]
# forward_checking = [csp_fc_6, csp_fc_9, csp_fc_12, csp_fc_15, csp_fc_18]
#
# plt.bar(y_pos, backtracking, align='center', alpha=0.5)
# plt.bar(y_pos, forward_checking, align='center', alpha=0.5)
#
# plt.xticks(y_pos, objects)
# plt.ylabel('Liczba kroków')
# plt.xlabel('Rozmiar kolorowanej kraty')
# plt.title('Liczba kroków do znalezienia pierwszego rozwiązania problemu kwadratu łacińskiego metodą backtracking i forward checking')
#
# plt.show()

# -------------------------------------PORÓWNANIE LICZBY NAWROTÓW DLA 5 ROZMIARÓW---------------------------------------

# objects = ('6 x 6',
#            '9 x 9',
#            '12 x 12',
#            '15 x 15'
#            '18 x 18')
# y_pos = np.arange(len(objects))
#
# csp_bt_6 = CSP.CSP(size=6, domain_size=6).backtracking_latin()[2]
# csp_bt_9 = CSP.CSP(size=9, domain_size=9).backtracking_latin()[2]
# csp_bt_12 = CSP.CSP(size=12, domain_size=12).backtracking_latin()[2]
# csp_bt_15 = CSP.CSP(size=15, domain_size=15).backtracking_latin()[2]
# csp_bt_18 = CSP.CSP(size=18, domain_size=18).backtracking_latin()[2]
#
# csp_fc_6 = CSP.CSP(size=6, domain_size=6).forward_checking_latin()[2]
# csp_fc_9 = CSP.CSP(size=9, domain_size=9).forward_checking_latin()[2]
# csp_fc_12 = CSP.CSP(size=12, domain_size=12).forward_checking_latin()[2]
# csp_fc_15 = CSP.CSP(size=15, domain_size=15).forward_checking_latin()[2]
# csp_fc_18 = CSP.CSP(size=18, domain_size=18).forward_checking_latin()[2]
#
# backtracking = [csp_bt_6, csp_bt_9, csp_bt_12, csp_bt_15, csp_bt_18]
# forward_checking = [csp_fc_6, csp_fc_9, csp_fc_12, csp_fc_15, csp_fc_18]
#
# plt.bar(y_pos, backtracking, align='center', alpha=0.5)
# plt.bar(y_pos, forward_checking, align='center', alpha=0.5)
#
# plt.xticks(y_pos, objects)
# plt.ylabel('Czas wykonania')
# plt.xlabel('Rozmiar kolorowanej kraty')
# plt.title('Liczba nawrotów do znalezienia pierwszego rozwiązania problemu kwadratu łacińskiego metodą backtracking i forward checking')
#
# plt.show()

# PORÓWNANIE WPLYWU ZASTOSOWANIA HEURYSTYKI (DOBÓR KOLORÓW OD NAJMNIEJSZEGO DO NAJWIĘKSZEGO I LOSOWY) NA CZAS WYKONANIA

# objects = ('backtracking',
#            'forward checking')
# y_pos = np.arange(len(objects))
#
# csp_bt_9 = CSP.CSP(size=9, domain_size=9).backtracking_latin()[0]
# csp_bt_9_random = CSP.CSP(size=9, domain_size=9).forward_checking_latin(choose_random_color=True)[0]
#
# csp_fc_9 = CSP.CSP(size=9, domain_size=9).forward_checking_latin()[0]
# csp_fc_9_random = CSP.CSP(size=9, domain_size=9).forward_checking_latin(choose_random_color=True)[0]
#
# backtracking = [csp_bt_9, csp_bt_9_random]
# forward_checking = [csp_fc_9, csp_fc_9_random]
#
# plt.bar(y_pos, backtracking, align='center', alpha=0.5)
# plt.bar(y_pos, forward_checking, align='center', alpha=0.5)
#
# plt.xticks(y_pos, objects)
# plt.ylabel('Czas wykonania')
# plt.xlabel('Użyty algorytm')
# plt.title('Wpływ wyboru heurytstyki na czas znalezienia pierwszego rozwiązania problemu kwadratu łacińskiego metodą backtracking i forward checking')
#
# plt.show()
