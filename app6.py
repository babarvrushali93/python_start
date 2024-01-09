import requests
import json
import matplotlib.pyplot as plt

a = requests.get('https://www.google.com/finance/quote/SBIN:NSE.json?')
b = json.loads(a.text)
my_data = b['dataset']['data']
useful_data = [i[1] for i in reversed(my_data)]
x_data = [i for i in range(len(useful_data))]
plt.plot(x_data, useful_data)
plt.title('SBI stock pricess')
plt.xlabel('Time')
plt.ylabel('stock price')

plt.savefig('figure.png')
plt.show()