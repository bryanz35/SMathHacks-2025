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
tf = 1000.0
Nsteps = int(tf / dt)

t = np.zeros(Nsteps)
rp = np.zeros((len(t), 3))
vp = np.zeros((len(t), 3))

m = 4.0 * m_p
q = 2.0 * qe

# ====== Define initial conditions ======
init_pos = [5, 4, 3.0]
init_vel = [1, 2, 3]
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
x = rp[:, 0]
y = rp[:, 1]
z = rp[:, 2]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sx = np.split(x, 5)
sy = np.split(y, 5)
sz = np.split(z, 5)
ax.plot(sx[0], sy[0], sz[0], color='blue')
ax.plot(sx[1], sy[1], sz[1], color='slateblue')
ax.plot(sx[2], sy[2], sz[2], color='mediumslateblue')
ax.plot(sx[3], sy[3], sz[3], color='darkslateblue')
ax.plot(sx[4], sy[4], sz[4], color='indigo')

ax.scatter([0],[0], [0], color='red')
plt.show()