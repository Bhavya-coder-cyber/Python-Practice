class TeaLeaf:
    age = 3
    def __init__(self, age):
        self.age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

leaf = TeaLeaf(5)
print(leaf.age)
leaf.age = 10
print(leaf.age)