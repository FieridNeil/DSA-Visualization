import random
from vector import *
def in_place_selection_sort(V):
    for k in range(len(V) - 1):
        least_index = k
        for i in range(k+1, len(V)):
            if V[i] < V[least_index]:
                least_index = i
        V.swap(k, least_index)
    return V
#end selection sort

def inplace_quick_sort(V):
    return inplace_quick_sort_range(V, 0, len(V))

def inplace_quick_sort_range(V, s, e):
    if (e-s) >= 2:
        lte, eqe = inplace_partition(V, s, e)
        inplace_quick_sort_range(V, s, lte)
        inplace_quick_sort_range(V, eqe, e)
    return V

def inplace_partition(V, s, e):
    pivot = V[random.randint(s, e-1)]
    V.addpivot(pivot)
    lte = s
    ges = e
    while lte < ges:
        if V[lte] < pivot:
            lte += 1
        elif V[ges-1] >= pivot:
            ges -= 1
        else:
            V.swap(lte, ges-1)
            lte += 1
    eqe = lte
    for i in range(ges, e):
        if V[i] == pivot:
            V.swap(eqe, i)
            eqe += 1
    return lte, eqe

def sequential_search(V, q):
    for i, e in enumerate(V):
        V.add(i)
        if e == q:
            return e
    return None

def binary_search(V, q):
    return binary_search_range(V, q, 0, len(V))

def binary_search_range(V, q, s, e):
    V.add([s, e])

    if s == e:
        return None
    else:
        half = (s + e) // 2
        if q < V[half]:
            return binary_search_range(V, q, s, half)
        elif q == V[half]:
            return half
        else:
            return binary_search_range(V, q, half+1, e)

def merge_sort(V):
    if len(V) <= 1:
        return V
    else:
        half = len(V) // 2
        L = V[:half]
        R = V[half:]
        return merge(merge_sort(L), merge_sort(R))

def merge(L, R):
    S = Vector(0, 0)
    li = ri = 0
    while li < len(L) and ri < len(R):
        if L[li] <= R[ri]:
            S.add_back(L[li])
            li += 1
        else:
            S.add_back(R[ri])
            ri += 1
    for i in range(li, len(L)):
        S.add_back(L[i])
    for i in range(ri, len(R)):
        S.add_back(R[i])
    return S

class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val


class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if(currentNode is None):
            return False
        elif(val == currentNode.val):
            return True
        elif(val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)
