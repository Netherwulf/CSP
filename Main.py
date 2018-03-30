import CSP
import numpy as np

csp = CSP.CSP(size=3)
csp.solve_graph_colorization_backtracking()
# domain = np.arange(2)
# # chosen_colors_matrix = np.where(x == 0, np.array([]), np.array([]))
# chosen_colors_matrix = np.zeros([5, 5, 5], dtype=int)
# chosen_colors_matrix[1][1][5-1] = 5
# print(np.array_equal(np.array([1, 2]), np.array([2, 1])))
