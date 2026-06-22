import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data/house.csv")
x = data["size_sqft"]
y = data["price_usd"]

# applying linear regression onto this
# Y = B1 * X  + B0
# where B1 is the correlation coefficent working as the slope of the line (kinda obvious)
# b1 = summation( ( xi - mean(x) ) * (yi - mean(y)) ) /  summation ( ( xi - mean(x))^2 )
# b2 = mean(y) - b1 * mean(x)

mean_x = np.mean(x)
mean_y = np.mean(y)
b1 = 0
b1_denom = 0

for i in x:
    b1_denom += np.square(i - mean_x)

for i in range(0, x.size):
    b1 += (x[i] - mean_x) * (y[i] - mean_y)

b1 = b1 / b1_denom
b2 = mean_y - b1 * mean_x

y_pred = b2 + b1 * x

plt.style.use("dark_background")
plt.scatter(x, y, label="Actual data")
plt.plot(x, y_pred, color="red", label="Regression line")


# %%

plt.xlabel("size_sqft")
plt.ylabel("price_usd")
plt.legend()
print(b1)
print(b2)
plt.show()
