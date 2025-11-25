import matplotlib.pyplot as plt
import numpy as np
#Definiere h
hvalue = 0.5
minvalue = 0
maxvalue = np.pi

#Funktion f(x) = cos(x)
#Funktion wird einmal definiert damit es simplere Aufrufe gibt
def f(x):
    return np.cos(x)

def f_prime(x):
    return -np.sin(x)

def g(x,h=hvalue):
    return (f(x+h)-f(x))/h

def h(x,h=hvalue):
    return (f(x+h/2)-f(x-h/2))/h

def Aufgabe3():
    # Definiert den Wertebereich der Funktion
    x = np.linspace(minvalue, maxvalue, 30000)
    y_f = f(x)
    y_fprime = f_prime(x)
    y_g = g(x)
    y_h = h(x)
    # Figure + Achse
    fig, ax = plt.subplots()
    # Graph zeichnen
    ax.plot(x, y_f, color="blue", label=r"f(x) = cos(x)")
    ax.plot(x, y_fprime, color="red", label=r"f'(x) = -sin(x)")
    ax.plot(x, y_g, color="green", label=r"$g(x) = \frac{(x + h) - x}{h}$")
    ax.plot(x, y_h, color="orange", label=r"$h(x) = \frac{\left(x + \frac{h}{2}\right) - \left(x - \frac{h}{2}\right)}{h}$")
    # 1. Zeile: Formel, größere Schrift
    ax.set_title(r"Ableitung der Funktion $f(x) = cos (x)$", fontsize=16, pad=20)
    # 2. Zeile: kleinere Schrift, direkt unter der ersten
    ax.text(
        0.5, 1.02,
        f"Annäherung der Funktion mit h={hvalue}",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=10,
        style="italic"
    )
    # Achsenbeschriftungen
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    # Gitterlinien für Plot
    ax.grid(True, which="major")
    ax.grid(True, which="minor",linewidth=0.5)
    #Legende aktivieren
    ax.legend()
    # Bereich einschränken
    ax.set_xlim(minvalue, maxvalue)
    fig.savefig(r"Bilder\aufgabe3.png", dpi=600, bbox_inches="tight")

#Aufruf der Funktion
if __name__ == "__main__":
    Aufgabe3()
    plt.show()