import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
N = 1001
t = np.linspace(0, N, N)
a = 0.02
b = 0.0005
c = 0.05
Z0 = 100
W0 = 30

Z = [Z0]
W = [W0]

for i in range(N-1):
    Z.append(Z[i]+a*Z[i]-b*Z[i]*W[i])
    W.append(W[i]+b*Z[i]*W[i]-c*W[i])

scat = ax.scatter(t[0], W[0], c="b", s=5, label='wilki')
line2 = ax.plot(t[0], Z[0], label='zające')[0]
ax.set(xlim=[0, N], ylim=[0, 140], xlabel='Time')
ax.legend()

def update(frame):
    x = t[:frame]
    y = W[:frame]
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    line2.set_xdata(t[:frame])
    line2.set_ydata(Z[:frame])
    return (scat, line2)


ani = FuncAnimation(fig=fig, func=update, frames=N, interval=30)
plt.show()