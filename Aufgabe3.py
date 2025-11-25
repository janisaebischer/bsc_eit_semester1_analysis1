import numpy as np
import matplotlib.pyplot as plt
import os

# Funktion
def f(x):
    return 3 * x**2

# Ordner für Bilder
out_dir = "Bilder"
os.makedirs(out_dir, exist_ok=True)

def aufgabe2_alle():
    # x-Bereiche
    x_lin = np.linspace(0, 10, 1000)    # für lineare Skalen
    x_pos = np.linspace(0.1, 10, 1000)  # für log-Skalen (x > 0!)
    y_lin = f(x_lin)
    y_pos = f(x_pos)

    # 1) linear-linear
    fig, ax = plt.subplots(figsize=(5.8, 4))   # gut druckbar (A5 quer)
    ax.plot(x_lin, y_lin, color="blue", label=r"$f(x) = 3x^2$")
    ax.set_title(r"$f(x) = 3x^2$" "\nX: linear, Y: linear")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()
    fig.savefig(os.path.join(out_dir, "aufgabe2_1_linear_linear.png"),
                dpi=600, bbox_inches="tight")

    # 2) log x, linear y
    fig, ax = plt.subplots(figsize=(5.8, 4))
    ax.plot(x_pos, y_pos, color="blue", label=r"$f(x) = 3x^2$")
    ax.set_xscale("log")
    ax.set_title(r"$f(x) = 3x^2$" "\nX: logarithmisch, Y: linear")
    ax.set_xlabel("x (log)")
    ax.set_ylabel("f(x)")
    ax.grid(True, which="both")
    ax.legend()
    fig.savefig(os.path.join(out_dir, "aufgabe2_2_logx_linear.png"),
                dpi=600, bbox_inches="tight")

    # 3) linear x, log y
    fig, ax = plt.subplots(figsize=(5.8, 4))
    ax.plot(x_pos, y_pos, color="blue", label=r"$f(x) = 3x^2$")
    ax.set_yscale("log")
    ax.set_title(r"$f(x) = 3x^2$" "\nX: linear, Y: logarithmisch")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x) (log)")
    ax.grid(True, which="both")
    ax.legend()
    fig.savefig(os.path.join(out_dir, "aufgabe2_3_linear_logy.png"),
                dpi=600, bbox_inches="tight")

    # 4) log x, log y
    fig, ax = plt.subplots(figsize=(5.8, 4))
    ax.plot(x_pos, y_pos, color="blue", label=r"$f(x) = 3x^2$")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(r"$f(x) = 3x^2$" "\nX: logarithmisch, Y: logarithmisch")
    ax.set_xlabel("x (log)")
    ax.set_ylabel("f(x) (log)")
    ax.grid(True, which="both")
    ax.legend()
    fig.savefig(os.path.join(out_dir, "aufgabe2_4_logx_logy.png"),
                dpi=600, bbox_inches="tight")

    # 5) u-v-Plot mit log10
    # u = log10(x), v = log10(y) = log10(3) + 2*log10(x)
    u = np.log10(x_pos)
    v = np.log10(y_pos)

    fig, ax = plt.subplots(figsize=(5.8, 4))
    ax.plot(u, v, color="blue", label=r"$v = 2u + \log_{10}(3)$")
    ax.set_title("u-v-Darstellung\n"
                 r"$u = \log_{10}(x),\ v = \log_{10}(y)$")
    ax.set_xlabel(r"$u = \log_{10}(x)$")
    ax.set_ylabel(r"$v = \log_{10}(y)$")
    ax.grid(True)
    ax.legend()
    fig.savefig(os.path.join(out_dir, "aufgabe2_5_uv_plot.png"),
                dpi=600, bbox_inches="tight")

    # Wenn du alle nacheinander sehen willst:
    plt.show()

if __name__ == "__main__":
    aufgabe2_alle()
