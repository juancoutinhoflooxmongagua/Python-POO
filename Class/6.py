import json
caminho_arquivo = 'aula.json'

class Person:
    def __init__(self, name, age, lastname):
        self.name = name 
        self.age = age
        self.lastame = lastname





p1 = Person(18, 'Juan', 'COutinho')
p2 = Person(18, 'Juan', 'Marcos')
p3 = Person(18, 'Juan', 'Fernando')

bd = [vars(p1), vars(p2), vars(p3)]

with open (caminho_arquivo, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)