class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def __eq__(self, other):
        return self.nombre == other.nombre and self.apellido == other.apellido


p1 = Persona("Jon", "Snow")
p3 = Persona("Jon", "Snow")
p2 = Persona("Daenerys", "Targaryen")
print(p1 == p3)
print(id(p1), id(p3))
            