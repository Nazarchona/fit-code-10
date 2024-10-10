import numpy as np
import matplotlib.pyplot as plt

# Функція
def f(x):
    return np.sin(4 * x)

# Поліном Тейлора 3-го степеня (аналітичний розрахунок)
def taylor_approximation(x):
    return 4 * x - (64 / 6) * (x ** 3)

# Створення точок для графіків
x = np.linspace(-1, 1, 400)
y_original = f(x)
y_taylor = taylor_approximation(x)

# Побудова графіків функції та полінома Тейлора
plt.figure(figsize=(10, 6))
plt.plot(x, y_original, label='Original function f(x) = sin(4x)')
plt.plot(x, y_taylor, label='Taylor polynomial (3rd degree)')
plt.title('Taylor Approximation for f(x) = sin(4x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
