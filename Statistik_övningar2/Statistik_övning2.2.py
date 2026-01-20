from scipy.stats import norm, binom
import math

#A)
def uppgift_a():
    print("Stickprovet kan komma från vilken fördelning som helst med medelvärde 0 och standardavvikelse 1.")
    print("Exempel: normalfördelning, t-fördelning, uniform fördelning, Laplace, etc.")

#B)
def uppgift_b():
    p1 = norm.cdf(1) - norm.cdf(-1)
    p2 = norm.cdf(2) - norm.cdf(-2)
    p3 = norm.cdf(3) - norm.cdf(-3)

    print(f"Inom 1σ: {p1:.4f}")
    print(f"Inom 2σ: {p2:.4f}")
    print(f"Inom 3σ: {p3:.4f}")

#C)
def uppgift_c():
    personer_per_dag = 24000
    p = 0.7
    expected = personer_per_dag * p
    print(f"Förväntade detekteringar per dag: {expected:.0f}")

#D)
import math

def uppgift_d(): #Fel
    n = 24000
    p = 0.7
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    gräns = mu - 2 * sigma
    print(f"Ovanligt få detekteringar: mindre än {gräns:.0f}")

#Rätt svar till d
# mu = binom.mean(n, p)
# sigma = binom.std(n, p)
# mu - 2 * sigma
# print(mu)

if __name__ == "__main__":
    uppgift_a()
    print("\nUppgift b:")
    uppgift_b()
    print("\nUppgift c:")
    uppgift_c()
    print("\nUppgift d:")
    uppgift_d()