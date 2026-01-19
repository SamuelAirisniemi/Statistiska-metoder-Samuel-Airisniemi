from math import comb

#A)
p = comb(10, 3)
s = comb(8, 2)
ce = comb(4, 2)
st = comb(3, 1)

antal_team = p * s * ce * st

print(f"Antal teams: {antal_team}")

#B)
p = comb(10, 3)
s = comb(8, 2)
ce = comb(3, 1) #Denna ändrad
st = comb(3, 1)

antal_team = p * s * ce * st

print(f"Antal teams med en specifik computer engineer: {antal_team}")