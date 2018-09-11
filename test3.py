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
        return self.array[i]
    def __setitem__(self, i, x):
        if i < 0 or i >= self.length:
            raise IndexError
        self.array[i] = x
#LAST \CodeArrayLast

class Vector:
    def __init__(self, length, default):
        self.array = Array(0, default)
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
    def add_back(self, x):
        if self.in_use == len(self.array):
            self._resize(len(self.array) * 2)
        self.array[self.in_use] = x
        self.in_use += 1
    def remove_back(self):
        if self.in_use == 0:
            raise UnderflowError
        self.in_use -= 1
        if (3 * self.in_use) < len(self.array):
            self._resize(self._capacity() // 2)
    def _resize(self, new_capacity):
        new_array = Array(new_capacity, None)
        for i in range(self.in_use):
            new_array[i] = self.array[i]
        self.array = new_array
#LAST \CodeVectorLast


v = Vector(10, 0)
