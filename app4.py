# How To Draw Scatter Charts Data Visualization
# with Python Matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [4, 3, 5, 3, 3, 3]

plt.scatter(x, y, label='scatter', color='red', marker=".", s=62 )
plt.legend()


plt.show()
