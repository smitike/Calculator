# date: Mar 6, 2023
# author: Selam Mitike
# file: stack.py a Python program that creates stack
# input: accepts parameter values from calculator.py and tree.py to modify the stack
# output: returns items depending on the method called

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self): # check if stack is empty
        return self.items == []

    def push(self, item): # add item to the stack
        self.items.append(item)

    def pop(self): # remove the last item and return it
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self): # returns the top element without removing
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]

    def size(self): # returns the number of elements
        return len(self.items)


# a driver program for class Stack
if __name__ == '__main__':

    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)

    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]
    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())
    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
    score = 0
    print("---Test Stack()---")

    hasStack = False

    try:
        from stack import Stack

        hasStack = True
    except Exception:
        print("Fail to import Stack()")

    if hasStack:
        # Test 1
        try:
            data_in = ['hello', 'how', 'are', 'you']
            s = Stack()
            for i in data_in:
                s.push(i)
            score += 2
        except Exception:
            print("Test 1 fails. +0/2")

        # Test 2
        try:
            assert s.size() == len(data_in)
            score += 2
        except Exception:
            print("Test 2 fails. +0/2")

        # Test 3
        try:
            assert s.peek() == data_in[-1]
            score += 2
        except Exception:
            print("Test 3 fails. +0/2")

        # Test 4
        try:
            data_out = []
            while not s.isEmpty():
                data_out.append(s.pop())
            score += 2
        except Exception:
            print("Test 4 fails. +0/2")

        # Test 5
        try:
            assert data_out == data_in[::-1]
            assert s.size() == 0
            assert s.peek() == None
            score += 2
        except Exception:
            print("Test 5 fails. +0/2")

    print(f'Stack: {score} points')

    # test classes BinaryTree and ExpTree
    score1 = 0
    score2 = 0