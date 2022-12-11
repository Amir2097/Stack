from Stack_cl import Stack

def balanced(data_stack: Stack):
    """
    Метод на проверку сбалансированности скобок
    :param data_stack: Класс работы со стеками
    :return:
    """
    if data_stack.size() % 2 == 0 and data_stack.is_empty():
        empty_stack = Stack()

        for data_stacks in data_stack.stack:
            if data_stacks in '([{':
                empty_stack.push(data_stacks)
            elif data_stacks in '}])':

                if empty_stack.size() == 0:
                    break

                last_return_stack = empty_stack.pop()
                if last_return_stack == '(' and data_stacks == ')' or last_return_stack == '[' and data_stacks == ']' \
                        or last_return_stack == '{' and data_stacks == '}':
                    continue

        if empty_stack.size() == 0:
            print('Balanced')
            return True

        elif empty_stack.peek() in '([{':
            print('Not balanced')
            return False

    else:
        print('Not balanced')
        return False



if __name__ == '__main__':
    stack = Stack('(((([{}]))))')
    print(f"{balanced(stack)} - 1")
    stack1 = Stack('[([])((([[[]]])))]{()}')
    print(f"{balanced(stack1)} - 2")
    stack2 = Stack('{{[()]}}')
    print(f"{balanced(stack2)} - 3")
    stack3 = Stack('}{}')
    print(f"{balanced(stack3)} - 4")
    stack4 = Stack('{{[(])]}}')
    print(f"{balanced(stack4)} - 5")
    stack5 = Stack('[[{())}]')
    print(f"{balanced(stack5)} - 6")
    stack6 = Stack('()((((((((((((((((((')
    print(f"{balanced(stack6)} - 7")

