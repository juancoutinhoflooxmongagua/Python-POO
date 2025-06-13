from contextlib import contextmanager

@contextmanager
def my_open(path, modo):
    print('Abrindo arquivo')
    arquive = open(path, modo)
    try:
        yield arquive
    finally:
        print('fechando arquivo')
        arquive.close()

with my_open('testando.txt', 'w') as arquive:
    arquive.write('foi')
    print('WITH', arquive)

print('Fora do bloco with')

with my_open('testando.txt', 'r') as arquive:
    conteudo = arquive.read()
    print(f"Conteúdo do arquivo 'testando.txt': '{conteudo}'")
