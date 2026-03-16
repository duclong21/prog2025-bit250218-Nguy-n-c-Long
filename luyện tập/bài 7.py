# Bài 7:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, s):
        if "-" not in s:
            raise ValueError("Chuỗi phải có định dạng name-age")
        name, age_str = s.split("-", 1)
        try:
            age = int(age_str)
        except ValueError:
            raise ValueError("Tuổi phải là số nguyên")
        return cls(name.strip(), age)

    def __str__(self):
        return f"{self.name} - {self.age} tuổi"


#thư
p1 = Person("long", 22)
print(p1)

p2 = Person.from_string("linh-19")
print(p2)
