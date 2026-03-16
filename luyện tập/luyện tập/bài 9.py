class SinhVien:
    def __init__(self, ho_ten, diem):
        self.ho_ten = ho_ten
        self.diem = diem

    def __eq__(self, other):
        if not isinstance(other, SinhVien):
            return NotImplemented
        return self.diem == other.diem

    def __str__(self):
        return f"{self.ho_ten} - Điểm: {self.diem}"


sv1 = SinhVien("Nguyễn Đức Long", 8.5)
sv2 = SinhVien("Nguyễn thị thảo linh", 8.5)
sv3 = SinhVien("Lò thuỳ trúc", 7.0)

print(sv1)
print(sv2)
print(sv3)

print("sv1 == sv2 →", sv1 == sv2)
print("sv1 == sv3 →", sv1 == sv3)
print("sv2 == sv3 →", sv2 == sv3)