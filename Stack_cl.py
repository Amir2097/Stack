class Stack:
    """
    Класс работы со стеком
    """
    def __init__(self, stack: str = ''):
        self.stack = list(stack)

    def is_empty(self):
        """
        Проверка стека на пустоту.
        :return: True или False
        """
        return True if len(self.stack) > 0 else False

    def push(self, item):
        """
        Метод добавляет новый элемент на вершину стека
        """
        self.stack.append(item)

    def pop(self):
        """
        Удаляет верхний элемент стека. Стек изменяется.
        :return: Верхний элемент стека
        """
        return None if len(self.stack) == 0 else self.stack.pop()

    def peek(self):
        """
        :return: Возвращает верхний элемент стека. Стек не меняется
        """
        return self.stack[-1]

    def size(self):
        """
        :return: Возвращает количество элементов в стеке
        """
        return len(self.stack)

