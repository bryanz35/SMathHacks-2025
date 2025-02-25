"""
TODO: Plot solutions (position, time, velocity...)
"""

import numpy as np
import matplotlib.pyplot as plt 

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


'''def B(R, R0, mu):
    V = 0
    sum1 = 0
    for n in range(1, N):
        sum2 = 0
        for m in range(0, n):
            ans = (a/r) ** (n+1)
            sum2 += ans
        sum1 += sum2
    return sum1'''

dt = 0.1
tf = 5000.0
Nsteps = int(tf / dt)

t = np.zeros(Nsteps)
rp = np.zeros((len(t), 3))
vp = np.zeros((len(t), 3))

m = m_e
q = -qe

# ====== Define initial conditions ======
init_pos = [5.0, 4.0, 3.0]
init_vel = [1.0, 2.0, 3.0]
t[0] = 0.0
rp[0, :] = np.array(init_pos)
vp[0, :] = np.array(init_vel)

# ====== RK4 implementation ======
for i in range(1, Nsteps):
    rp1 = rp[i - 1, :]
    vp1 = vp[i - 1, :]
    ap1 = q / m * np.cross(vp1, B(rp1, R0dip, mu))

    rp2 = rp[i - 1, :] + 0.5 * vp1 * dt
    vp2 = vp[i - 1, :] + 0.5 * ap1 * dt
    ap2 = q / m * np.cross(vp2, B(rp2, R0dip, mu))

    rp3 = rp[i - 1, :] + 0.5 * vp2 * dt
    vp3 = vp[i - 1, :] + 0.5 * ap2 * dt
    ap3 = q / m * np.cross(vp3, B(rp3, R0dip, mu))

    rp4 = rp[i - 1, :] + vp3 * dt
    vp4 = vp[i - 1, :] + ap3 * dt
    ap4 = q / m * np.cross(vp4, B(rp4, R0dip, mu))

    rp[i] = rp[i - 1, :] + (dt / 6.0) * (vp1 + 2 * vp2 + 2 * vp3 + vp4)
    vp[i] = vp[i - 1, :] + (dt / 6.0) * (ap1 + 2 * ap2 + 2 * ap3 + ap4)
    t[i] = dt * i
print(rp)
def x(initial_pos, vel_arr, time_arr):
    dists = [initial_pos]
    for i in range(len(time_arr.tolist())):
        spec_vel = vel_arr[i]
        dists.append(np.array(spec_vel + dists[-1]))
    return dists

pos = x([init_pos], vp, t)
px = [r[0] for r in rp]
py = [r[0] for r in rp]
pz = [r[0] for r in rp]
pos = np.array([pos])
x_vals = [p[0][0] for p in pos[0]][:1000]
y_vals = [p[0][1] for p in pos[0]][:1000]
z_vals = [p[0][2] for p in pos[0]][:1000]
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot(px, py, pz, label='Orbit')
plt.show()
