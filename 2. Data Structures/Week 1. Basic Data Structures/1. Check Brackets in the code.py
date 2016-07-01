import re

def test_stack():
    stack = my_stack()
    print stack.pop()
    stack.push('Aleh')
    stack.push('Darashenka')
    print len(stack)
    print stack.pop()
    print len(stack)
    print stack.pop()
    print len(stack)

class my_stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.stack:
            element = self.stack[-1]
            self.stack = self.stack[:-1]
            return element
        else:
            print 'Stack is empty'

    def push(self, a):

        self.stack.append(a)

    def __len__(self):
        return len(self.stack)


def input():
    return 'fo}o(bar[i);'



def check_brackets():
    idx = 0
    stack = []
    code =  input()
    for char in code:
        idx+=1

        if not re.match('[^\{\}\[\]\(\)]',char):
            if char in ['[','{','(']:
                stack.append(char)
            else:
                if stack:
                    top = stack.pop()
                    if (top == '[' and char !=']') or (top == '(' and char !=')') or (top == '{' and char !='}'):
                        return idx
                else:
                    return idx
    if stack:
        return stack
    else:
        return 'Success'


if __name__ == '__main__':
    print test_stack()