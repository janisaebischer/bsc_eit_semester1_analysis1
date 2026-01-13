import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Output
OUTPUT = Path(__file__).parent / "output"
OUTPUT.mkdir(exist_ok=True)

# Daten
r = np.logspace(-3, 3, 2000)
p = 4 * r / (1 + r)**2

# Plot
plt.figure()
plt.semilogx(r, p, label=r"$p(r)=\frac{4r}{(1+r)^2}$")
plt.xlim(r[0], r[-1])
plt.margins(x=0)
plt.minorticks_on()
plt.grid(True, which="both")
plt.xlabel(r"$r=\frac{R_L}{R_I}$")
plt.ylabel(r"$p(r)=\frac{P_L}{P_0}$")
plt.legend()
plt.grid(True)

# Speichern
plt.savefig(OUTPUT / "2_1_3_p_r_spannungsquelle.png", dpi=200, bbox_inches="tight")
plt.savefig(OUTPUT / "2_1_3_p_r_spannungsquelle.pdf", bbox_inches="tight")
plt.close()
