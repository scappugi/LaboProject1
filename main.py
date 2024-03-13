import os
import timeit
from time import perf_counter as ptimer
from timeit import default_timer as timer
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
import random
from Listaconcatenata import ListaConcatenata
import Heap
from Listaconcatenataordinata import ListaConcatenataOrdinata

'''
       CREO STRUTTURE DINAMICHE
'''


def valuesRandomListConc(dimensione):
    # Creo lista con i valori randomici
    valori = ListaConcatenata()
    for k in range(dimensione):
        #  valori.aggiungi_elemento(Nodo(random.randint(0, valMax)))
        valori.aggiungi_elemento(random.randint(0, dimensione))
    return valori


def valuesRandomHeap(dimensione):  # crea un heap dinamico con n elementi randomici (costo log)
    heap = Heap.Heap()
    for k in range(dimensione):
        # heap.inserisci_elemento(random.randint(0, 100))
        heap.add(random.randint(0, 100))  # inserisce senza aggiustare

    heap.build_max_heap()
    return heap


def valuesRandomListaO(dimensione):
    valori = ListaConcatenataOrdinata()
    for k in range(dimensione):
        valori.aggiungi_elemento_o(random.randint(0, dimensione))
    return valori


'''
        TEST PER LISTA CONCATENATA
'''


def testAddLista2(dimMax, numRipet):
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


def testAddLista1(dimMax, numRipet):
    tempi_inserimento = []  # Lista per memorizzare i tempi di inserimento
    for i in range(1, dimMax, 5):  # Modifica l'incremento a 1
        lista = valuesRandomListConc(i)
        tempi = timeit.repeat(lambda: lista.aggiungi_elemento(random.randint(0, i)), number=numRipet, repeat=10)
        tempo_medio = np.mean(tempi)
        tempi_inserimento.append(tempo_medio)

    asse_x = [i for i in range(1, dimMax, 5)]
    plt.plot(asse_x, tempi_inserimento, label="insert ", color="orange")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di Inserimento (secondi)')
    plt.title('Tempo di Inserimento in Lista Concatenata')
    plt.grid(True)
    plt.show()


def testRicercaMaxLista(dimMax, numRipet):
    tempi_inserimento = []
    for i in range(1, dimMax, 100):
        lista = valuesRandomListConc(dimensione=i)
        tempi = timeit.repeat(lambda: lista.trova_massimo(), number=numRipet, repeat=1)
        tempo_medio = np.mean(tempi)
        tempi_inserimento.append(tempo_medio)

    asse_x = [i for i in range(1, dimMax, 100)]
    plt.plot(asse_x, tempi_inserimento, label="insert ", color="blue")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di ricerca max (secondi)')
    plt.title('Tempo di ricerca massimo in Lista Concatenata')
    plt.grid(True)
    plt.show()


def testAggiornaElementoLista(dimMax, numRipet):
    tempi_inserimento = []
    for i in range(1, dimMax, 1):
        lista = valuesRandomListConc(dimensione=i)
        tempi = timeit.repeat(lambda: lista.aggiorna_elemento(random.randint(0, i), random.randint(0, i)),
                              number=numRipet, repeat=1)
        tempo_medio = np.mean(tempi)
        tempi_inserimento.append(tempo_medio)

    asse_x = [i for i in range(1, dimMax, 1)]
    plt.plot(asse_x, tempi_inserimento, label="insert ", color="blue")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di ricerca max (secondi)')
    plt.title('Tempo di Inserimento in Lista Concatenata')
    plt.grid(True)
    plt.show()


'''
        TEST PER HEAP
'''


def testaddHeap(dimMax, numRipet):
    tempi_inserimento = []
    for i in range(1, dimMax, 100):
        heap = valuesRandomHeap(i)
        tempi = timeit.repeat(lambda: heap.inserisci_elemento(random.randint(0, i)), number=numRipet,
                              repeat=1)  # questo temp dovrebbe essere logaritmico

        tempo_medio = np.mean(tempi)
        tempi_inserimento.append(tempo_medio)

    asse_x = [i for i in range(1, dimMax, 100)]
    plt.plot(asse_x, tempi_inserimento, label="insert ", color="blue")
    # plt.semilogy(asse_x, tempi_inserimento, label="insert ", color="blue")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di inserimento')
    plt.title('Tempo di Inserimento in un Heap')
    plt.grid(True)
    plt.show()


def testAddHeap2(dimMax, numRipet):
    tempi_inserimento = []

    for i in range(1, dimMax, 50):
        heap = valuesRandomHeap(i)

        tempi = []
        for _ in range(numRipet):
            start_time = ptimer()
            heap.inserisci_elemento(random.randint(0, i))
            end_time = ptimer()
            tempi.append(end_time - start_time)

        tempo_medio = np.mean(tempi)
        tempi_inserimento.append(tempo_medio)

    asse_x = [i for i in range(1, dimMax, 50)]
    plt.plot(asse_x, tempi_inserimento, label="insert ", color="blue")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di inserimento')
    plt.title('Tempo di Inserimento in un Heap')
    plt.grid(True)
    plt.show()


def testMaxheapifyHeap(dimMax, numRipet):
    tempi_inserimento = []
    for i in range(1, dimMax, 100):
        heap = Heap.Heap()
        for j in range(i):
            heap.add(random.randint(0, i))
        tempi = timeit.repeat(lambda: heap.max_heapify(i - 1), number=numRipet, repeat=10)
        tempo_medio = np.mean(tempi)
        tempi_inserimento.append(tempo_medio)

    asse_x = [i for i in range(1, dimMax, 100)]
    plt.plot(asse_x, tempi_inserimento, label="insert ", color="blue")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo (secondi)')
    plt.title('Tempo di esecuzione maxheapify')
    plt.grid(True)
    plt.show()


def testFindMaxHeap(dimMax, numRipet):
    tempi_inserimento = []
    for i in range(1, dimMax, 5):
        heap = Heap.Heap()
        for j in range(i):
            heap.add(random.randint(0, i))
        tempi = timeit.repeat(lambda: heap.heap_maximum(), number=numRipet, repeat=10)
        tempo_medio = np.mean(tempi)
        tempi_inserimento.append(tempo_medio)

    asse_x = [i for i in range(1, dimMax, 5)]
    plt.plot(asse_x, tempi_inserimento, label="insert ", color="green")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo (secondi)')
    plt.title('Tempo di esecuzione heap maximum')
    plt.grid(True)
    plt.show()


'''
        TEST PER LISTA CONCATENATA ORDINATA
'''

def testAddListaO(dimMax, numRipet):
    tempi_inserimento = []  # Lista per memorizzare i tempi di inserimento
    for i in range(1, dimMax, 100):  # Modifica l'incremento a 1
        lista = valuesRandomListaO(dimensione=i)
        tempi = timeit.repeat(lambda: lista.aggiungi_elemento_o(random.randint(0, i)), number=numRipet, repeat=1)
        tempo_medio = np.mean(tempi)
        tempi_inserimento.append(tempo_medio)

    asse_x = [i for i in range(1, dimMax, 100)]
    plt.plot(asse_x, tempi_inserimento, label="insert ", color="orange")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di Inserimento (secondi)')
    plt.title('Tempo di Inserimento in Lista Concatenata Ordinata')
    plt.grid(True)
    plt.show()






# Esegui il test con i valori desiderati
print("ciao")
# testAddLista1(dimMax=2000, numRipet=1000)
# testRicercaMaxLista(dimMax=5000, numRipet=1000)  # ok
# testAggiornaElementoLista(dimMax=100, numRipet=10)
# testAddHeap2(dimMax=10000, numRipet=5000)
# testMaxheapifyHeap(10000,50000)
# testFindMaxHeap(2000, 1000)
testAddListaO(dimMax=2000, numRipet=1000)
print("ciao")





max_heap = Heap.Heap()
max_heap.inserisci_elemento(4)
max_heap.inserisci_elemento(10)
max_heap.inserisci_elemento(8)
max_heap.inserisci_elemento(5)
max_heap.inserisci_elemento(7)
max_heap.inserisci_elemento(14)
max_heap.inserisci_elemento(22)
max_heap.inserisci_elemento(4)
max_heap.rimuovi_elemento(3)

print(max_heap.lista)
