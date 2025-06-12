from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    idade: int
    status: str = field(init=False)

    def __post_init__(self):
        if self.idade < 0:
            raise ValueError("A idade não pode ser um número negativo.")

        if self.idade >= 18:
            self.status = "Maior de idade"
        else:
            self.status = "Menor de idade"


try:
    p1 = Person(name="Ana", idade=30)
    print(p1)
    print(p1.status)
except ValueError as e:
    print(e)

print("-" * 20)

try:
    p2 = Person(name="Beto", idade=15)
    print(p2)
    print(p2.status)
except ValueError as e:
    print(e)

print("-" * 20)

try:
    p3 = Person(name="Carlos", idade=-5)
    print(p3)
except ValueError as e:
    print(e)
