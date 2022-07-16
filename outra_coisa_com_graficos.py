from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns; sns.set()
import random

rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = 2 * x - 5 + rng.randn(50)
z = 2 * x + 0.67 + rng.randn(50)
plt.style.use('grayscale')
plt.scatter(x, y, color='blue', marker='o')
plt.title('Random Numbers versus others Random')
plt.xlabel('Ordinal numbers by x')
plt.ylabel('Ordinal numbers for y')
plt.grid(True, linestyle='--', linewidth=0.5, color='grey', )
plt.savefig('F:/dumps/cosa2.png', format='png')
plt.show()
model = LinearRegression(fit_intercept=True)

model.fit(x[:, np.newaxis], y)
xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])
plt.scatter(x, y, color='green', marker='.')
plt.plot(xfit, yfit, linewidth=0.6, linestyle='--', color='blue')
plt.grid(True, linestyle='--', linewidth=0.5, color='grey', )
plt.xlabel('Ordinal numbers by x')
plt.ylabel('Ordinal numbers for y')
plt.savefig('F:/dumps/cosa3.png', format='jpg')
plt.show()

