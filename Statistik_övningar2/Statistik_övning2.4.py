import math

#A)
p = 0.7
n = 12

expected_attempts = n / p
print(f"Förväntat antal försök: {expected_attempts:.1f}")

#B)
p = 0.7
n = 12
prob_T_eq_12 = p ** n

print(f"P(T=12) = {prob_T_eq_12:.5f}")

#C)
p = 0.7
n = 12

mu = n / p
var_T = n * (1 - p) / (p ** 2)
sigma_T = math.sqrt(var_T)

worst_case = mu + 3 * sigma_T

print(f"E[T] ≈ {mu:.4f}")
print(f"Var(T) ≈ {var_T:.4f}, σ_T ≈ {sigma_T:.4f}")
print(f'Rimligt värsta fall (≈ μ + 2σ): {worst_case:.2f} försök')