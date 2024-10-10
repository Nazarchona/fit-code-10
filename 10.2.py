from scipy.interpolate import approximate_taylor_polynomial

# Побудова полінома Тейлора за допомогою scipy
taylor_poly = approximate_taylor_polynomial(f, 0, degree=3, scale=1)

# Графік функції та полінома Тейлора з scipy
y_taylor_scipy = taylor_poly(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_original, label='Original function f(x) = sin(4x)')
plt.plot(x, y_taylor_scipy, label='Taylor polynomial (3rd degree) - scipy')
plt.title('Taylor Polynomial with scipy')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
