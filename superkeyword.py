class A:
    a=10
    def __init__(self):
        print('constructor')
class B(A):
    b=20
    def __init__(self):
        super().__init__(self)
        print('b class')
        def f2(self,b):
            super().f1()
            (super(a))
        print(self.b)
ob=B()
ob.f2(30)
