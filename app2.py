# Plot Two Plots Inside a single Window Data Visualization
# with Python Matp

import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x1, y1, label='first plot',color='red')
plt.plot(x2, y2, label='second plot')

plt.xlabel('x ka label')
plt.ylabel('y ka label')
plt.title('ye mera graph hai')
plt.legend()

plt.show()