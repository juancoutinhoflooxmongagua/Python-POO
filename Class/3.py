

class Animal:
    def __init__(self, name):
        self.name = name
    
    def comendo(self, alimento):
        return(f'{self.name} está comendo {alimento}')

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal('Leão')

print(leao.name)

print(leao.executar('Maçã'))