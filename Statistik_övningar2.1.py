from math import comb

def binom_pmf(k, n, p):
    return comb(n ,k) * (p**k) * ((1-p)**(n-k))

print(binom_pmf(3, 5, 0.7))