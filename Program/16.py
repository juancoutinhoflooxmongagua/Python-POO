class CallMe:
    def __init__(self, phone):
        self.phone = phone
    def __call__(self):
        print(f'está chamando {self.phone}')

call1 = CallMe('24342')

call1()