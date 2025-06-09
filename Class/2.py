

class Car:
    def __init__(self, model, velocity):
        self.model = model
        self.velocity = velocity

    def acelerate(self):
        print(f'o {self.model} está acelerando a {self.velocity} por hora')



fusca = Car('Ferrari', 234)
Car.acelerate(fusca)

fusca.acelerate()
print(fusca)