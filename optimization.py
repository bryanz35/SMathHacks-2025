import numpy as np
import matplotlib.pyplot as plt 

optimalOrbit = (0, 0, 0)
a_values = np.linspace(7000e3, 30000e3, 10)
e_values = np.linspace(0, 0.9, 10)   
i_values = np.linspace(0, 90, 10)  

radiation = 0
minradiation = float('inf')
min_a = 0
min_e = 0
min_i = 0

RT = 6371000.0  # Earth radius [m]
m_p = 1.67E-27  # mass of proton [kg]
m_e = 9.109E-31  # mass of electron [kg]
qe = 1.602E-19  # charge of proton [C]
phi = 11.70 * np.pi / 180.0  # Magnetic dipole tilt [rad]
th = 23.67 * np.pi / 180.0  # Earth’s obliquity [rad]
mu = -7.94e22 * np.array([0.0, np.sin(phi), np.cos(phi)])  # Earth’s magnetic moment [A m²]
R0dip = np.array([0.0, 0.0, 0.0])  # Dipole moment location
M0 = 1.0E-7  # mu0 / 4 pi

# TODO: Update B to use IGRF model
def B(R, R0, mu):
    r = np.array([R[0] - R0[0], R[1] - R0[1], R[2] - R0[2]]) * RT
    rmag = np.sqrt(r[0]**2 + r[1]**2 + r[2]**2)
    Bfield = M0 * (3.0 * r * np.dot(mu, r) / (rmag**5) - mu / (rmag**3))
    return Bfield

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
            if radiation(a, e, i) < minradiation:
                minradiation = radiation
                min_a = a
                min_e = e
                min_i = i

            else:
                continue


print(min_a + " " + min_e + " " + min_i) 
