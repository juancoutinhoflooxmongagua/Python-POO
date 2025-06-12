class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        if not isinstance(idade, int):
            raise TypeError("A idade deve ser um número inteiro.")
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}(nome="{self.nome}", idade={self.idade})'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta = None

    def __repr__(self) -> str:
        class_name = type(self).__name__
        conta_repr = repr(self.conta) if self.conta is not None else "None"
        return (
            f'{class_name}(nome="{self.nome}", idade={self.idade}, conta={conta_repr})'
        )


if __name__ == "__main__":
    p1 = Pessoa("Alice", 25)
    print(p1)

    c1 = Cliente("Juan", 16)
    print(c1)

    c2 = Cliente("Maria", 30)
    c2.conta = "Conta123"
    print(c2)
