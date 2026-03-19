import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
phan_tram = [30, 25, 15, 20, 10]
colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']

plt.figure(figsize=(7, 7))
plt.pie(phan_tram, labels=labels, colors=colors, autopct='%1.0f%%',
        startangle=90, shadow=True, explode=[0.05]*5)

plt.title('Phân bố doanh số 5 sản phẩm (%)', fontsize=14, fontweight='bold')

plt.axis('equal')
plt.show()