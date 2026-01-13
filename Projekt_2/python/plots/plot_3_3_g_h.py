import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT = Path(__file__).parent / "output"
OUTPUT.mkdir(exist_ok=True)

x = np.linspace(-2, 2, 4000)

def f(x):
    return np.cos(2*x**3 + 1) * np.exp(x - 1)

fx = f(x)
gx = (f(x) + f(-x)) / 2
hx = (f(x) - f(-x)) / 2

plt.figure()
plt.xlim(x[0], x[-1])
plt.margins(x=0)
plt.plot(x, fx, label=r"$f(x)$")
plt.plot(x, gx+hx, label=r"$g(x)+h(x)$")
plt.xlabel(r"$x$")
plt.ylabel("Wert")
plt.legend()
plt.grid(True)

plt.savefig(OUTPUT / "3_3_f_vs_g_plus_h.png", dpi=200, bbox_inches="tight")
plt.savefig(OUTPUT / "3_3_f_vs_g_plus_h.pdf", bbox_inches="tight")
plt.close()
