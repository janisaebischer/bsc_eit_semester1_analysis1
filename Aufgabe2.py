import matplotlib.pyplot as plt
import numpy as np

#Funktion f(x) = 3x^2
#Funktion wird einmal definiert damit es simplere Aufrufe gibt
def f(x):
    return 3*x**2

#Funktion für linear linear
def Aufgabe2_linear_linear():
    #Definiert den Wertebereich der Funktion
    x = np.linspace(0, 10, 30000) 
    #Aufruf der zuvor definierten Funktion, also unsere Funktion aus der Aufgabenstellung. Abbildung mit der entsprechenden Funktion auf y
    y = f(x)
    #Öffnet einen neuen Graphen
    plt.figure()
    #Zeichnet den Graphen in Abhängikeit mit den zuvor definierten x und y. Das Label wir anschliessend unten in der Legende angezeigt. Das r ist da, um die Formel in LaTeX-Syntax einzugeben
    plt.plot(x, y, color="blue",label=r"$f(x) = 3x^2$")
    #Eingabe des Titels, erneut in LaTex-Syntax
    plt.title(r"$f(x) = 3x^2$" "\nX-Achse: linear, Y-Achse: linear")
    #X-Achsenbeschriftung
    plt.xlabel("x")
    #Y-Achsenbeschriftung
    plt.ylabel("f(x)")
    #Anzeige des XY-Gitters
    plt.grid(True)
    #Zeigt die in den "label" definierten Texte in der Legende an
    plt.legend()
    #Zeigt nur den ausgewählten Bereich an
    plt.xlim(0, 10)
    #Bild für den Bericht speichern
    plt.savefig(r"Bilder\aufgabe2_linear_linear.png", dpi=600, bbox_inches="tight")

#Funktion für logarithmisch linear
def Aufgabe2_log_linear():
    #Definiert den Wertebereich der Funktion
    x = np.linspace(0.000001, 10, 30000) 
    #Aufruf der zuvor definierten Funktion, also unsere Funktion aus der Aufgabenstellung. Abbildung mit der entsprechenden Funktion auf y
    y = f(x)
    #Öffnet einen neuen Graphen
    plt.figure()
    #Zeichnet den Graphen in Abhängikeit mit den zuvor definierten x und y. Das Label wir anschliessend unten in der Legende angezeigt. Das r ist da, um die Formel in LaTeX-Syntax einzugeben
    plt.plot(x, y, color="blue",label=r"$f(x) = 3x^2$")
    #Einstellen der logarithmischen Skala
    plt.xscale("log")
    #Eingabe des Titels, erneut in LaTex-Syntax
    plt.title(r"$f(x) = 3x^2$" "\nX-Achse: logarithmisch, Y-Achse: linear")
    #X-Achsenbeschriftung
    plt.xlabel("x")
    #Y-Achsenbeschriftung
    plt.ylabel("f(x)")
    #Anzeige des XY-Gitters
    plt.grid(True)
    #Zeigt die in den "label" definierten Texte in der Legende an
    plt.legend()
    #Zeigt nur den ausgewählten Bereich an
    plt.xlim(0, 10)
    #Bild für den Bericht speichern
    plt.savefig(r"Bilder\aufgabe2_log_linear.png", dpi=600, bbox_inches="tight")

#Funktion für logarithmisch logarithmisch
def Aufgabe2_log_log():
    #Definiert den Wertebereich der Funktion
    x = np.linspace(0.000001, 10, 30000) 
    #Aufruf der zuvor definierten Funktion, also unsere Funktion aus der Aufgabenstellung. Abbildung mit der entsprechenden Funktion auf y
    y = f(x)
    #Öffnet einen neuen Graphen
    plt.figure()
    #Zeichnet den Graphen in Abhängikeit mit den zuvor definierten x und y. Das Label wir anschliessend unten in der Legende angezeigt. Das r ist da, um die Formel in LaTeX-Syntax einzugeben
    plt.plot(x, y, color="blue",label=r"$f(x) = 3x^2$")
    #Einstellen der logarithmischen Skala
    plt.xscale("log")
    plt.yscale("log")
    #Eingabe des Titels, erneut in LaTex-Syntax
    plt.title(r"$f(x) = 3x^2$" "\nX-Achse: logarithmisch, Y-Achse: logarithmisch")
    #X-Achsenbeschriftung
    plt.xlabel("x")
    #Y-Achsenbeschriftung
    plt.ylabel("f(x)")
    #Anzeige des XY-Gitters
    plt.grid(True)
    #Zeigt die in den "label" definierten Texte in der Legende an
    plt.legend()
    #Zeigt nur den ausgewählten Bereich an
    plt.xlim(0, 10)
    #Bild für den Bericht speichern
    plt.savefig(r"Bilder\aufgabe2_logarithmisch_logarithmisch.png", dpi=600, bbox_inches="tight")

def Aufgabe2_log_log2():
    # Definiert den Wertebereich der Funktion
    x = np.linspace(0.000001, 10, 30000)
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
        fontsize=10
    )

    # Achsenbeschriftungen
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Gitter (für log-Skala besser mit which="both")
    ax.grid(True, which="both")

    # Bereich einschränken (untere Grenze > 0 wegen log-Skala!)
    ax.set_xlim(0.000001, 10)

    
#Aufruf der Funktion
if __name__ == "__main__":
    Aufgabe2_linear_linear()
    Aufgabe2_log_linear()
    Aufgabe2_log_log()
    Aufgabe2_log_log2()
    plt.show()