import matplotlib.pyplot as plt

categories = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yếu', 'Kém']
so_luong = [6, 10, 12, 4, 1]


plt.figure(figsize=(8, 5))
plt.bar(categories, so_luong, color=['#4CAF50', '#2196F3', '#FF9800', '#F44336', '#9E9E9E'])

plt.title('Phân bố kết quả học tập của lớp', fontsize=14, fontweight='bold')
plt.xlabel('Xếp loại', fontsize=12)
plt.ylabel('Số lượng học sinh', fontsize=12)

for i, v in enumerate(so_luong):
    plt.text(i, v + 0.1, str(v), ha='center', fontsize=11)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()