import math
from datetime import date
ex_1='''Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria 
diametru() 
circumferinta()
'''
print(ex_1)
class Cerc:
    raza=1
    color=None
    def __init__(self, raza, color):
        self.raza = raza
        self.color = color
    def descriere_cerc(self):
        return (f"culoarea este ",self.color, f"raza este", self.raza)
    def aria(self):
        arie=math.pi*self.raza*self.raza
        return (f"aria este", arie)
    def diametru(self):
        diametru_cerc=self.raza*2
        return (f"diametru este", diametru_cerc)
    def circumerinta(self):
        circumferinta_cerc = 2*math.pi*self.raza
        return (f"circumferinta este", circumferinta_cerc)
cerc_1 = Cerc(8,'alb')
print(cerc_1.descriere_cerc())
print(cerc_1.aria())
print(cerc_1.diametru())
print(cerc_1.circumerinta())
ex_2='''2. 
Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
descrie() va PRINTA lungime, latime, culoare
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. 
Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. 
Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''
print(ex_2)
class Dreptunghi:
    lungime = 1
    latime = 1
    color = None
    def __init__(self, lungime, latime, color):
        self.lungime = lungime
        self.latime = latime
        self.color = color
    def descriere(self):
        return (f"lungimea=", self.lungime, f"latimea=", self.latime, f"culoare=", self.color)
    def aria(self):
        arie = self.latime * self.lungime
        return (f"aria este", arie)
    def perimetru(self):
        perim = (self.latime + self.lungime) * 2
        return ("perimetrul este ", perim)
    def schimba_culoarea(self, noua_culoare):
        self.color = noua_culoare
dreptunghi_1 = Dreptunghi(10,9,"rosu")
print(dreptunghi_1.descriere())
print(dreptunghi_1.aria())
print(dreptunghi_1.perimetru())
dreptunghi_1.schimba_culoarea("mov")
print(dreptunghi_1.descriere())
ex_3='''3.
Clasa Angajat

Atribute: nume, prenume, salariu

Constructor() pt toate atributele // constructor reprezinta __init__

Metode:
descrie() print nume, prenume, salariu
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''
print(ex_3)
class Angajat:
    nume = ""
    prenume = ""
    salariu = 1
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
    def descriere(self):
        print("nume", self.nume, "prenume", self.prenume, "salariu", self.salariu)
    def nume_complet(self):
        full_name = self.prenume + " " + self.nume
        return ('numele complet ', full_name)
    def salariu_lunar(self):
        sal_luna = self.salariu
        return ("salariu lunar este", sal_luna)
    def salariu_anual(self):
        sal_an = self.salariu * 12
        return ("salariu anual este", sal_an)
    def marire_salariu(self, procent):
        sal_nou = self.salariu * (procent / 100) + self.salariu
        self.salariu = sal_nou
        return sal_nou
angajat_1 = Angajat("Dinu", "Andrei", 5000)
angajat_1.descriere()
print(angajat_1.nume_complet())
print(angajat_1.salariu_lunar())
print(angajat_1.salariu_anual())
angajat_1.marire_salariu(10)
angajat_1.descriere()
print(angajat_1.nume_complet())
print(angajat_1.salariu_lunar())
print(angajat_1.salariu_anual())
ex_4='''4.
Clasa Factura

Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie),
 numar, nume_produs, cantitate, pret_buc

Constructor: toate atributele, fara serie

Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total “
Telefon |      7       |       700       | 49000     
'''
print(ex_4)
class Factura:
    serie = "SF"
    numar = 1
    nume_produs = None
    cantitate = 1
    pret_buc = 1
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
    def schimbati_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua
    def schimbati_pret(self, pret_nou):
        self.pret_buc = pret_nou
    def schimbati_nume(self, nume_nou):
        self.nume_produs = nume_nou
    def genereaza_factura(self):
        today = date.today()
        total = self.cantitate * self.pret_buc
        print("Factura seria ", self.serie, "numar", self.numar)
        print(today)
        print("Produs           | cantitate | pret bucata | Total")
        print(self.nume_produs," | ", self.cantitate,"       | ", self.pret_buc,"      | ", total)
factura_1 = Factura(1, "Telefon Samsung", 6, 1254)
factura_1.genereaza_factura()
ex_='''5. 
Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''
class Cont:
    iban = 1234567890123
    titular_cont = ""
    sold = 0
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print("titularul ", self.titular_cont, "are in contul ", self.iban, "suma de", self.sold, "lei" )
    def debitare_cont(self, suma):
        self.sold = self.sold + suma
    def creditare_cont(self, suma):
        self.sold = self.sold - suma
cont_1 =Cont(5748, "Dinu", 450)
cont_1.afisare_sold()
cont_1.debitare_cont(1000)
cont_1.afisare_sold()
cont_1.creditare_cont(2544)
cont_1.afisare_sold()
ex_6='''6.
Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, 
altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare,
 daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0
'''
print(ex_6)
class Masina:
    marca = "BMW"
    model ="Seria 3"
    viteza_maxima = 130
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibile = {"alb", "negru", "mov", "metalizat", "albastru", "rosu", "galben taxi"}
    inmatriculata = False
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
    def descriere(self):
        print("\n Marca:", self.marca, "\n Model:", self.model, "\n Viteza Maxima:", self.viteza_maxima, "\n Viteza actuala:", self.viteza_actuala, "\n Culoare:", self.culoare, "\n Inmatriculata:", self.inmatriculata)
    def inmatriculare(self):
        self.inmatriculata = True
    def vopseste(self, color):
        if color in self.culori_disponibile:
            self.culoare = color
        else:
            print(f"Culoarea nu este disponibila, incercati din culorile {self.culori_disponibile}")
    def acelereaza(self, speed):
        if speed < 0:
            print(f"viteza e negativa")
        elif speed > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = speed
    def franeaza(self):
        self.viteza_actuala = 0
car_1 = Masina(" i ", 185)
car_1.descriere()
car_1.inmatriculare()
car_1.descriere()
car_1.vopseste("violet")
car_1.vopseste("alb")
car_1.descriere()
car_1.acelereaza(-15)
car_1.acelereaza(90)
car_1.descriere()
car_1.acelereaza(1587)
car_1.descriere()
car_1.franeaza()
car_1.descriere()
ex_7='''7. Clasa TodoList
 
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in functie de numele taskului, 
printam detalii suplimentare daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict

'''
print(ex_7)
class TodoList:
    todo = {}
    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
    def finalizeaza_task(self, nume):
        self.todo.pop(nume)
todolist_1 = TodoList()
todolist_1.adauga_task("1","2")
print(todolist_1.todo)
todolist_1.finalizeaza_task("1")
print(todolist_1.todo)
ex_7 = '''7. Clasa TodoList

Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in functie de numele taskului, 
printam detalii suplimentare daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict

'''
print(ex_7)
class TodoList:
    todo = {}
    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
    def finalizeaza_task(self, nume):
        self.todo.pop(nume)
    def afiseaza_todo_list(self):
        print(list(self.todo.keys()))
    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo.keys():
            print(nume_task)
        else:
            print(nume_task, "nu e in todolist, doriti sa adaugati?")
            if input() == "da":
                self.todo[nume_task] = input('adauga ')
            else:
                print("la revedere")
todolist_1 = TodoList()
todolist_1.adauga_task("buy","bread")
todolist_1.adauga_task("play","teniss")
todolist_1.adauga_task("drink","beear")
todolist_1.adauga_task("sleap","night")
print(todolist_1.todo)
todolist_1.finalizeaza_task("buy")
print(todolist_1.todo)
todolist_1.afiseaza_todo_list()
todolist_1.afiseaza_detalii_suplimentare("alergat")
print(todolist_1.todo)
