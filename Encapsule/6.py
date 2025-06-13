class A:
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

class C(A):
    ...

    def quem_sou(self):
        print('C')


class D(B, C):
    ...

    def quem_sou(self):
        print('D')


d = D()
d.quem_sou()
# print(D.__mro__)
print(D.mro())