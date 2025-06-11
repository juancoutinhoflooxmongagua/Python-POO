
Foo = type('Foo', (object,), {})
f = Foo()
print(type(f))
print(type(Foo))