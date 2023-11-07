import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from LCS import *


def random_string_generator(length=2, min_value=0, max_value=1):  # metodo per la generazione casuale delle sequenze da testare
    sequence = ""
    for i in range(length):
        sequence += str(random.randint(min_value, max_value))
    return sequence

import string

number_of_strings = 10
length_of_string = 10
for x in range(number_of_strings):
    print(
        "".join(
            random.choice(string.ascii_uppercase)
            for _ in range(length_of_string)
        )
    )

if __name__ == '__main__':
    print("\n")
    print("********************************************************************")
    print("* Programma per il confronto dei metodi                            *")
    print("* Forza Bruta, Ricorsivo, Ricorsivo con Memoization e Bottom Up    *")
    print("* per il calcolo della LCS tra sequenze generate casualmente       *")
    print("********************************************************************")
    print("\n")

    for i in range(5):  # controllo sull'input della dimensione minima
        i -= 1
        minLength = input("Inserisci la dimensione minima delle sequenze (min 1): ")
        minLength = int(minLength)
        if minLength >= 1:
            break

    for i in range(5):  # controllo sull'input della dimensione massima
        i -= 1
        maxLength = input("Inserisci la dimensione massima delle sequenze (si consiglia max 16): ")
        maxLength = int(maxLength)
        if maxLength >= minLength:
            break

    for i in range(5):  # controllo sull'input dell'incremento per la generazione delle diverse sequenze
        i -= 1
        step = input("Inserisci lo step di generazione delle sequenze (min 1): ")
        step = int(step)
        if step >= 1:
            break

    timeArrayBruteForce = []
    timeArrayRecursive = []
    timeArrayRecursiveMemo = []
    timeArrayBottomUp = []
    stepArray = []

    for i in range(minLength, maxLength + 1, step):
        sequence1 = random_string_generator(i, 0, 9)  # sequenza X generata casualmente
        sequence2 = random_string_generator(i, 0, 9)  # sequenza Y generata casualmente
        print("\n")
        print("Dimensione: ", i)
        print("Sequenze generate casualmente e confrontate: ", sequence1, "  ", sequence2)

        stepArray.append(i)  # array con la dimensione delle sequenze per le ascisse dei grafici

        lcs1 = LCS(
            sequence1)  # creazione dell'oggetto LCS a cui verrà passata X come attributo e Y come parametro di volta in volta

        # misurazioni sull'algoritmo brute force
        start = timer()
        lcs1.lcs_bruteForce(sequence2)
        end = timer()
        timeArrayBruteForce.append(end - start)

        # misurazioni sull'algoritmo puramente ricorsivo
        start = timer()
        lcs1.lcs_recursive(sequence2)
        end = timer()
        timeArrayRecursive.append(end - start)

        # misurazioni sull'algoritmo ricorsivo con memoization
        start = timer()
        lcs1.lcs_memoization(sequence2)
        end = timer()
        timeArrayRecursiveMemo.append(end - start)

        # misurazioni sull'algoritmo bottom-up
        start = timer()
        lcs1.lcs_bottomUp(sequence2)
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