class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # Проверка стека на пустоту.
        return len(self.items) == 0

    def push(self, item):
        # Добавляет новый элемент на вершину стека.
        self.items.append(item)

    def pop(self):
        # Удаляет верхний элемент стека и возвращает его.
        if self.is_empty():
            raise IndexError("Стек пустой")
        return self.items.pop()

    def peek(self):
        # Возвращает верхний элемент стека, но не удаляет его.
        if self.is_empty():
            raise IndexError("Стек пустой")
        return self.items[-1]

    def size(self):
        # Возвращает количество элементов в стеке.
        return len(self.items)

def is_balanced(expression):
    stack = Stack()
    opening = "([{"
    closing = ")]}"
    matches = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != matches[char]:
                return False
    return stack.is_empty()


# Проверка сбалансированности скобок
if __name__ == "__main__":
  test_cases = [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
    "}{",
    "{{[(])]}}",
    "[[{())}]"
]

for expression in test_cases:
    result = is_balanced(expression)
    print(f"{expression}: {'Сбалансировано, количество скобок совпадает' if result else 'Несбалансировано, количество скобок не совпадает'}")  