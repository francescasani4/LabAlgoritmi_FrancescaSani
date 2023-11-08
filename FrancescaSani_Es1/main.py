import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from LCS import *
import string

timeArrayBruteForce = []
timeArrayRecursive = []
timeArrayRecursiveMemo = []
timeArrayBottomUp = []
stepArray = []

maxLength = 100
j = 15

def random_string_generator(length):
    sequence = ""
    for x in range(length):
        sequence = ("".join(random.choice(string.ascii_uppercase)for _ in range(length)))
    return sequence

if __name__ == '__main__':
    print("\n")
    print("********************************************************************")
    print("* Programma per il confronto dei metodi                            *")
    print("* Forza Bruta, Ricorsivo, Ricorsivo con Memoization e Bottom Up    *")
    print("* per il calcolo della LCS tra sequenze generate casualmente       *")
    print("********************************************************************")
    print("\n")

    for i in range(1, maxLength, j):
        s1 = random_string_generator(i)  # sequenza X generata casualmente
        s2 = random_string_generator(i)  # sequenza Y generata casualmente
        print("\n")
        print("Dimensione: ", i)
        print("Sequenze generate casualmente e confrontate: ", s1, "  ", s2)

        stepArray.append(i)  # array con la dimensione delle sequenze per le ascisse dei grafici

        lcs1 = LCS(s1)  # creazione dell'oggetto LCS a cui verrà passata X come attributo e Y come parametro di volta in volta

        # misurazioni sull'algoritmo brute force
        start = timer()
        print("LCS: ", lcs1.lcs_bruteForce(s2))
        end = timer()
        timeArrayBruteForce.append(end - start)

        # misurazioni sull'algoritmo puramente ricorsivo
        start = timer()
        print("LCS: ", lcs1.lcs_recursive(s2))
        end = timer()
        timeArrayRecursive.append(end - start)

        # misurazioni sull'algoritmo ricorsivo con memoization
        start = timer()
        print("LCS: ", lcs1.lcs_memoization(s2))
        end = timer()
        timeArrayRecursiveMemo.append(end - start)

        # misurazioni sull'algoritmo bottom-up
        start = timer()
        print("LCS: ", lcs1.lcs_bottomUp(s2))
        end = timer()
        timeArrayBottomUp.append(end - start)

    # si plottano 4 grafici per confrontare i metodi
    figure, axis = plt.subplots(2, 2)

    figure.suptitle("Confronto delle prestazioni dei 4 metodi")

    axis[0, 0].plot(stepArray, timeArrayBruteForce)
    axis[0, 0].set_title("Forza bruta")

    axis[0, 1].plot(stepArray, timeArrayRecursive)
    axis[0, 1].set_title("Ricorsivo")

    axis[1, 0].plot(stepArray, timeArrayRecursiveMemo)
    axis[1, 0].set_title("Ricorsivo con Memoization")

    axis[1, 1].plot(stepArray, timeArrayBottomUp)
    axis[1, 1].set_title("Bottom-Up")

    print("\nTempi di esecuzione algoritmo Forza Bruta: ")
    print(timeArrayBruteForce)

    print("\nTempi di esecuzione algoritmo Ricorsivo: ")
    print(timeArrayRecursive)

    print("\nTempi di esecuzione algoritmo Ricorsivo con Memoization: ")
    print(timeArrayRecursiveMemo)

    print("\nTempi di esecuzione algoritmo Bottom-Up: ")
    print(timeArrayBottomUp)

    i = 0
    for ax in axis.flat:
        if i == 0 or i == 2:
            ax.set(ylabel='Tempo di esecuzione')

        if i == 2 or i == 3:
            ax.set(xlabel='Dimensione della sequenza')
        i += 1

    plt.tight_layout()
    plt.savefig("Confronto_metodi_LCS.png")
    plt.show()