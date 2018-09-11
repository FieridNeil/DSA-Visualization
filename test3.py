class A:
    def __init__(self, elms):
        self.elms = elms


    def show(self, *args):
        print("v2")
        for i in args:
            self.elms.append(i)
        print(self.elms)
#End

a = A([1,2,3,4,5])
a.show()
a.show(6,7,8,9)
