import numpy as np
import matplotlib.pyplot as plt
import random
import sys

rng = np.random.default_rng()

def generate_distribution():
    dist = random.choice([
        "uniform",
        "normal",
        "binomial",
        "negative_binomial",
        "gamma",
        "geometric",
        "integers"
    ])

    if dist == "uniform":
        data = rng.uniform(0, 1, size=200)
        label = "uniform"
    elif dist == "normal":
        mu = rng.uniform(-1, 1)
        sigma = rng.uniform(0.5, 1.5)
        data = rng.normal(mu, sigma, size=200)
        label = "normal"
    elif dist == "binomial":
        n = rng.integers(5, 20)
        p = rng.uniform(0.1, 0.9)
        data = rng.binomial(n, p, size=200)
        label = "binomial"
    elif dist == "negative_binomial":
        n = rng.integers(5, 20)
        p = rng.uniform(0.1, 0.9)
        data = rng.negative_binomial(n, p, size=200)
        label = "negative_binomial"
    elif dist == "gamma":
        shape = rng.uniform(0.5, 3)
        scale = rng.uniform(0.5, 2)
        data = rng.gamma(shape, scale, size=200)
        label = "gamma"
    elif dist == "geometric":
        p = rng.uniform(0.1, 0.9)
        data = rng.geometric(p, size=200)
        label = "geometric"
    elif dist == "integers":
        data = rng.integers(0, 100, size=200)
        label = "integers"

    return data, label

def show_plot(data):
    plt.figure(figsize=(7, 5))

    if random.random() < 0.5:
        # Histogram
        plt.hist(data, bins=15, color="steelblue", edgecolor="black")
        plt.title("Identify the distribution (Histogram)")
    else:
        # Ogive (CDF)
        sorted_vals = np.sort(data)
        cdf = np.arange(1, len(data) + 1) / len(data)
        plt.plot(sorted_vals, cdf, color="steelblue")
        plt.title("Identify the distribution (Ogive / CDF)")

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()

def quiz():
    score = 0
    rounds = 0

    print("Distribution Quiz - type 'quit' to exit.\n")
    print("Possible answers: uniform, normal, binomial, negative_binomial, gamma, geometric, integers\n")

    while True:
        data, correct = generate_distribution()
        show_plot(data)

        guess = input("Your guess: ").strip().lower()
        if guess == "quit":
            break

        rounds += 1
        if guess == correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. Correct answer was: {correct}\n")

        print(f"Score: {score}/{rounds}\n")

    print(f"Final score: {score}/{rounds}")
    print("Good luck on the exam!")


if __name__ == "__main__":
    quiz()