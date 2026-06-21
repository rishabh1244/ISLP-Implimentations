import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# generating random data
np.random.seed(42)

n = 10000

size_sqft = np.random.normal(1510, 300, n)
bedrooms = np.random.randint(1, 6, n)

noise = np.random.normal(0, 40000, n)

price = 500000 + 180 * size_sqft + 15000 * bedrooms + noise

df = pd.DataFrame({"size_sqft": size_sqft, "bedrooms": bedrooms, "price": price})

df.to_csv("data/housing_demo.csv", index=False)

# testing for central limit theorem
data = pd.read_csv("data/housing_demo.csv")
x = data["size_sqft"]

print("actual mean : ", x.mean())

sample_size = 100
num_samples = 10000

sample_means = []

for _ in range(num_samples):

    sample = x.sample(n=sample_size, replace=True)

    sample_means.append(sample.mean())


true_SE = x.mean() / np.sqrt(num_samples)
print("TRUE SAMPLE ERROR ", true_SE)

plt.style.use("dark_background")

plt.figure(figsize=(8, 5))
plt.hist(sample_means, bins=31, edgecolor="black", color="steelblue")
plt.grid(axis="y", alpha=0.3)
plt.xlabel("mean")
plt.ylabel("freq")
plt.show()


# hypothesis testing

a = 2
b = 244

sample_mean = x[a:b].mean()
std_dev = x[a:b].std()
print(sample_mean)


se = std_dev / np.sqrt(b - a)
print("SE ", se)

print("Z ", (sample_mean - x.mean()) / se)
