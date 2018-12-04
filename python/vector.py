#FIRST \CodeArrayFirst
class Array:
    def __init__(self, length, default):
        if length < 0:
            raise ValueError
        self.length = length
        self.elements = [default] * length
    def __len__(self):
        return self.length
    def __iter__(self):
        return iter(self.elements)
    def __getitem__(self, i):
        if i < 0 or i >= self.length:
            raise IndexError
        return self.elements[i]
    def __setitem__(self, i, x):
        if i < 0 or i >= self.length:
            raise IndexError
        self.elements[i] = x
        return x
#LAST \CodeArrayLast

#FIRST \CodeVectorFirst
class Vector:
    def __init__(self, length, default):
        self.array = Array(length, default)
        self.in_use = 0
        for i in range(length):
            self.add_back(default)
    def __len__(self):
        return self.in_use
    def __iter__(self):
        return VectorIter(self)
    def __getitem__(self, i):
        if i < 0 or i >= self.in_use:
            raise IndexError
        return self.array[i]
    def __setitem__(self, i, x):
        if i < 0 or i >= self.in_use:
            raise IndexError
        self.array[i] = x
        return x
    def add_back(self, x):
        if self.in_use == len(self.array):
            if len(self.array) == 0:
                self._resize(1)
            else:
                self._resize(len(self.array) * 2)
        self.array[self.in_use] = x
        self.in_use += 1
    def remove_back(self):
        self.in_use -= 1
        if (3 * self.in_use) < len(self.array):
            self._resize(len(self.array) // 2)
    def _resize(self, new_capacity):
        new_array = Array(new_capacity, None)
        for i in range(self.in_use):
            new_array[i] = self.array[i]
        self.array = new_array
    def clear(self):
        while self.in_use > 0:
            self.remove_back()

#LAST \CodeVectorLast

#FIRST \CodeVectorIterFirst
class VectorIter:
    def __init__(self, vector):
        self.vector = vector
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == len(self.vector):
            raise StopIteration
        else:
            self.index = self.index + 1
            return self.vector[self.index-1]
#LAST \CodeVectorIterLast

class VectorLog(Vector):
    def __init__(self, length, default):
        super().__init__(length, default)
        self.log = []
        self.extra = {}
    def swap(self, i, j):
        if i != j:
            self.log.append((i,j))
            temp = self.array[i]
            self.array[i] = self.array[j]
            self.array[j] = temp
    def add(self, q):
        self.log.append(q)
    def addExtra(self, **kwargs):
        for key,value in kwargs.items():
            self.extra[key] = value
