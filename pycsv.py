import csv

caminho_do_arquivo = "learning.csv"

with open(caminho_do_arquivo, "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    print(next(leitor))
    print(next(leitor))
    print(next(leitor))
