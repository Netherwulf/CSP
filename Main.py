import CSP
import numpy as np
import matplotlib.pyplot as plt

csp_1 = CSP.CSP(size=25, domain_size=5).backtracking_map()

########################################################################################################################
# --------------------------------------------------KOLOROWANIE GRAFU---------------------------------------------------
########################################################################################################################

# -----------------------------------------PORÓWNANIE CZASU DLA 4/5 ROZMIARÓW-------------------------------------------

# objects = ('10 x 10',
#            '15 x 15',
#            '20 x 20',
#            '25 x 25'
#            '30 x 30')
# y_pos = np.arange(len(objects))
#
# csp_bt_10 = CSP.CSP(size=10, domain_size=5).backtracking_map()[0]
# csp_bt_15 = CSP.CSP(size=15, domain_size=5).backtracking_map()[0]
# csp_bt_20 = CSP.CSP(size=20, domain_size=5).backtracking_map()[0]
# csp_bt_25 = CSP.CSP(size=25, domain_size=5).backtracking_map()[0]
# csp_bt_30 = CSP.CSP(size=30, domain_size=5).backtracking_map()[0]
#
# csp_fc_10 = CSP.CSP(size=10, domain_size=5).forward_checking_map()[0]
# csp_fc_15 = CSP.CSP(size=15, domain_size=5).forward_checking_map()[0]
# csp_fc_20 = CSP.CSP(size=20, domain_size=5).forward_checking_map()[0]
# csp_fc_25 = CSP.CSP(size=25, domain_size=5).forward_checking_map()[0]
# csp_fc_30 = CSP.CSP(size=30, domain_size=5).forward_checking_map()[0]
#
# backtracking = [csp_bt_10, csp_bt_15, csp_bt_20, csp_bt_25, csp_bt_30]
# forward_checking = [csp_fc_10, csp_fc_15, csp_fc_20, csp_fc_25, csp_fc_30]
#
# plt.bar(y_pos, backtracking, align='center', alpha=0.5)
# plt.bar(y_pos, forward_checking, align='center', alpha=0.5)
#
# plt.xticks(y_pos, objects)
# plt.ylabel('Czas wykonania')
# plt.xlabel('Rozmiar kolorowanej kraty')
# plt.title('Czas znalezienia pierwszego rozwiązania problemu kolorowania mapy metodą backtracking i forward checking')
#
# plt.show()

# -------------------------------------PORÓWNANIE LICZBY KROKÓW DLA 4/5 ROZMIARÓW---------------------------------------

# objects = ('10 x 10',
#            '15 x 15',
#            '20 x 20',
#            '25 x 25'
#            '30 x 30')
# y_pos = np.arange(len(objects))
#
# csp_bt_10 = CSP.CSP(size=10, domain_size=5).backtracking_map()[1]
# csp_bt_15 = CSP.CSP(size=15, domain_size=5).backtracking_map()[1]
# csp_bt_20 = CSP.CSP(size=20, domain_size=5).backtracking_map()[1]
# csp_bt_25 = CSP.CSP(size=25, domain_size=5).backtracking_map()[1]
# csp_bt_30 = CSP.CSP(size=30, domain_size=5).backtracking_map()[1]
#
# csp_fc_10 = CSP.CSP(size=10, domain_size=5).forward_checking_map()[1]
# csp_fc_15 = CSP.CSP(size=15, domain_size=5).forward_checking_map()[1]
# csp_fc_20 = CSP.CSP(size=20, domain_size=5).forward_checking_map()[1]
# csp_fc_25 = CSP.CSP(size=25, domain_size=5).forward_checking_map()[1]
# csp_fc_30 = CSP.CSP(size=30, domain_size=5).forward_checking_map()[1]
#
# backtracking = [csp_bt_10, csp_bt_15, csp_bt_20, csp_bt_25, csp_bt_30]
# forward_checking = [csp_fc_10, csp_fc_15, csp_fc_20, csp_fc_25, csp_fc_30]
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

# ------------------------------------PORÓWNANIE LICZBY NAWROTÓW DLA 4/5 ROZMIARÓW--------------------------------------

# objects = ('10 x 10',
#            '15 x 15',
#            '20 x 20',
#            '25 x 25'
#            '30 x 30')
# y_pos = np.arange(len(objects))
#
# csp_bt_10 = CSP.CSP(size=10, domain_size=5).backtracking_map()[2]
# csp_bt_15 = CSP.CSP(size=15, domain_size=5).backtracking_map()[2]
# csp_bt_20 = CSP.CSP(size=20, domain_size=5).backtracking_map()[2]
# csp_bt_25 = CSP.CSP(size=25, domain_size=5).backtracking_map()[2]
# csp_bt_30 = CSP.CSP(size=30, domain_size=5).backtracking_map()[2]
#
# csp_fc_10 = CSP.CSP(size=10, domain_size=5).forward_checking_map()[2]
# csp_fc_15 = CSP.CSP(size=15, domain_size=5).forward_checking_map()[2]
# csp_fc_20 = CSP.CSP(size=20, domain_size=5).forward_checking_map()[2]
# csp_fc_25 = CSP.CSP(size=25, domain_size=5).forward_checking_map()[2]
# csp_fc_30 = CSP.CSP(size=30, domain_size=5).forward_checking_map()[2]
#
# backtracking = [csp_bt_10, csp_bt_15, csp_bt_20, csp_bt_25, csp_bt_30]
# forward_checking = [csp_fc_10, csp_fc_15, csp_fc_20, csp_fc_25, csp_fc_30]
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
# csp_bt_15 = CSP.CSP(size=15, domain_size=5).backtracking_map()[0]
# csp_bt_15_random = CSP.CSP(size=15, domain_size=5).forward_checking_map(choose_random_color=True)[0]
#
# csp_fc_15 = CSP.CSP(size=15, domain_size=5).forward_checking_map()[0]
# csp_fc_15_random = CSP.CSP(size=15, domain_size=5).forward_checking_map(choose_random_color=True)[0]
#
# backtracking = [csp_bt_15, csp_bt_15_random]
# forward_checking = [csp_fc_15, csp_fc_15_random]
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

# objects = ('10 x 10',
#            '15 x 15',
#            '20 x 20',
#            '25 x 25'
#            '30 x 30')
# y_pos = np.arange(len(objects))
#
# csp_bt_10 = CSP.CSP(size=10, domain_size=10).backtracking_latin()[0]
# csp_bt_15 = CSP.CSP(size=15, domain_size=15).backtracking_latin()[0]
# csp_bt_20 = CSP.CSP(size=20, domain_size=20).backtracking_latin()[0]
# csp_bt_25 = CSP.CSP(size=25, domain_size=25).backtracking_latin()[0]
# csp_bt_30 = CSP.CSP(size=30, domain_size=30).backtracking_latin()[0]
#
# csp_fc_10 = CSP.CSP(size=10, domain_size=10).forward_checking_latin()[0]
# csp_fc_15 = CSP.CSP(size=15, domain_size=15).forward_checking_latin()[0]
# csp_fc_20 = CSP.CSP(size=20, domain_size=20).forward_checking_latin()[0]
# csp_fc_25 = CSP.CSP(size=25, domain_size=25).forward_checking_latin()[0]
# csp_fc_30 = CSP.CSP(size=30, domain_size=30).forward_checking_latin()[0]
#
# backtracking = [csp_bt_10, csp_bt_15, csp_bt_20, csp_bt_25, csp_bt_30]
# forward_checking = [csp_fc_10, csp_fc_15, csp_fc_20, csp_fc_25, csp_fc_30]
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

# objects = ('10 x 10',
#            '15 x 15',
#            '20 x 20',
#            '25 x 25'
#            '30 x 30')
# y_pos = np.arange(len(objects))
#
# csp_bt_10 = CSP.CSP(size=10, domain_size=10).backtracking_latin()[1]
# csp_bt_15 = CSP.CSP(size=15, domain_size=15).backtracking_latin()[1]
# csp_bt_20 = CSP.CSP(size=20, domain_size=20).backtracking_latin()[1]
# csp_bt_25 = CSP.CSP(size=25, domain_size=25).backtracking_latin()[1]
# csp_bt_30 = CSP.CSP(size=30, domain_size=30).backtracking_latin()[1]
#
# csp_fc_10 = CSP.CSP(size=10, domain_size=10).forward_checking_latin()[1]
# csp_fc_15 = CSP.CSP(size=15, domain_size=15).forward_checking_latin()[1]
# csp_fc_20 = CSP.CSP(size=20, domain_size=20).forward_checking_latin()[1]
# csp_fc_25 = CSP.CSP(size=25, domain_size=25).forward_checking_latin()[1]
# csp_fc_30 = CSP.CSP(size=30, domain_size=30).forward_checking_latin()[1]
#
# backtracking = [csp_bt_10, csp_bt_15, csp_bt_20, csp_bt_25, csp_bt_30]
# forward_checking = [csp_fc_10, csp_fc_15, csp_fc_20, csp_fc_25, csp_fc_30]
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

# objects = ('10 x 10',
#            '15 x 15',
#            '20 x 20',
#            '25 x 25'
#            '30 x 30')
# y_pos = np.arange(len(objects))
#
# csp_bt_10 = CSP.CSP(size=10, domain_size=10).backtracking_latin()[2]
# csp_bt_15 = CSP.CSP(size=15, domain_size=15).backtracking_latin()[2]
# csp_bt_20 = CSP.CSP(size=20, domain_size=20).backtracking_latin()[2]
# csp_bt_25 = CSP.CSP(size=25, domain_size=25).backtracking_latin()[2]
# csp_bt_30 = CSP.CSP(size=30, domain_size=30).backtracking_latin()[2]
#
# csp_fc_10 = CSP.CSP(size=10, domain_size=10).forward_checking_latin()[2]
# csp_fc_15 = CSP.CSP(size=15, domain_size=15).forward_checking_latin()[2]
# csp_fc_20 = CSP.CSP(size=20, domain_size=20).forward_checking_latin()[2]
# csp_fc_25 = CSP.CSP(size=25, domain_size=25).forward_checking_latin()[2]
# csp_fc_30 = CSP.CSP(size=30, domain_size=30).forward_checking_latin()[2]
#
# backtracking = [csp_bt_10, csp_bt_15, csp_bt_20, csp_bt_25, csp_bt_30]
# forward_checking = [csp_fc_10, csp_fc_15, csp_fc_20, csp_fc_25, csp_fc_30]
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
# csp_bt_15 = CSP.CSP(size=15, domain_size=15).backtracking_latin()[0]
# csp_bt_15_random = CSP.CSP(size=15, domain_size=15).forward_checking_latin(choose_random_color=True)[0]
#
# csp_fc_15 = CSP.CSP(size=15, domain_size=15).forward_checking_latin()[0]
# csp_fc_15_random = CSP.CSP(size=15, domain_size=15).forward_checking_latin(choose_random_color=True)[0]
#
# backtracking = [csp_bt_15, csp_bt_15_random]
# forward_checking = [csp_fc_15, csp_fc_15_random]
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
