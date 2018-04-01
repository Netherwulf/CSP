import CSP
import numpy as np

########################################################################################################################
# --------------------------------------------------KOLOROWANIE GRAFU---------------------------------------------------
########################################################################################################################

# csp1 = CSP.CSP(size=10)
# csp1.backtracking_map_horizontal()
# csp2 = CSP.CSP(size=10)
# csp2.backtracking_map_vertical()
# csp3 = CSP.CSP(size=10)
# csp3.forward_checking_map_horizontal()
# csp4 = CSP.CSP(size=10)
# csp4.forward_checking_map_vertical()

########################################################################################################################
# --------------------------------------------------KKWADRAT LACINSKI---------------------------------------------------
########################################################################################################################
# csp5 = CSP.CSP(size=10, domain_size=10)
# csp5.backtracking_latin_horizontal(choose_random_color=True)
# csp6 = CSP.CSP(size=10, domain_size=10)
# csp6.backtracking_latin_vertical(choose_random_color=True)
csp7 = CSP.CSP(size=10, domain_size=10)
csp7.forward_checking_latin_horizontal(choose_random_color=True)
csp8 = CSP.CSP(size=10, domain_size=10)
csp8.forward_checking_latin_vertical(choose_random_color=True)

