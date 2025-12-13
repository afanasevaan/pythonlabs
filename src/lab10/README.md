# Лабораторная работа 10: Структуры данных

## Теория

### Стек (Stack)
- **Определение**: структура данных LIFO (Last In, First Out)
- **Основные операции**:
  - `push(item)` - добавление элемента на вершину (O(1))
  - `pop()` - удаление элемента с вершины (O(1))
  - `peek()` - просмотр вершины (O(1))
- **Реализация**: на базе list, вершина - последний элемент

### Очередь (Queue)
- **Определение**: структура данных FIFO (First In, First Out)
- **Основные операции**:
  - `enqueue(item)` - добавление в конец (O(1))
  - `dequeue()` - удаление из начала (O(1))
  - `peek()` - просмотр начала (O(1))
- **Реализация**: на базе collections.deque для эффективного удаления из начала

### Односвязный список (Singly Linked List)
- **Определение**: динамическая структура из узлов, каждый содержит значение и ссылку на следующий
- **Основные операции**:
  - `append(value)` - добавление в конец (O(1) с tail)
  - `prepend(value)` - добавление в начало (O(1))
  - `insert(idx, value)` - вставка по индексу (O(n))
  - `remove(value)` - удаление по значению (O(n))

## Реализация

### Классы в structures.py

#### Stack
```python
class Stack:
    def __init__(self):
        self._data = []  # Хранилище на базе list
    
    def push(self, item):  # O(1)
    def pop(self):         # O(1)
    def peek(self):        # O(1)
    def is_empty(self):    # O(1)
```

#### Queue
```python
class Queue:
    def __init__(self):
        self._data = deque()  # Хранилище на базе deque
    
    def enqueue(self, item):  # O(1)
    def dequeue(self):        # O(1)
    def peek(self):           # O(1)
    def is_empty(self):       # O(1)
```

### Классы в linked_list.py
#### Node
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

#### SinglyLinkedList
```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Для O(1) добавления в конец
        self._size = 0
    
    def append(self, value):    # O(1)
    def prepend(self, value):   # O(1)
    def insert(self, idx, value):  # O(n)
    def remove_at(self, idx):   # O(n)
    def remove(self, value):    # O(n)
```

## Примеры использования

### Stack 
```python
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # 2
print(stack.peek())  # 1
```

### Queue
```python
queue = Queue()
queue.enqueue("first")
queue.enqueue("second")
print(queue.dequeue())  # "first"
print(queue.peek())  # "second"
```

### SinglyLinkedList
```python
lst = SinglyLinkedList()
lst.append(1)
lst.append(2)
lst.prepend(0)
print(list(lst))  # [0, 1, 2]
```
![im01.png](/images/lab10/im01.png)

### Выводы по бенчмаркам

Стек и очередь демонстрируют высокую производительность благодаря использованию оптимизированных структур Python (list и deque). Их основные операции имеют сложность O(1).

Связный список, несмотря на O(1) для операций в начале, на практике работает медленнее из-за:
- Необходимости создания объектов Node для каждого элемента
- Отсутствия локальности данных в памяти
- Дополнительных операций с указателями

**Итог:** Для большинства задач в Python оптимальны встроенные list/deque. Связные списки полезны в специфических сценариях с частыми вставками в начало.


