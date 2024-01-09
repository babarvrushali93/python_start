# Drawing Pie Charts Data Visualization
# with Python Matplotlib

import matplotlib.pyplot as plt

slices = [45, 34, 32, 35, 12]
channels = ['FTV', '9XM', 'Ten Sports', 'sony', 'HCZ']
cols = ['red', 'green', 'b', 'cyan', 'y']

plt.pie(slices,
        labels=channels,
        colors=cols,
        explode=(0.05, 0, 0, 0, 0),
        startangle=90,
        shadow=True,
        autopct='%1.1f%%')
plt.title('yaha koi bhi title de do yarr')
plt.show()
