class BinaryTree:
    def __init__(self,key, rootObj):
        self.key = key
        self.data = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = newNode
        else:
            t = newNode
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = newNode
        else:
            t = newNode
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.data = obj

    def getRootVal(self):
        return self.data

    def __str__(self):
        s = f"{self.key}:{self.data}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

class BST(BinaryTree):
    def find(tree, key):
        if tree == None:
            return None
         # should return the value associated with a given key or None
        if tree.key == key:
            return tree.data
        if key < tree.key:
            if tree.getLeftChild() == None:
                return None
            else:
                return BST.find(tree.getLeftChild(), key)
        else:
            if tree.getRightChild() == None:
                return None
            else:
                return BST.find(tree.getRightChild(), key)

if __name__ == '__main__':
    r = BST(4, 'Daniel')
    r.insertLeft(BST(2, 'Bob'))
    r.insertRight(BST(6, 'Fred'))
    r.getLeftChild().insertLeft(BST(1, 'Anna'))
    r.getLeftChild().insertRight(BST(3, 'Carol'))
    r.getRightChild().insertLeft(BST(5, 'Evan'))
    print(r)

    print(BST.find(r,5))
    assert BST.find(r,5) == 'Evan'

    print(BST.find(r,3))
    assert BST.find(r,3) == 'Carol'

    print(BST.find(r,7))
    assert BST.find(r,7) == None