# date: Mar 6, 2023
# author: Selam Mitike
# file: tree.py a Python program that builds a tree of expression to calculate. it follows operator precedence by using them as a root and by using Stack()
# input: any expression to be calculated
# output: interactive text messages and a solved answer as a decimal

from stack import Stack


class BinaryTree:
    def __init__(self, rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:  # makes a node with the item and makes it the left child
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else: # makes a node with the item and makes it the right child
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self): # returns right child
        return self.rightChild

    def getLeftChild(self): # returns left child
        return self.leftChild

    def setRootVal(self, obj): # sets a root value with obj
        self.key = obj

    def getRootVal(self): # returns the root
        return self.key

    def __str__(self): # when str is called, it returns the tree with parentheses as string
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s


class ExpTree(BinaryTree):
    def make_tree(postfix):
        s = Stack()
        for each in postfix: # iterate through the postfix expression
            if each.isdigit() or each.isdecimal(): # if it's a number add the expression tree to the stack
                s.push(ExpTree(each))
            else: # if it's operator, pop right and left child from the stack
                right_child = s.pop()
                left_child = s.pop()
                temp = ExpTree(each) # make expression tree with the operator, set the right and left child
                temp.rightChild = right_child
                temp.leftChild = left_child
                s.push(temp) # add the tree in the stack
        return s.pop()

    def preorder(tree):
        s = ''
        if tree != None: # in preorder, the root comes first and then calls preorder recursively to add right and left child
            s += (str(tree.getRootVal()))
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s

    def inorder(tree):
        s = ''
        if tree != None:
            if tree.getLeftChild() != None: # if the left exists, add parentheses and add left child by calling inorder recursively
                s += '('
                s = s + ExpTree.inorder(tree.getLeftChild())
            s = s + tree.getRootVal() # add the operator in the middle
            if tree.getRightChild() != None: # close parentheses after adding the right child
                s = s + ExpTree.inorder(tree.getRightChild())
                s += ')'
        return s

    def postorder(tree):
        s = ''
        if tree != None: # the left and right child are added with recursive call and the operator after
            s = s + ExpTree.postorder(tree.getLeftChild())
            s = s + ExpTree.postorder(tree.getRightChild())
            s += (str(tree.getRootVal()))
        return s

    def evaluate(tree):
        if tree == None: # if tree is none do nothing
            return
        else: # iterate through the string tree, if it's number or decimal return the value
            li = []
            s =''
            for each in str(tree):
                if str(tree).isdigit() or each == '.':
                    return str(tree)

                # using the returned value, set the right and left child with recursive call
                left_child = ExpTree.evaluate(tree.getLeftChild())
                right_child = ExpTree.evaluate(tree.getRightChild())
                # do the math using the operator and its left and right childs
                if tree.getRootVal() == '+':
                    return float(left_child) + float(right_child)
                if tree.getRootVal() == '-':
                    return float(left_child) - float(right_child)
                if tree.getRootVal() == '*':
                    return float(left_child) * float(right_child)
                if tree.getRootVal() == '^':
                    return float(left_child) ** float(right_child)

    def __str__(self):
        return ExpTree.inorder(self)


# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree

    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild() == None
    assert r.getRightChild() == None
    assert str(r) == 'a()()'

    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'

    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    # test an ExpTree
    #postfix = '51 20 4 2 - 3 ^ * +'.split()
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    #print(str(tree), 'tree')
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    #print(ExpTree.evaluate(tree), 'lill')
    assert ExpTree.evaluate(tree) == 11.0
    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
    print("---Test BinaryTree()---")
    score1 = 0
    score2 = 0
    score = 0
    print("---Test Stack()---")

    hasStack = False

    hasBinaryTree = False
    try:
        from tree import BinaryTree

        hasBinaryTree = True
    except Exception:
        print("Fail to import BinaryTree()")

    if hasBinaryTree:
        # Test 1
        try:
            r = BinaryTree('a')
            assert r.getRootVal() == 'a'
            assert r.getLeftChild() == None
            assert r.getRightChild() == None
            assert str(r) == 'a()()'
            score1 += 2
        except Exception:
            print("Test 1 fails. +0/2")

        # Test 2
        try:
            r.insertLeft('b')
            assert r.getLeftChild().getRootVal() == 'b'
            assert str(r) == 'a(b()())()'
            score1 += 2
        except Exception:
            print("Test 2 fails. +0/2")

        # Test 3
        try:
            r.insertRight('c')
            assert r.getRightChild().getRootVal() == 'c'
            assert str(r) == 'a(b()())(c()())'
            score1 += 2
        except Exception:
            print("Test 3 fails. +0/2")

        # Test 4
        try:
            r.getLeftChild().insertLeft('d')
            r.getLeftChild().insertRight('e')
            r.getRightChild().insertLeft('f')
            assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
            score1 += 2
        except Exception:
            print("Test 4 fails. +0/2")

        # Test 5
        try:
            assert str(r.getRightChild()) == 'c(f()())()'
            assert r.getRightChild().getLeftChild().getRootVal() == 'f'
            score1 += 2
        except Exception:
            print("Test 5 fails. +0/2")

        print(f'Binary tree: {score1} points')
        hasExpTree = False
        try:
            from tree import ExpTree

            hasExpTree = True
        except Exception:
            print("Fail to import ExpTree()")

        if hasExpTree:
            # test an ExpTree
            # Test 1
            try:
                postfix = '5 2 3 * +'.split()
                tree = ExpTree.make_tree(postfix)
                assert str(tree) == '(5+(2*3))'
                score2 += 2
            except Exception:
                print("Test 1 fails. +0/2")

            # Test 2
            try:
                assert ExpTree.inorder(tree) == '(5+(2*3))'
                assert ExpTree.postorder(tree) == '523*+'
                # assert ExpTree.postorder(tree) == ' 5 2 3 * +'
                assert ExpTree.preorder(tree) == '+5*23'
                # assert ExpTree.preorder(tree) == '+ 5 * 2 3 '
                score2 += 2
            except Exception:
                print("Test 2 fails. +0/2")

            # Test 3
            try:
                assert ExpTree.evaluate(tree) == 11.0
                score2 += 2
            except Exception:
                print("Test 3 fails. +0/2")

            # Test 4
            try:
                postfix = '5 2 + 3 *'.split()
                tree = ExpTree.make_tree(postfix)
                assert str(tree) == '((5+2)*3)'
                assert ExpTree.inorder(tree) == '((5+2)*3)'
                score2 += 2
            except Exception:
                print("Test 4 fails. +0/2")

            # Test 5
            try:
                assert ExpTree.postorder(tree) == '52+3*'
                assert ExpTree.preorder(tree) == '*+523'
                assert ExpTree.evaluate(tree) == 21.0
                score2 += 2
            except Exception:
                print("Test 5 fails. +0/2")
        print(f'Expression tree: {score2} points')

        # output results
        # print(f'stack: {score} points')
        # print(f'binary tree: {score1} points')
        # print(f'expression tree: {score2} points')
        score += score1 + score2
        with open('tmp', 'w') as f:
            f.write(str(score))