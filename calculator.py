# date: Mar 6, 2023
# author: Selam Mitike
# file: calculator.py a Python program that convertes infix to postfix to calculate it in tree.py.
# input: any expression to be calculated
# output: interactive text messages and a solved answer as a decimal


import tree
from stack import Stack

def infix_to_postfix(infix):
    opStack = Stack()
    postfix = ''
    num = ''
    prec = {} # create dict based on the operators precendence order
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
# loop through the infix expression
    for char in infix:
        if char.isdigit() or char == '.': # if it's number or decimal, add it to num(useful for multidigit numbers and decimals)
            num += char
        elif not char.isdigit() or not char == '.':
            postfix += num
            if len(num) != 0: # adds space after adding num to postfix
                postfix += ' '
            num = ''
            if char == '(':
                opStack.push(char)
            elif char == ')': # if parentheses is closed, add items that are in parentheses from stock to postfix
                top = opStack.pop()
                while top != '(':
                    postfix += top
                    top = opStack.pop()
            else:  # if the operator in the stack has high precendence, remove it and add it to postfix
                while not opStack.isEmpty() and prec[opStack.peek()] >= prec[char]:
                    postfix += opStack.pop()
                opStack.push(char)
    # add the rest from num and the stack to postfix
    postfix += num
    if len(num) != 0:
        postfix += ' '
    while not opStack.isEmpty():
        postfix += opStack.pop()
    postfix1 = ''
    # check if a space is not missing, if it is add space in the postfix
    for i in range(len(postfix)):
        if i != len(postfix)-1:
            if postfix[i] == '+' or postfix[i] == '-' or postfix[i] == '/' or postfix[i] == '*' or postfix[i] == '^':
                if postfix[i+1] != ' ':
                    postfix1 += postfix[i]
                    postfix1 += ' '
            else:
                postfix1 += postfix[i]
        else:
            postfix1 += postfix[i]
    return  postfix1   #' '.join(postfix)

def calculate(infix):
    post = infix_to_postfix(infix)  # convert the expresion into postfix
    return tree.ExpTree.evaluate(tree.ExpTree.make_tree(post.split())) # make a tree and evaluate the expression


# a driver to test calculate module
if __name__ == '__main__':
    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
    expression = input('Welcome to Calculator Program!\nPlease enter your expression here. To quit enter \'quit\' or \'q\':')
    if expression != 'q' or expression != 'quit':
        print(calculate(expression))
        # keep asking to enter until user types quit/q
        while expression != 'q' or expression != 'quit':
            expression = input('Please enter your expression here. To quit enter \'quit\' or \'q\':')
            if expression == 'q' or expression == 'quit':
                print('Goodbye!')
                break
            else:
                print(calculate(expression))





