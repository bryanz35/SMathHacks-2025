import numpy as np

optimalOrbit = (0, 0, 0)
a_values = np.linspace(7000e3, 30000e3, 10)
e_values = np.linspace(0, 0.9, 10)   
i_values = np.linspace(0, 90, 10)  

radiation = 0
minradiation = float('inf')


def radiation(a, e, i):
    pos = np.linspace(0, 2*np.pi, 1000)
    r = a*(1-e**2)/(1 + e*np.cos(pos))
    x = r * np.cos(pos)
    y = r * np.sin(pos)
    z = r * np.sin(np.radians(i))

    radiation = 0
    for i in range(1000):
        radiation += B(x[i], y[i], z[i])
    
    return radiation

for a in a_values:
    for e in e_values:
        for i in i_values:
            if B(a, e, i) < minradiation:
                minradiation = radiation

            else:
                continue

