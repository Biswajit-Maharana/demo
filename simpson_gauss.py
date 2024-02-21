
import numpy as np
import my_lib as lib
def integrand(x):
    return np.sqrt(1 + x**4)
a=0
b = 1
n_simpsons = 1000
n_gaussian = 5
result_simpsons = lib.simpsons_rule(integrand, a, b, n_simpsons)

print(f"Simpson's Rule result: {result_simpsons:.6f}")
