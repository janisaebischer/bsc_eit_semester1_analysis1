import matplotlib.pyplot as plt
import numpy as np

#Funktion f(x) = 3x^2
#Funktion wird einmal definiert damit es simplere Aufrufe gibt
def f(x):
    return 3*x**2
#Funktion g(x) = 3*10**2*log10(x**2)
minvalue = 1e-3

#Funktion lineare Skala mit f(x)
def Aufgabe2_linear_linear_1():
    # Definiert den Wertebereich der Funktion
    x = np.linspace(minvalue, 10, 30000)
    y = f(x)
    # Figure + Achse
    fig, ax = plt.subplots()
    # Graph zeichnen
    ax.plot(x, y, color="blue", label=r"$f(x) = 3x^2$")
    # 1. Zeile: Formel, größere Schrift
    ax.set_title(r"$f(x) = 3x^2$", fontsize=16, pad=20)
    # 2. Zeile: kleinere Schrift, direkt unter der ersten
    ax.text(
        0.5, 1.02,
        "X-Achse: linear, Y-Achse: linear",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=10,
        style="italic"
    )
    # Achsenbeschriftungen
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    # Gitterlinien für Plot
    ax.grid(True, which="major")
    ax.grid(True, which="minor",linewidth=0.5)
    #Legende aktivieren
    ax.legend()
    # Bereich einschränken
    ax.set_xlim(minvalue, 10)
    fig.savefig(r"Bilder\aufgabe2_linear_linear_1.png", dpi=600, bbox_inches="tight")

#Funktion lineare Skala mit f(x)
def Aufgabe2_linear_linear_2():
    # Definiert den Wertebereich der Funktion
    x = np.linspace(minvalue, 10, 30000)
    y = f(x)
    u = np.log10(x)
    # Figure + Achse
    fig, ax = plt.subplots()
    # Graph zeichnen
    ax.plot(u, y, color="blue", label=r"$f(x) = 3x^2$")
    # 1. Zeile: Formel, größere Schrift
    ax.set_title(r"$f(x) = 3x^2$", fontsize=16, pad=20)
    # 2. Zeile: kleinere Schrift, direkt unter der ersten
    ax.text(
        0.5, 1.02,
        "X-Achse: logarithmisch, Y-Achse: linear",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=10,
        style="italic"
    )
    # Achsenbeschriftungen
    ax.set_xlabel(r"$\log_{10}(x)$")
    ax.set_ylabel("f(x)")
    # Gitterlinien für Plot
    ax.grid(True, which="major")
    ax.grid(True, which="minor",linewidth=0.5)
    #Legende aktivieren
    ax.legend()
    # Bereich einschränken
    ax.set_xlim(-3, 1)
    fig.savefig(r"Bilder\aufgabe2_linear_linear_2.png", dpi=600, bbox_inches="tight")

    #Funktion lineare Skala mit f(x)
def Aufgabe2_linear_linear_3():
    # Definiert den Wertebereich der Funktion
    x = np.linspace(minvalue, 10, 30000)
    y = f(x)
    u = np.log10(x)
    v = np.log10(3)+2*u

    # Figure + Achse
    fig, ax = plt.subplots()
    # Graph zeichnen
    ax.plot(u, v, color="blue", label=r"$f(x) = 3x^2$")
    # 1. Zeile: Formel, größere Schrift
    ax.set_title(r"$f(x) = 3x^2$", fontsize=16, pad=20)
    # 2. Zeile: kleinere Schrift, direkt unter der ersten
    ax.text(
        0.5, 1.02,
        "X-Achse: logarithmisch, Y-Achse: logarithmisch",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=10,
        style="italic"
    )
    # Achsenbeschriftungen
    ax.set_xlabel(r"$\log_{10}(x)$")
    ax.set_ylabel(r"$\log_{10}(3)+2*log_{10}(x)$")
    # Gitterlinien für Plot
    ax.grid(True, which="major")
    ax.grid(True, which="minor",linewidth=0.5)
    #Legende aktivieren
    ax.legend()
    # Bereich einschränken
    ax.set_xlim(-3, 1)
    fig.savefig(r"Bilder\aufgabe2_linear_linear_3.png", dpi=600, bbox_inches="tight")

#Funktion semilog Skala mit f(x)
def Aufgabe2_log_linear():
    # Definiert den Wertebereich der Funktion
    x = np.linspace(minvalue, 10, 30000)
    y = f(x)
    # Figure + Achse
    fig, ax = plt.subplots()
    # Graph zeichnen
    ax.plot(x, y, color="blue", label=r"$f(x) = 3x^2$")
    # Logarithmische Skala
    ax.set_xscale("log")
    ax.set_yscale("linear")
    # 1. Zeile: Formel, größere Schrift
    ax.set_title(r"$f(x) = 3x^2$", fontsize=16, pad=20)
    # 2. Zeile: kleinere Schrift, direkt unter der ersten
    ax.text(
        0.5, 1.02,
        "X-Achse: logarithmisch, Y-Achse: linear",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=10,
        style="italic"
    )
    # Achsenbeschriftungen
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    # Gitterlinien für Plot
    ax.grid(True, which="major")
    ax.grid(True, which="minor",linewidth=0.5)
    #Legende aktivieren
    ax.legend()
    # Bereich einschränken (untere Grenze > 0 wegen log-Skala!)
    ax.set_xlim(minvalue, 10)
    fig.savefig(r"Bilder\aufgabe2_logarithmisch_linear.png", dpi=600, bbox_inches="tight")

#Funktion logarithmische Skala mit f(x)
def Aufgabe2_log_log():
    # Definiert den Wertebereich der Funktion
    x = np.linspace(minvalue, 10, 30000)
    y = f(x)
    # Figure + Achse
    fig, ax = plt.subplots()
    # Graph zeichnen
    ax.plot(x, y, color="blue", label=r"$f(x) = 3x^2$")
    # Logarithmische Skalen
    ax.set_xscale("log")
    ax.set_yscale("log")
    # 1. Zeile: Formel, größere Schrift
    ax.set_title(r"$f(x) = 3x^2$", fontsize=16, pad=20)
    # 2. Zeile: kleinere Schrift, direkt unter der ersten
    ax.text(
        0.5, 1.02,
        "X-Achse: logarithmisch, Y-Achse: logarithmisch",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=10,
        style="italic"
    )
    # Achsenbeschriftungen
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    # Gitterlinien für Plot
    ax.grid(True, which="major")
    ax.grid(True, which="minor",linewidth=0.5)
    #Legende aktivieren
    ax.legend()
    # Bereich einschränken (untere Grenze > 0 wegen log-Skala!)
    ax.set_xlim(minvalue, 10)
    fig.savefig(r"Bilder\aufgabe2_logarithmisch_logarithmisch.png", dpi=600, bbox_inches="tight")
    
#Aufruf der Funktion
if __name__ == "__main__":
    Aufgabe2_linear_linear_1()
    Aufgabe2_linear_linear_2()
    Aufgabe2_log_linear()
    Aufgabe2_linear_linear_3()
    Aufgabe2_log_log()
    plt.show()