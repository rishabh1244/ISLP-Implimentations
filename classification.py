# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# %%
data = pd.read_csv("./data/heart.csv").to_numpy()

# need 1 more col containing 1s so we can have a scaling factor beta_n
expected_output = data[:, -1]
scaling_col = np.ones((data.shape[0], 1))
data = data[:, :-1]
data = np.column_stack((data, scaling_col))

# %%

# geneate a parameter matrix
# size = len(data[0])

rng = np.random.default_rng()
beta_param = rng.normal(0, 0.01, data.shape[1])

print(data)
print(data.shape)
print(beta_param)
print(beta_param.shape)

# predicted value

val = sigmoid(data @ beta_param)
eps = 1e-15
p = np.clip(val, eps, 1 - eps)

# cross-entropy loss

# %%
log_likelihood = np.sum(
    expected_output * np.log(p) + (1 - expected_output) * np.log(1 - p)
) / len(data)

print(log_likelihood)

gradient = 1 / len(data) * (data.T @ (p - expected_output))
learning_rate = 0.01
beta_param -= learning_rate * gradient
epochs = 1025

for i in range(0, epochs):

    z = data @ beta_param

    val = sigmoid(z)

    gradient = data.T @ (val - expected_output) / len(expected_output)

    beta_param -= learning_rate * gradient

z = data @ beta_param

p = sigmoid(z)


p = np.clip(p, eps, 1 - eps)

new_log_likelihood = np.mean(
    expected_output * np.log(p) + (1 - expected_output) * np.log(1 - p)
)
print(new_log_likelihood)


# %%
