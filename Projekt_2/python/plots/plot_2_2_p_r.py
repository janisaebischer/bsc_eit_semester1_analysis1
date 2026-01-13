import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT = Path(__file__).parent / "output"
OUTPUT.mkdir(exist_ok=True)

r = np.logspace(-3, 3, 2000)  # r = G_L / G_I
p = 4 * r / (1 + r)**2

plt.figure()
plt.semilogx(r, p, label=r"$p(r)=\frac{4r}{(1+r)^2}$")
plt.xlim(r[0], r[-1])
plt.margins(x=0)
plt.minorticks_on()
plt.grid(True, which="both")
plt.xlabel(r"$r=\frac{G_L}{G_I}$")
plt.ylabel(r"$p(r)=\frac{P}{P_0}$")
plt.legend()
plt.grid(True)

plt.savefig(OUTPUT / "2_2_3_p_r_stromquelle.png", dpi=200, bbox_inches="tight")
plt.savefig(OUTPUT / "2_2_3_p_r_stromquelle.pdf", bbox_inches="tight")
plt.close()
