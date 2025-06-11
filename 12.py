class A:
    def __new__(cls):
        instancia = super().__new__(cls) 
        print('Criando instancia')
        return instancia
    def __init__(self):
        print('sou o init')
    def __repr__(self):
        return 'A()'

a = A()

print(a)