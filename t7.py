from abc import ABC, abstractmethod

ex_1 = '''

ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi
'''
print(ex_1)
#The class hase 1 Abstract method and 1 method
class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descriere(self):
        print("Cel mai probabil am colturi. ")
        pass
ex_2 = '''INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de clasa abstracta
'''
print(ex_2)

class Patrat(FormaGeometrica):
    __latura = 1

    def __init__(self, __latura):
        self.__latura = __latura

    def get_latura():
        return Patrat.__latura

    def set_latura(latura_patratului):
        Patrat.__latura = latura_patratului

    def del_latura():
        Patrat.__latura = 0 # pun 0, cu None imi da eroare dupa del

    def aria():
        aria_patrat = Patrat.__latura * Patrat.__latura
        return (f"aria patratului {aria_patrat}")

ex_3 = '''Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte
'''
ex_4 = '''POLYMORPHISM 
Definiti o noua metoda descrie() - printati ‘Eu nu am colturi’

Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui
'''
class Cerc(FormaGeometrica):
    __raza = 0
    def __init__(self, __raza):
        Cerc.__raza = __raza
    def get_raza():
        return Cerc.__raza
    def set_raza( raza_cercului):
        Cerc.__raza = raza_cercului
    def del_raza():
        Cerc.__raza = 0 # daca pun Cerc.__raza = None imi da eroare la calcul arie
    def aria():
        aria_cercului = FormaGeometrica.PI * Cerc.__raza * Cerc.__raza
        return (f"aria cercului {aria_cercului}")
    def descriere():
        print("Eu nu am colturi")
patrat_test = Patrat
cerc_test = Cerc
print(cerc_test.descriere())
cerc_test.set_raza(5)
print(cerc_test.aria())
print(cerc_test.get_raza())
print(cerc_test.del_raza())
print(cerc_test.get_raza())
print(cerc_test.aria())
patrat_test.set_latura(6)
print(patrat_test.aria())
print(patrat_test.descriere())
print(patrat_test.get_latura())
patrat_test.del_latura()
print(patrat_test.aria())
print(patrat_test.descriere())
print(patrat_test.get_latura())


