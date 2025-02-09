import numpy as np

I0 = 1361
AU = 1.496e11
MU = 3.986e14

def solar_radiation(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    return I0 * (AU / r)**2

def total_radiation(a, e, i, num_points=1000):
    t = np.linspace(0, 2 * np.pi, num_points)
    r = a * (1 - e**2) / (1 + e * np.cos(t))
    
    x = r * np.cos(t)
    y = r * np.sin(t)
    z = r * np.sin(np.radians(i))

    radexposure = 0
    for j in range(num_points):
        radiation = solar_radiation(x[j], y[j], z[j])
        radexposure += radiation

    return radexposure

def compute_perigee_apogee_velocity(a, e):
    r_p = a * (1 - e)
    r_a = a * (1 + e)
    v_p = np.sqrt(MU * (2/r_p - 1/a))
    v_a = np.sqrt(MU * (2/r_a - 1/a))
    return (v_p, v_a)

a_min = float(input("Enter minimum value for semi-major axis (a) in meters: "))
a_max = float(input("Enter maximum value for semi-major axis (a) in meters: "))
e_min = float(input("Enter minimum value for eccentricity (e): "))
e_max = float(input("Enter maximum value for eccentricity (e): "))
i_min = float(input("Enter minimum value for inclination (i) in degrees: "))
i_max = float(input("Enter maximum value for inclination (i) in degrees: "))

a_values = np.linspace(a_min, a_max, 10)
e_values = np.linspace(e_min, e_max, 10)
i_values = np.linspace(i_min, i_max, 5)

min_radiation = float('inf')
optimalOrbit = None

for a in a_values:
    for e in e_values:
        for i in i_values:
            rad = total_radiation(a, e, i)
            if rad < min_radiation:
                min_radiation = rad
                optimalOrbit = (a, e, i)


print(f"Optimal Orbit: a={optimalOrbit[0]/1e3} km, e={optimalOrbit[1]}, i={optimalOrbit[2]} deg with min radiation {min_radiation:.2e} W/m^2")
