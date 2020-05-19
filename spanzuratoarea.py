import random
from random_word import RandomWords

r = RandomWords()
lista_cuvinte = r.get_random_words(hasDictionaryDef='true', minCorpusCount=1, maxCorpusCount=5, minLength=5, maxLength=12, sortBy="alpha", sortOrder="asc", limit=15)
print(lista_cuvinte)

cuvant_ales = random.choice(lista_cuvinte)
print(cuvant_ales)

cuvant_curent = list(['_'] * len(cuvant_ales))
alegeri_gresite = []
numar_incercari = 8
print("Cuvantul este {}".format(" ".join(cuvant_curent)))

while "".join(cuvant_curent) != cuvant_ales and numar_incercari:

    urmatoarea_litera = input("Introduceti urmatoarea litera: ").lower()

    if len(urmatoarea_litera) != 1:
        print("Introduceti o singura litera")
    elif not urmatoarea_litera.isalpha():
        print("Caracterul introdus nu este o litera")
    elif urmatoarea_litera in alegeri_gresite:
        print("Litera a fost deja aleasa")
    elif urmatoarea_litera in cuvant_curent:
        print("Litera a fost deja aleasa si se afla in cuvantul curent")
    elif urmatoarea_litera in cuvant_ales:
        for index,litera in enumerate(cuvant_ales):
            if litera == urmatoarea_litera:
                cuvant_curent[index] = urmatoarea_litera
        print("Cuvantul pana acuma este {}".format(' '.join(cuvant_curent)))
    else:
        alegeri_gresite.append(urmatoarea_litera)
        numar_incercari -= 1
        print('Incercari ramase: {} | Litere gresite: {}'.format(numar_incercari, alegeri_gresite))


if numar_incercari:
    print('Cuvantul corect este: {}'.format(''.join(cuvant_ales)))
else:
    print('Cuvantul corect era: {}'.format(''.join(cuvant_ales)))
