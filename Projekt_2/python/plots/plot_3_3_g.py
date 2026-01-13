import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Output-Ordner
OUTPUT = Path(__file__).parent / "output"
OUTPUT.mkdir(exist_ok=True)

# x-Bereich (bei Bedarf anpassen)
x = np.linspace(-2, 2, 4000)

def f(x):
    return np.cos(2 * x**3 + 1) * np.exp(x - 1)

# Gerade Komponente
g = (f(x) + f(-x)) / 2

# Plot
plt.figure()
plt.plot(x, g, label=r"$g(x)=\frac{f(x)+f(-x)}{2}$")

# Achsen "von links bis rechts"
plt.xlim(x[0], x[-1])
plt.margins(x=0)

plt.xlabel(r"$x$")
plt.ylabel("g(x)")


# Optik wie gewünscht
plt.minorticks_on()
plt.grid(True, which="both")
plt.legend(loc="best")

# Speichern
plt.savefig(OUTPUT / "3_3_g_only.png", dpi=200, bbox_inches="tight")
plt.savefig(OUTPUT / "3_3_g_only.pdf", bbox_inches="tight")
plt.close()
