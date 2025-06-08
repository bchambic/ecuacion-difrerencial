import numpy as np
import matplotlib.pyplot as plt

def heun(f, tspan, y0, h):
    t = np.arange(tspan[0], tspan[1] + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(len(t)-1):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h, y[i] + h*k1)
        y[i+1] = y[i] + h/2 * (k1 + k2)
    return t, y

def rk4(f, tspan, y0, h):
    t = np.arange(tspan[0], tspan[1] + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(len(t)-1):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h/2, y[i] + h/2*k1)
        k3 = f(t[i] + h/2, y[i] + h/2*k2)
        k4 = f(t[i] + h, y[i] + h*k3)
        y[i+1] = y[i] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    return t, y

# Problema 37
def dNdt(t, N):
    return 0.000095 * N * (5000 - N)

t_heun, N_heun = heun(dNdt, [0, 20], 100, 0.1)
t_rk4, N_rk4 = rk4(dNdt, [0, 20], 100, 0.1)

plt.figure(figsize=(10,6))
plt.plot(t_heun, N_heun, label='Heun')
plt.plot(t_rk4, N_rk4, label='RK4', linestyle='--')
plt.title('Crecimiento Poblacional')
plt.xlabel('Tiempo (años)')
plt.ylabel('Población')
plt.legend()
plt.grid()
plt.show()