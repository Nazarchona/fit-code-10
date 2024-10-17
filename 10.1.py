import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

# Визначення функції f(x) = sin(4x)
def f(x):
    return np.sin(4 * x)

# Пошук перших трьох похідних вручну
def first_derivative(x):
    return 4 * np.cos(4 * x)

def second_derivative(x):
    return -16 * np.sin(4 * x)

def third_derivative(x):
    return -64 * np.cos(4 * x)

def fourth_derivative(x):
    return 256 * np.sin(4 * x)

# Поліном Тейлора третього степеня побудований вручну
def taylor_polynomial_third(x):
    return 4 * x - (64 / 6) * x**3  # P3(x)

# Оцінка похибки для полінома третього степеня
def taylor_error_third(x):
    return np.abs(fourth_derivative(x) / 24 * x**4)

# Межі для графіку
x_vals = np.linspace(-1, 1, 400)

# Обчислення значень функції та полінома
f_vals = f(x_vals)
taylor_vals_third = taylor_polynomial_third(x_vals)
error_third = taylor_error_third(x_vals)

# Побудова полінома Тейлора четвертого степеня за допомогою scipy
taylor_polynomial_scipy = approximate_taylor_polynomial(f, 0, degree=4, scale=1)

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label="f(x) = sin(4x)", color="blue")
plt.plot(x_vals, taylor_vals_third, label="Taylor P3(x)", linestyle="--", color="green")
plt.plot(x_vals, taylor_polynomial_scipy(x_vals), label="Taylor P4(x) (scipy)", linestyle="--", color="red")
plt.fill_between(x_vals, taylor_vals_third - error_third, taylor_vals_third + error_third, color='lightgreen', alpha=0.3, label="Error P3(x)")
plt.title("Поліном Тейлора та наближення для f(x) = sin(4x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

