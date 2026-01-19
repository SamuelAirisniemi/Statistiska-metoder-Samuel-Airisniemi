from math import comb

#A)
def binom_pmf(k, n, p):
    return comb(n ,k) * (p**k) * ((1-p)**(n-k))

print(binom_pmf(3, 5, 0.7))

#B)
prob = sum(binom_pmf(k, 12, 0.7) for k in range(2, 8))

print(prob)

#C)
expected = 10 * 0.7
print(expected)

#D)
possible_n = range(1, 11)
p = 0.7
prior = 1 / len(possible_n)
likelihoods = [binom_pmf(3, n, p) * prior for n in possible_n]
total = sum(likelihoods)

posterior_n5 = binom_pmf(3, 5, p) * prior / total
print(posterior_n5)