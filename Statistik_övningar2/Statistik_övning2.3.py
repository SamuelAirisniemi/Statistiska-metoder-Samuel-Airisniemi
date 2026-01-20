from scipy.stats import geom

#A)
p = 0.7
P_X_eq_2 = geom.pmf(2, p)
print(f"P(X=2) = {P_X_eq_2:.4f}")

#B)
p = 0.7
P_X_eq_3 = geom.pmf(3, p)
print(f"P(X=3) = {P_X_eq_3:.4f}")

#C)
mu = geom.mean(p)
sigma = geom.std(p)
answer = mu + 2 * sigma
print(answer)