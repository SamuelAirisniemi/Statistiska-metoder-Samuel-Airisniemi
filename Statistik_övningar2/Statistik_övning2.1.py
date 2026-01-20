from math import comb
from math import factorial
from scipy.stats import binom

#A)
n = 10
p = 0.7

detections = n * p
print(f"Förväntat antal detekteringar: {detections}")

#B)
n = 12
p = 0.7

total_prob = sum(binom.pmf(k, n, p) for k in range(2, 8))
print(f"Sannolikhet att mellan 2 och 7 personer detekteras: {total_prob:.4f}")

#C)
n = 5
x = 3
likelihood = binom.pmf(x,n,p)
print(likelihood)