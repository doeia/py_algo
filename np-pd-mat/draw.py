import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 256)
y = np.sin(x)

plt.plot(x, y)

plt.savefig("./output/o.png")
