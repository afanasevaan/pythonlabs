from collections import deque
from typing import Any, Optional

class Stack:
    """Стек (LIFO) на базе list."""
    
    def __init__(self):
        self._data = []
    
    def push(self, item: Any) -> None:
        """Добавить элемент на вершину стека."""
        self._data.append(item)
    
    def pop(self) -> Any:
        """Взять элемент с вершины стека."""
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]:
        """Вернуть верхний элемент без удаления."""
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """Проверить, пуст ли стек."""
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Количество элементов в стеке."""
        return len(self._data)
    
    def __str__(self) -> str:
        return f"Stack({self._data})"

class Queue:
    """Очередь (FIFO) на базе collections.deque."""
    
    def __init__(self):
        self._data = deque()
    
    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди."""
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """Взять элемент из начала очереди."""
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустой очереди")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]:
        """Вернуть первый элемент без удаления."""
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        """Проверить, пуста ли очередь."""
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Количество элементов в очереди."""
        return len(self._data)
    
    def __str__(self) -> str:
        return f"Queue({list(self._data)})"