#1
    cifre = '1234567890'
    cont = 0

    inp = input("Introduceti valorile dorite:")
    nume = str(input("Introduceti numele dvs:"))

    for cifra in inp:
        if cifra in cifre:
            cont += 1

    if cont == len(inp):
        print(f"Sirul de numere a fost gasit de {nume}")
    elif cont == 0:
        print(f"Sirul de caractere a fost gasit de {nume}")
    else:
        print("mixt")

#2
numar = input("Introduceti un numar:")
while not numar.isdecimal():
    numar = input("Ala nu e numar,mai incearca odata:")

if (int(numar) % 2) == 0:
    print("Wow , este par!")
else:
    print("Wow, nu este par!")


3
year = input("Introduceti un an:")
while not year.isdecimal():
     year = input("Ala nu e an,mai incearca odata:")
if int(year) % 4 == 0 and (int(year) % 400 == 0 or int(year) % 100 != 0):
    print("An bisect")
else:
    print("Nu e an bisect")

#4
numar = input("Introduceti un numar:")
try:
    val = int(numar)
    print("Input is an integer number. Number = ", val)
except ValueError:
    print("Input is a string, try again ")

if int(numar) < 0:
    print("Numarul in val absoluta este:", abs(int(numar)))
elif int(numar) == 0:
    print("Numar este 0")
else:
    if int(numar) < 10:
        print("Este mai mic decat 10")

#5
meniu = {
    1: "Afisare lista de cumparaturi",
    2: "Adaugare element",
    3: "Stergere element",
    4: "Sterere lista de cumparaturi ",
    5: "Cautare in lista de cumparaturi"
}
optiuni = [1,2,3,4,5]
opt = int(input("Alegeti o optiune din meniu(1-5):"))
if opt in optiuni:
    print(meniu[opt])
else:
    print("alegerea nu exista")