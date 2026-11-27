import secrets
import string

haslo = input("Podaj haslo: ")

punkty = 0

braki = []

if len(haslo) >= 12:
    punkty += 1
else:
    braki.append("Minimum 12 znakow")
    
for znak in haslo:
    if znak.islower():
        punkty += 1
        break
else:
    braki.append("Mala litera")
    
for znak in haslo:
    if znak.isupper():
        punkty += 1
        break
else:
    braki.append("Wielka litera")
    
for znak in haslo:
    if znak.isdigit():
        punkty += 1
        break
else:
    braki.append("Cyfra")

for znak in haslo:
    if not znak.isalnum():
        punkty += 1
        break
else:
    braki.append("Znak specjalny")
    
if punkty <= 2:
    ocena = "Slabe"
elif punkty <= 4:
    ocena = "Srednie"
else:    
    ocena = "Mocne"

print("Liczba punktow:", punkty, "/ 5")
print("Ocena hasla:", ocena)

if braki:
    print("Brakuje:")
    for brak in braki:
        print("-", brak)
else:
    print("Haslo spelnia wszystkie wymagania!")

def generuj_haslo(dlugosc=16):
    znaki = string.ascii_letters + string.digits + "!@#$%^&*"
    haslo = ''.join(secrets.choice(znaki) for _ in 
    range(dlugosc))
    return haslo

print("Wygenerowane haslo:", generuj_haslo())


