import CSP
import numpy as np

csp = CSP.CSP(size=100)
# csp.backtracking_map_horizontal()
csp.forward_checking_map_horizontal()
# domain = np.arange(2)
# chosen_colors_matrix = np.array([np.array([domain for i in range(3)]) for j in range(3)])
# print(chosen_colors_matrix.shape)
# chosen_colors_matrix = np.zeros([5, 5, 5], dtype=int)
# chosen_colors_matrix[1][1][5-1] = 5
# print(np.array_equal(np.array([1, 2]), np.array([2, 1])))
