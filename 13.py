

class MyContextManager:
    def __init__(self, caminho, modo):
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        print('abrindo arquivo')
        return open(self.caminho, self.modo)
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('saindo')
        self._arquivo.close()
        print('exit')

instance = MyContextManager('arquivo.text', 'w')

with instance as arquivo:
    arquivo.write('LInha1')
    print('WITH', arquivo)