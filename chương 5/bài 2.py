import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 400)
y2 = x ** 2
y3 = x ** 3

plt.figure(figsize=(9, 6))
plt.plot(x, y2, color='green', linewidth=2, label='y = x²')
plt.plot(x, y3, color='red', linewidth=2, label='y = x³')

plt.title('So sánh hai hàm số y = x² và y = x³', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.show()