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
            print("detalii",nume_task)
        else:
            print(nume_task, "nu e in todolist, doriti sa adaugati?")
            if input() == "da":
                self.todo[nume_task] = input("adauga")
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
todolist_1.afiseaza_detalii_suplimentare("merge")
print(todolist_1.todo)