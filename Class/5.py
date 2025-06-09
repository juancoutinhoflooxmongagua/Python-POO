

class Person: 
    ano_atual = 2025

    def __init__(self, age, name):
        self.name = name
        self.age = age

    def get_ano_nascimento(self):
        return self.ano_atual - self.age

p1 = Person(18, 'Juan')
print(p1.get_ano_nascimento())

print(vars(p1))