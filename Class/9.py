class Caneta:
    def __init__(self, cor):  
        self._cor = cor 
    @property
    def cor(self):
        return self._cor  

caneta = Caneta('Azul')
print(caneta.cor) 