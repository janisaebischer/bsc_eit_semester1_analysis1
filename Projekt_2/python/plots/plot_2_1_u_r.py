import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT = Path(__file__).parent / "output"
OUTPUT.mkdir(exist_ok=True)

r = np.logspace(-3, 3, 2000)
u = r / (1 + r)

plt.figure()
plt.semilogx(r, u, label = r"$u(r)=\frac{r}{1+r}$")
plt.xlim(r[0], r[-1])
plt.margins(x=0)
plt.minorticks_on()
plt.grid(True, which="both")
plt.xlabel(r"$r=\frac{R_L}{R_I}$")
plt.ylabel(r"$u(r)=\frac{U}{U_0}$")
plt.legend()
plt.grid(True)

plt.savefig(OUTPUT / "2_1_4_u_r_spannungsquelle.png", dpi=200, bbox_inches="tight")
plt.savefig(OUTPUT / "2_1_4_u_r_spannungsquelle.pdf", bbox_inches="tight")
plt.close()
