class Clothes:
    def __init__(self, name, description, color, size, material):
        self.name = name
        self.description = description
        self.color = color
        self.size = size
        self.material = material

    def visual(self):
        print(f"{self.name} is a {self.size} {self.color} {self.description} made out of {self.material}")
