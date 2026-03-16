class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} phát ra âm thanh...")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"{self.name} sủa: Gâu gâu gâu!")


# test
cho = Dog("thảo linh")

cho.sound()

# test kế thừa
print(isinstance(cho, Dog))
print(isinstance(cho, Animal))