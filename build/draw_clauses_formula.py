import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Define n(x)


def n(x):
    return 1000

# Define N(x)


def N(x):
    return n(x) - x + 1

# Define the reduced expression


def reduced(x):
    return (x - 1) * x / 2 + (N(x) - 1) * (x - 1)

# Define the seq expression


def seq(x):
    return N(x) * (3 * (x - 2) + 1)

# Define the naive expression


def naive(x):
    return (N(x) * (x - 1) * x) / 2

# Define the BDD expression


def bdd(x):
    return N(x) * (3 * (x - 2) + 2 * (x - 1) - 1)

# Define the product expression


def product(x):
    return N(x) * (2 * x + 4 * np.sqrt(x))

# Define the duplex expression


def duplex(x):
    return 13 * np.ceil(n(x) / x) * x - 14 * np.ceil(n(x) / x) - 3 * x + 2

# Define the SCL expression


def ladder(x):
    return 8 * np.ceil(n(x) / x) * x - 8 * np.ceil(n(x) / x) - 7 * x + 7


# Generate x values
x_values = np.linspace(2, 999, 998)

# Calculate y values using the expressions
reduced_values = reduced(x_values)
seq_values = seq(x_values)
naive_values = naive(x_values)
bdd_values = bdd(x_values)
product_values = product(x_values)
duplex_values = duplex(x_values)
ladder_values = ladder(x_values)

# Custom formatter for y-axis


def custom_formatter(y, pos):
    return f'{y * 1e-4:.0f}'  # Format the y value


# Create the plot
# plt.figure(figsize=(10, 10))
plt.plot(x_values, naive_values, linestyle='-',
         label="Naive", color='green', linewidth=2)
plt.plot(x_values, reduced_values, linestyle=':',
         label="Reduced", color='blue', linewidth=2)
plt.plot(x_values, seq_values, linestyle='--',
         label="Seq", color='orange', linewidth=2)
plt.plot(x_values, bdd_values, linestyle='-.',
         label="BDD", color='purple', linewidth=2)
plt.plot(x_values, product_values, linestyle=':',
         label="Product", color='red', linewidth=2)
plt.plot(x_values, duplex_values, linestyle='--',
         label="Duplex", color='magenta', linewidth=2)
plt.plot(x_values, ladder_values, linestyle='-',
         label="SCL", color='black', linewidth=2)

plt.xlabel('#Width')
plt.ylabel('#Clauses')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.ylim(0, 150000)
# Apply the custom formatter to the y-axis
plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formatter))
plt.text(y=1, x=0, s='e+04', va='bottom',
         ha='center', transform=plt.gca().transAxes)
plt.tight_layout()
plt.show()
