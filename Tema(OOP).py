# class Catalog:
#
#     def __init__(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#         self.materii = {}
#         self.absente = 0
#
#     def __str__(self):
#         return f"Elevul {self.prenume} {self.nume} are {self.absente}"
#
#     def chiul(self):
#         self.absente += 1
#         return self.absente
#
#     def scutire(self, count):
#         self.absente = self.absente - count
#         if self.absente < 0:
#             return "Studentul nu are atatea absente"
#         else:
#             return f"Studentul mai are {self.absente} absente"
#
#
# class Materii(Catalog):
#
#     def __init__(self, nume, prenume, materie, note):
#         super().__init__(nume, prenume)
#         self.materie = materie
#         self.note = note
#
#
#     def adauga_materie(self, materie, note):
#         return self.materii.update({materie: note})
#
#     def afisare_materii(self):
#         return f"Studentul are materiile {self.materii.keys()}"
#
#     def afisare_situatie_scolara(self):
#         return f"{self.materie} | {sum(list(self.materii[self.materie]))/len(list(self.materii[self.materie]))}"
#
#
#
# student = Catalog("Ion", "Roata")
# student.chiul()
# student.chiul()
# student.chiul()
# student.scutire(2)
#
# student2 = Catalog("George", "Cerc")
# student2.chiul()
# student2.chiul()
# student2.chiul()
# student2.chiul()
# student2.scutire(2)
# print(student.absente)
# print(student2.absente)
#
# student = Materii("Ion", "Roata", "Python", [3, 7, 10])
# student2 = Materii("George", "Cerc", "Python", [7, 9, 10])
#
# student.adauga_materie("Matematica", [2, 6, 9])
# student2.adauga_materie("Romana", [7, 7, 9])
#
#
# print(student.afisare_materii())
# student2.afisare_materii()
# student.afisare_situatie_scolara()
# student2.afisare_situatie_scolara()


################################################################33333333333
#ex 2

# class Catalog:
#
#     meniu = {}
#
#     def __init__(self, nume, pret, gramaj):
#         self.nume = nume
#         self.pret = pret
#         self.gramaj = gramaj
#         self.meniu.update({nume: gramaj})
#
#     def afisare_prajituri(self):
#         meniu_sortat = sorted(self.meniu.items(), key=lambda x: x[1], reverse=True)
#         for i in range(len(meniu_sortat)):
#             if self.nume == meniu_sortat[i][0]:
#                 print(f"Prajitura {meniu_sortat[i][0]} de {meniu_sortat[i][1]}g are pretul de {self.pret}$")
#
#
# class Tort(Catalog):
#
#     def __int__(self, nume, pret, gramaj, glazura="Ciocolata", etajat=False):
#         Catalog.__init__(self, nume, pret, gramaj)
#         self.etajat = etajat
#         self.glazura = glazura
#
#     def afisare_tip_tort(self):
#         if self.etajat:
#             return f"Tortul nostru este etajat si are glazura de {self.glazura}"
#         else:
#             return f"Tortul nostru nu este etajat si are glazura de {self.glazura}"
#
#
#
#
#
# class Fursec(Catalog):
#     pass
#
#
# tort1 = Tort("fabisimo", 100, 2000)
# tort2 = Tort("quatro", 200, 1500)
# tort3 = Tort("fruittyasda", 300, 5000)
#
# fursec1 = Fursec("Ciocolata Neagra", 1.5, 35)
# fursec2 = Fursec("Ciocolata Alba", 3, 70)
# fursec3 = Fursec("Ciocolata Visinie", 20, 50)
#
# tort1.afisare_prajituri()
# tort2.afisare_prajituri()
# tort3.afisare_prajituri()
#
# fursec1.afisare_prajituri()
# fursec2.afisare_prajituri()
# fursec3.afisare_prajituri()
#
# tort1.glazura = 'cacao'
# tort1.etajat = True
# tort1.afisare_tip_tort()
