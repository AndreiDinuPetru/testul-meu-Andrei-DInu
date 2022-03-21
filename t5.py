import math
from datetime import datetime
from datetime import date
import calendar
from calendar import monthrange
ex_1='''1. Functie care sa calculeze si sa returneze suma a 2 numere
'''
print(ex_1)
def suma_doua(nr1, nr2):
    suma = nr1 + nr2
    return suma
print(f"suma este {+suma_doua(8, 15)} ")
ex_2='''2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar'''
print(ex_2)
def paritate_numar (numar):
    if numar % 2 ==0:
        return True
    else:
        return False
print(paritate_numar(-9))
ex_3='''3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) 
'''
print(ex_3)
def caractere_nume(nume):
    nr_de_caractere=len(nume)
    return nr_de_caractere
print(caractere_nume("Andrei Dinu Petru"))
def litere_nume(nume):
    spatii_goale = 0
    for index in range(len(nume)):
        if nume[index] == " ":
            spatii_goale+=1
    return caractere_nume(nume)-spatii_goale
print(litere_nume("Andrei Dinu Petru"))
ex_4='''4. Functie care returneaza aria dreptunghiului'''
print(ex_4)
def arie_drept(L,l):
    if l>0 and L>0:
        arie=2*(L+l)
        return arie
    else:
        return "Nu este dreptunghi"
print(arie_drept(9.4,0.6))
ex_5='''5. Functie care returneaza aria cercului'''
def arie_cerc(r):
    if r>0:
        arie=math.pi*r*r
        return  arie
    else:
        return "nu este cerc"
print(arie_cerc(-2.5))
ex_6='''6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
'''
print(ex_6)
def caracter_existent(caracter, string):
    car_string = 0
    for index in range(len(string)):
        if string[index] == caracter:
            car_string += 1
    if car_string > 0:
        return True
    else:
        return False
print(caracter_existent("A" , "Andrei Dinu Petru"))
ex_7='''7. Functie fara return, primeste un string si printeaza pe ecran:
Nr de caractere lower case este x
Nr de caractere upper case exte y 
'''
print(ex_7)
def lower_uper(string):
    count_lower = 0
    count_upper = 0
    count_special = 0
    for a in string:
        if (a.isupper()):
            count_upper += 1
        elif (a.islower()):
            count_lower += 1
        else:
            count_special += 1
    print(f"upper {count_upper}, lower {count_lower}, speciale {count_special}")
print(lower_uper("Andrei Dinu Petru"))
ex_8='''8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive'''
print(ex_8)
def poz_list(numere):
    pozitiv=[]
    for a in numere:
        if a >= 0 :
            pozitiv.append(a)
    return  pozitiv
print(poz_list([2,9,6,-9,0,-65]))
ex_9='''9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale. 
'''
print(ex_9)
def max_of_2_numbers(x_1, x_2):
    if x_1>x_2:
        return x_1
    elif x_2>x_1:
        return x_2
    else:
        return ("numere egale")
print(max_of_2_numbers(12,-89))
ex_10='''10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
'''
print(ex_10)
def numar_in_set(my_number, my_set):
    if my_number in my_set:
        print(f"nu am adaugat numarul in set. Acesta exista deja");print(my_set)
        return False
    else:
        my_set.add(my_number)
        print(f"am adaugat numarul nou in set");print(my_set)
        return True
print(numar_in_set(6,{6,9,7}))
ex_11='''11. Functie care primeste o luna din an si returneaza cate zile are acea luna'''
print(ex_11)
def nr_zile_luna (luna):
    if luna in range (1,13):
        num_days = monthrange(2022, luna)[1]
        return num_days
    else:
        return f"nu exista luna {luna}"
print(nr_zile_luna(6))
#print(nr_zile_luna(int(input(f"luna este "))))
ex_12='''12. Functie calculator care sa returneze 4 valori 
Suma, diferenta, inmultirea, impartirea a 2 numere

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
'''
def adunare(nr_1, nr_2):
    a=nr_1+nr_2
    return a
def scadere(nr_1, nr_2):
    b=nr_1-nr_2
    return b
def imultire(nr_1, nr_2):
    c=nr_1*nr_2
    return c
def impartire(nr_1, nr_2):
    if nr_2!=0:
        d=nr_1/nr_2
        return d
    else:
        return "impartirea cu 0 nu se poate"
def calculator(nr_1, nr_2):
    print("Suma: ", adunare(nr_1,nr_2))
    print("Diferenta: ", scadere(nr_1,nr_2))
    print("Inmultirea: ", imultire(nr_1,nr_2))
    print("Impartirea: ", impartire(nr_1,nr_2))
print(calculator(10,-8))
ex_13='''13. Functie care primeste o lista de cifre (adica doar 0-9)
Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''
print(ex_13)
def frecventa (lista1):
    dict1 = {index: lista1.count(index) for index in range(10)}
    for i in lista1:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
    return dict1
print(frecventa([1, 3, 1, 5, 9, 7, 7, 5, 5]))
ex_14='''14. Functie care primeste 3 numere
Returneaza valoarea maxima dintre ele
'''
print(ex_14)
def max_of_3_numbers(x_1, x_2, x_3):
    max=0
    if x_1>x_2 and x_1>x_3:
        max=x_1
    elif x_2>x_3 and x_2>x_1:
        max=x_2
    elif x_3>x_1 and x_3>x_2:
        max=x_3
    elif x_3==x_1==x_2:
        max=x_3
    return max
print(max_of_3_numbers(6,9,8))
ex_15='''15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
Ex: daca dam nr 3
Suma va fi 6 (0+1+2+3)
'''
print(ex_15)
def suma_all_nr(n):
    suma=(n*(n+1))/2
    return  suma
print(suma_all_nr(9))
ex_16='''16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
‘Numele este de baiat’ sau ‘Numele este de fata’
'''
ex_17='''17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
Returnati numerele comune 

Ex:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
'''
print(ex_17)
def list_intersection(lista1, lista2):
    list1_as_set = set(lista1)
    intersection = list1_as_set.intersection(lista2)
    return intersection
print(list_intersection([1, 1, 2, 3],[2, 2, 3, 4]))
ex_18='''18. Functie care sa aplice o reducere de pret
Daca produsul costa 100 lei si aplicam reducere de 10%
Pretul va fi 90
Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
'''
print(ex_18)
def reduction(price, discount):
    if discount in range(0,101):
        price_with_discount=price - ( price * discount / 100 )
        return price_with_discount
    else:
        print('discont prea mare')
print(reduction(102,50))
ex_19='''19. Functie care sa afiseze data si ora curenta'''
print(ex_19)
def ora_curenta():
    now=datetime.now()
    return now
print(ora_curenta())
ex_20='''20. Functie care sa afiseze cate zile mai sunt pana la ziua ta /
 sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
'''
print(ex_20)
def a_mai_rams (year, month, day):
    today = date.today()
    birthday = date(year, month, day)
    delta = birthday - today
    return delta
print(a_mai_rams(2023, 1, 16))