import datetime

cnp = input("Please enter you ID for validation:")


def validate(number):

    century = {
        1: 1900, 2: 1900, 3: 1800, 4: 1800, 5: 2000, 6: 2000, 7: 1900, 8: 1900, 9: 1900
    }


    county = {
        '01': "Alba", '02': "Arad", '03': "Arges", '04': "Bacau", '05': "Bihor", '06': "Bistrita",
        '07': "Botosani", '08': "Brasov", '09': "Braila", '10': 'Buzau', '11': "Caras-Severin", '12': "Cluj",
        '13': "Constanta", '14': "Covasna", '15': "Dambovita", '16': "Dolj", '17': "Galati", '18': "Gorj",
        '19': "Harghita", '21': "Ialomita", '22': "Iasi", '23': "Ilfov", '24': "Maramures", '25': "Mehedinti",
        '26': "Mures", '27': "Neamt", '28': "Olt", '29': "Prahova", '30': "Satu-Mare", '32': "Salaj", '33': "Sibiu",
        '34': "Suceava", '35': "Timis", '36': "Tulcea", '37': "Vaslui", '38': "Valcea", '39': "Vrancea",
        '40': "Bucuresti", '41': "Bucuresti S1", '42': "Bucuresti S2", '43': "Bucuresti S3", '44': "Bucuresti S4",
        '45': "Bucuresti S5", '46': "Bucuresti S6", '51': "Calarasi", '52': "Giurgiu"
    }

    s = int(number[0])
    year = int(number[1:3]) + century[s]
    month = int(number[3:5])
    day = int(number[5:7])

    try:
        while datetime.date(year, month, day):
            break
    except ValueError:
        return "Data de nastere invalida"

    jj = number[7:9]
    if jj not in county.keys():
        return "Invalid county "

    nnn = number[9:12]
    if not nnn.isdigit():
        return "Numar unic invalid "

    multy = "2791463582790"
    var = 0
    for index in range(len(multy)):
        var += int(multy[index]) * int(number[index])
    c = var % 11
    if c == 10:
        c = 1
    if str(c) != number[-1]:
        return "Cifra de control invalida"

    if int(number[0]) % 2 == 0:
        sex = "Feminin"
    else:
        sex = 'Masculin'

    if int(number[0]) > 6:
        nationalitate = 'tigan'
    else:
        nationalitate = 'romana'

    return """Persoana {} de sexul {} nascuta in anul {},luna {},in ziua {},din judetul {} are CNP-ul valid"""\
        .format(nationalitate, sex, year, month, day, county[jj])


print(validate(cnp))
