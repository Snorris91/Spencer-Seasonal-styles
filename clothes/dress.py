from .clothes import Clothes
from season import Spring

class Dress(Clothes, Spring):
    def __init__(self, name, description, color, size, material, sex, age):
        self.sex = sex
        self.age = age
        Clothes.__init__(self, name, description, color, size, material)
        Spring.__init__(self)
        # put season here
        # put area here
