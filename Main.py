import CSP
import numpy as np

# Kolorowanie Grafu

# csp1 = CSP.CSP(size=10)
# csp1.backtracking_map_horizontal()
# csp2 = CSP.CSP(size=10)
# csp2.backtracking_map_vertical()
# csp3 = CSP.CSP(size=10)
# csp3.forward_checking_map_horizontal()
# csp4 = CSP.CSP(size=10)
# csp4.forward_checking_map_vertical()

# Kwadrat Laciński

# csp5 = CSP.CSP(size=10, domain_size=10)
# csp5.backtracking_latin_horizontal(choose_random_color=True)
# csp6 = CSP.CSP(size=10, domain_size=10)
# csp6.backtracking_latin_vertical(choose_random_color=True)
csp7 = CSP.CSP(size=10, domain_size=10)
csp7.forward_checking_latin_horizontal(choose_random_color=True)
csp8 = CSP.CSP(size=10, domain_size=10)
csp8.forward_checking_latin_vertical(choose_random_color=True)

########################################################################################################################

# domain = np.arange(2)
# chosen_colors_matrix = np.array([np.array([domain for i in range(2)]) for j in range(2)])
# print(chosen_colors_matrix)
# test = np.append([chosen_colors_matrix], [chosen_colors_matrix], axis=0)
# print(test)
# test = np.append(test, [chosen_colors_matrix], axis=0)
# print(test[-1])
# chosen_colors_matrix = np.zeros([5, 5, 5], dtype=int)
# chosen_colors_matrix[1][1][5-1] = 5
# print(np.array_equal(np.array([1, 2]), np.array([2, 1])))
