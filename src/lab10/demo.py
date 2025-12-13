from structures import Stack, Queue
from linked_list import SinglyLinkedList

def demo_stack():
    print("=== Демонстрация работы Stack ===")
    stack = Stack()
    
    # Добавление элементов
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack после push: {stack}")
    
    # Просмотр вершины
    print(f"peek(): {stack.peek()}")
    
    # Извлечение
    print(f"pop(): {stack.pop()}")
    print(f"pop(): {stack.pop()}")
    print(f"Stack после pop: {stack}")
    
    # Проверка на пустоту
    print(f"is_empty(): {stack.is_empty()}")
    print()

def demo_queue():
    print("=== Демонстрация работы Queue ===")
    queue = Queue()
    
    # Добавление элементов
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print(f"Queue после enqueue: {queue}")
    
    # Просмотр первого элемента
    print(f"peek(): {queue.peek()}")
    
    # Извлечение
    print(f"dequeue(): {queue.dequeue()}")
    print(f"dequeue(): {queue.dequeue()}")
    print(f"Queue после dequeue: {queue}")
    
    # Проверка на пустоту
    print(f"is_empty(): {queue.is_empty()}")
    print()

def demo_linked_list():
    print("=== Демонстрация работы SinglyLinkedList ===")
    lst = SinglyLinkedList()
    
    # Добавление в конец
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(f"После append: {lst}")
    
    # Добавление в начало
    lst.prepend(0)
    print(f"После prepend(0): {lst}")
    
    # Вставка по индексу
    lst.insert(2, 1.5)
    print(f"После insert(2, 1.5): {lst}")
    
    # Удаление по индексу
    lst.remove_at(3)
    print(f"После remove_at(3): {lst}")
    
    # Удаление по значению
    lst.remove(1.5)
    print(f"После remove(1.5): {lst}")
    
    # Итерация
    print("Элементы через итератор:")
    for item in lst:
        print(f"  {item}")
    
    print(f"Длина списка: {len(lst)}")
    print(f"Строковое представление: {lst}")
    print(f"Repr: {repr(lst)}")

if __name__ == "__main__":
    demo_stack()
    demo_queue()
    demo_linked_list()