import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from lab09.group import Group
from lab08.models import Student

def print_students(title, students):
    print("\n" + title)
    for s in students:
        print(f"{s.fio} | {s.birthdate} | {s.group} | {s.gpa}")
        

g = Group("src/data/lab09/students.csv")

print_students("Изначальный CSV:", g.list())

new_st = Student("Дурова Варвара Дмитриевна", "2007-08-10", "БИВТ-25-8", 4.7)
g.add(new_st)
print_students("После добавления:", g.list())

found = g.find("ов")  # ищем по подстроке
print_students("Поиск 'ов':", found)

g.update("Невейкин Захар Захарович", gpa=4.1, group="БИВТ-21-4")
print_students("После обновления данных Невейкина:", g.list())

g.remove("Желдак Мария Анатольевна")
print_students("После удаления Желдак:", g.list())