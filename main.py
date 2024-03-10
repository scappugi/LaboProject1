import os
import timeit
#from time import perf_counter as timer

from timeit import default_timer as timer

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
import random
from Listaconcatenata import Nodo
from Listaconcatenata import ListaConcatenata
import Heap
import Listaconcatenataordinata

#servono per creare struttre dinamiche
def valuesRandomListConc(valMax):
    # Creo lista con i valori randomici
    valori = ListaConcatenata()
    '''for k in range(valMax):
        #  valori.aggiungi_elemento(Nodo(random.randint(0, valMax)))
        valori.aggiungi_elemento(random.randint(0, valMax))'''
    return valori



def testLista(dimMax, numRipet):
    tempi_inserimento = []  # Lista per memorizzare i tempi di inserimento
    for i in range(1, dimMax, 10):
        tempo_inserimento_medio = 0
        tempo_totale = 0
        valore = valuesRandomListConc(i)

        for j in range(numRipet):
            start_timer = timer()
            valore.aggiungi_elemento(random.randint(0, i))
            fine_timer = timer()
            iterationTime = fine_timer - start_timer
            tempo_totale += iterationTime
            valore.cancella_in_testa()

        tempo_inserimento_medio = tempo_totale / numRipet
        tempi_inserimento.append(tempo_inserimento_medio)
        # disegno del grafico

    asse_x = [i for i in range(1, dimMax, 10)]
    plt.plot(asse_x, tempi_inserimento, label="insert ", color="orange")
    plt.xlabel('Dimensione Lista')
    plt.ylabel('Tempo di Inserimento (secondi)')
    plt.title('Tempo di Inserimento in Lista Concatenata')
    plt.grid(True)
    plt.show()




# Esegui il test con i valori desiderati
print("ciao")
testLista(dimMax=10000, numRipet=10000)
print("ciao")
