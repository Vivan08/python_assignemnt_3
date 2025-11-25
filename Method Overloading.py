class animal:
    def __init__(self, name="unknown", species="unknown"):
        self.name = name
        self.species = species
        print(f"Animal created: Name = {self.name}, Species = {self.species}")
a = animal()
b = animal('tiger')
c = animal('lion', 'Mammelian')