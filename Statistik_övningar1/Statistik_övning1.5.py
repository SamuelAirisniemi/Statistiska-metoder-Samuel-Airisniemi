from math import factorial

#A) 26^5 * 10
letters = 26 ** 5
digits = 10
total_passwords = letters * digits

print(f"Totalt sntal lösenord: {total_passwords}")

#B) 5!/(3! * 2!)=10  --> 10*5 = 50 
letter_arrangements = factorial(5) // (factorial(3) * factorial(2))
even_digits = 5
password = letter_arrangements * even_digits

print(f"Antal speciallösenord: {password}")

#C) 1/50 = 0.02
probability = 1 / password

print(f"Sannolikheten att gissa rätt: {probability}")