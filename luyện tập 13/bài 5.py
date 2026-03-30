class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Flower: {self.name} - Color: {self.color}"

hoa = Flower("Rose", "Red")
print(hoa)

hoa2 = Flower("Sunflower", "Yellow")
print(hoa2)