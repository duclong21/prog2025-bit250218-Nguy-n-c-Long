import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu Top 10 thành phố California theo diện tích đất
# Nguồn:Wikipedia
thanh_pho = [
    'Los Angeles', 'San Diego', 'California City', 'San Jose',
    'Bakersfield', 'Fresno', 'Palmdale', 'Lancaster',
    'Sacramento', 'Stockton'
]

dien_tich_km2 = [1215, 842, 527, 461, 394, 300, 274, 244, 259, 161]  # km²

plt.figure(figsize=(12, 7))
bars = plt.barh(thanh_pho, dien_tich_km2, color='cornflowerblue', height=0.6)

for bar in bars:
    width = bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height()/2,
             f'{int(width)} km²', va='center', fontsize=10, fontweight='bold')

plt.title('Top 10 Thành Phố Lớn Nhất California Theo Diện Tích Đất (km²)',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Diện tích đất (km²)', fontsize=12)
plt.ylabel('Thành phố', fontsize=12)

plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()