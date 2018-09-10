class A():
    def __init__(self):
        self.var = "Hi"

    def show(self):
        print(self.var)


class B(A):
    def __init__(self, *args, **kwargs):
        super().__init__()


    def update(self, *args, **kwargs):
        for thing in args:
            self.var += thing

    def show(self):
        super().show()


b = B('!', ' ', 'how are you?')
b.update('\nI am fine, how about you?')
b.var += "\nI'm great!"
b.show()
