class SinhVien:
    tong_so_sv = 0

    def __init__(self, ho_ten, diem):
        self.ho_ten = ho_ten
        self.diem = diem
        SinhVien.tong_so_sv += 1

    @classmethod
    def so_luong_sinh_vien(cls):
        return cls.tong_so_sv

    def __str__(self):
        return f"{self.ho_ten} - Điểm: {self.diem}"


#test
print("Trước khi tạo SV:", SinhVien.so_luong_sinh_vien())

sv1 = SinhVien("Nguyễn Đức Long", 8.5)
sv2 = SinhVien("Nguyễn thị thảo linh", 7.0)
sv3 = SinhVien("Lò thuỳ trúc", 9.2)

print("Sau khi tạo 3 SV:", SinhVien.so_luong_sinh_vien())

print(sv1.so_luong_sinh_vien())