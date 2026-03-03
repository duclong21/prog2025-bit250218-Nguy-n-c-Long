# Bài 3

mau_sac = ["Red", "Blue", "Pink", "Green", "Orange"]

print("Danh sách ban đầu:", mau_sac)

try:
    mau_sac.remove("Green")
    print("Đã xóa Green thành công!")
except:
    print("Không tìm thấy màu Green trong danh sách.")

print("Danh sách sau khi xử lý:", mau_sac)