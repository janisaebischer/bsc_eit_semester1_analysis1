import matplotlib.pyplot as plt
import numpy as np

#Funktion f(x) = sin(1/x) / (1/x) für x > 0
#Funktion wird einmal definiert damit es simplere Aufrufe gibt
def f(x):
    return np.sin(1 / x) / (1 / x)

#Funktion Aufgabe1 wird hier definiert
def Aufgabe1():
    #Definiert den Wertebereich der Funktion, hier von 1-20 mit 10000 Messpunkten dazwischen
    x = np.linspace(0.000001, 5, 30000) 
    #Aufruf der zuvor definierten Funktion, also unsere Funktion aus der Aufgabenstellung. Abbildung mit der entsprechenden Funktion auf y
    y = f(x)
    #Zeichnet den Graphen in Abhängikeit mit den zuvor definierten x und y. Das Label wir anschliessend unten in der Legende angezeigt. Das r ist da, um die Formel in LaTeX-Syntax einzugeben
    plt.plot(x, y, color="blue",label=r"$f(x) = \frac{\sin(1/x)}{1/x}$",linewidth=0.6)
    #Zeichnet die Asymptote in den Graphen ein. Diverse Parameter wie Farbe und Linienstil können eingegeben werden. Label analog wie oben
    plt.axhline(1, color="orange", linestyle="--", label="Asymptote y = 1")
    #Eingabe des Titels, erneut in LaTex-Syntax
    plt.title(r"$f(x) = \frac{\sin(1/x)}{1/x}$")
    #X-Achsenbeschriftung
    plt.xlabel("x")
    #Y-Achsenbeschriftung
    plt.ylabel("f(x)")
    #Anzeige des XY-Gitters
    plt.grid(True)
    #Zeigt die in den "label" definierten Texte in der Legende an
    plt.legend()
    #Zeigt nur den Bereich zwischen 0 und 5 an
    plt.xlim(0, 5)
    #Bild für den Bericht speichern
    plt.savefig(r"Bilder\aufgabe1.png", dpi=600, bbox_inches="tight")
    #Plot anzeigen
    plt.show()

#Aufruf der Funktion
if __name__ == "__main__":
    Aufgabe1()