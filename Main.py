import CSP
import numpy as np

csp = CSP.CSP()

domain = np.arange(2)
# chosen_colors_matrix = np.where(x == 0, np.array([]), np.array([]))
chosen_colors_matrix = np.ones([5, 5, 1], dtype=int)
print(chosen_colors_matrix)
