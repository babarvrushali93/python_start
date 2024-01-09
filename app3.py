# How To Plot Bar Charts Data Visualization with Python Matplotlib

import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [5, 2, 6, 3, 6]

x1 = [2, 4, 6,  8]
y1 = [4, 5, 6, 7]
plt.bar(x, y, label='first plot', color='red')
plt.bar(x1, y1, label='second plot', color='blue')
plt.legend()
plt.title('kuch bhi title de do')
plt.xlabel('kuch bhi xlabel de do')
plt.ylabel('kuch bhi ylabel de do')


plt.show()

