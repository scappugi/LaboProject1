import os
import timeit
from time import perf_counter as ptimer
from timeit import default_timer as timer
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import copy

matplotlib.use('TkAgg')

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


def valuesRandomListConc2(lista, passo, dimMax):
    for k in range(passo):
        lista.aggiungi_elemento(random.randint(0, dimMax))

def valuesRandomListConcOrdinata(lista, passo, dimMax):
    for k in range(passo):
        lista.aggiungi_elemento_o(random.randint(0,dimMax))

def valuesRandomHeap(dimensione):  # crea un heap dinamico con n elementi randomici (costo log)
    heap = Heap.Heap()
    for k in range(dimensione):
        # heap.inserisci_elemento(random.randint(0, 100))
        heap.add(random.randint(0, dimensione))  # inserisce senza aggiustare

    heap.build_max_heap()
    return heap


def valuesRandomHeap2(heap, passo,dimMax):  # passo identifica quanto vuoi inghrandire il tuo heap
    for k in range(passo):
        heap.inserisci_elemento(random.randint(0, heap.heapSize))


def valuesRandomListaO(dimensione):
    valori = ListaConcatenataOrdinata()
    for k in range(dimensione):
        valori.aggiungi_elemento_o(random.randint(0, dimensione))
    return valori




def testMediaEsternaAdd(dimMax, numRipet):
    tempi_inserimento = []
    tempi_media = []
    progress_bar = tqdm(total=numRipet, desc="Inserimento Lista Random")
    for i in range(0, numRipet, 1):  # gestisce quante volte fare l' esperimento
        k = 0
        passo = 1
        lista = ListaConcatenata()
        for j in range(0, dimMax, 10):
            valuesRandomListConc2(lista, passo, dimMax)
            if j == 0:
                passo = 10
            dato = random.randint(0, j)
            t_inizio = ptimer()
            lista.aggiungi_elemento(dato)
            t_fine = ptimer()
            lista.rimuovi_elemento(dato)
            t_esecuzione = t_fine - t_inizio
            if i == 0:  # siamo nella prima iterazione e il vettore tempi è vuoto
                tempi_inserimento.append(t_esecuzione)
            else:
                tempi_inserimento[k] += t_esecuzione
            k += 1
        progress_bar.update(1)

    progress_bar.close()
    # calcolo la media di ogni elemento di tempi_inserimento
    for l in range(len(tempi_inserimento)):
        media = tempi_inserimento[l] / numRipet
        tempi_media.append(media)




    asse_x = [i for i in range(0, dimMax, 10)]
    plt.plot(asse_x, tempi_media, label="insert", color="green")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di Inserimento (secondi)')
    plt.title('Tempo di Inserimento')
    plt.grid(True)
    plt.legend()
    plt.show()


def testMediaEsternaHash(dimMax, numRipet):
    tempi_inserimento = []
    tempi_media = []
    #barretta di caricamento:

    progress_bar = tqdm(total=numRipet, desc="In esecuzione...")

    for i in range(0, numRipet, 1):  # gestisce quante volte fare l' esperimento
        k = 0
        heap = Heap.Heap()
        passo = 1
        for j in range(0, dimMax, 10):
            valuesRandomHeap2(heap, passo, dimMax)
            if j == 0:
                passo = 10
            dato = random.randint(0, heap.heapSize)
            #INIZIO DEL TIMER

            t_inizio = ptimer()
            heap.inserisci_elemento(dato)
            t_fine = ptimer()

            #FINE DEL TIMER
            heap.rimuovi_elemento_per_valore(dato)
            t_esecuzione = t_fine - t_inizio
            if i == 0:  # siamo nella prima iterazione e il vettore tempi è vuoto
                tempi_inserimento.append(t_esecuzione)
            else:
                tempi_inserimento[k] += t_esecuzione
            k += 1
        progress_bar.update(1)

    progress_bar.close()


    # calcolo la media di ogni elemento di tempi_inserimento
    for l in range(len(tempi_inserimento)):
        media = tempi_inserimento[l] / numRipet
        tempi_media.append(media)

    asse_x = [i for i in range(0, dimMax, 10)]
    plt.plot(asse_x, tempi_media, label="insert", color="blue")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di Inserimento (secondi)')
    plt.title('Tempo di Inserimento')
    plt.grid(True)
    plt.legend()
    plt.show()


def testMediaEsternaHashCHATGPT(dimMax, numRipet):
    tempi_inserimento = [[] for _ in range(dimMax)]  # Lista di liste per memorizzare i tempi di inserimento
    print(f'num di iterazioni totali {numRipet}')

    for i in range(numRipet):
        heap = Heap.Heap()
        if i % 100 == 0:
            print(f'iterazione {i}')

        for j in range(dimMax):
            valuesRandomHeap2(heap, j)  # Aggiungi j elementi casuali all'heap
            dato = random.randint(0, heap.heapSize)
            t_inizio = ptimer()
            heap.inserisci_elemento(dato)
            t_fine = ptimer()
            heap.rimuovi_elemento_per_valore(dato)
            tempi_inserimento[j].append(
                t_fine - t_inizio)  # Aggiungi il tempo di inserimento alla lista corrispondente alla dimensione j

    # Calcola la media per ogni dimensione
    tempi_media = [sum(tempi) / numRipet for tempi in tempi_inserimento]

    # Disegna il grafico
    asse_x = [i for i in range(dimMax)]
    plt.plot(asse_x, tempi_media, label="insert", color="blue")
    plt.xlabel('Dimensione Heap')
    plt.ylabel('Tempo di Inserimento Medio (secondi)')
    plt.title('Tempo di Inserimento Medio per Dimensione Heap')
    plt.grid(True)
    plt.legend()
    plt.show()

def testMediaEsternaAddListaOrdinata(dimMax, numRipet):
    tempi_inserimento = []
    tempi_media = []
    #barretta di caricamento:

    progress_bar = tqdm(total=numRipet, desc="In esecuzione")

    for i in range(0, numRipet, 1):  # gestisce quante volte fare l' esperimento
        k = 0
        lista = ListaConcatenataOrdinata()
        passo = 1
        for j in range(0, dimMax, 10):
            valuesRandomListConcOrdinata(lista,passo,dimMax)
            if j == 0:
                passo = 10
            dato = random.randint(0, dimMax)
            #INIZIO DEL TIMER

            t_inizio = ptimer()
            lista.aggiungi_elemento_o(dato)
            t_fine = ptimer()

            #FINE DEL TIMER
            lista.rimuovi_elemento(dato)
            t_esecuzione = t_fine - t_inizio
            if i == 0:  # siamo nella prima iterazione e il vettore tempi è vuoto
                tempi_inserimento.append(t_esecuzione)
            else:
                tempi_inserimento[k] += t_esecuzione
            k += 1
        progress_bar.update(1)

    progress_bar.close()


    # calcolo la media di ogni elemento di tempi_inserimento
    for l in range(len(tempi_inserimento)):
        media = tempi_inserimento[l] / numRipet
        tempi_media.append(media)

    asse_x = [i for i in range(0, dimMax, 10)]
    plt.plot(asse_x, tempi_media, label="insert", color="blue")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di Inserimento (secondi)')
    plt.title('Tempo di Inserimento')
    plt.grid(True)
    plt.legend()
    plt.show()

def testMediaEsternaMaxListaOrdinata(dimMax, numRipet):
    tempi_inserimento = []
    tempi_media = []
    #barretta di caricamento:

    progress_bar = tqdm(total=numRipet, desc="In esecuzione")

    for i in range(0, numRipet, 1):  # gestisce quante volte fare l' esperimento
        k = 0
        lista = ListaConcatenataOrdinata()
        passo = 1
        for j in range(0, dimMax, 10):
            valuesRandomListConcOrdinata(lista,passo,dimMax)
            if j == 0:
                passo = 10
            dato = random.randint(0, dimMax)
            #INIZIO DEL TIMER

            t_inizio = timer()
            lista.trova_massimo()
            t_fine = timer()

            #FINE DEL TIMER
            t_esecuzione = t_fine - t_inizio
            if i == 0:  # siamo nella prima iterazione e il vettore tempi è vuoto
                tempi_inserimento.append(t_esecuzione)
            else:
                tempi_inserimento[k] += t_esecuzione
            k += 1
        progress_bar.update(1)

    progress_bar.close()


    # calcolo la media di ogni elemento di tempi_inserimento
    for l in range(len(tempi_inserimento)):
        media = tempi_inserimento[l] / numRipet
        tempi_media.append(media)

    asse_x = [i for i in range(0, dimMax, 10)]
    plt.plot(asse_x, tempi_media, label="find Max", color="blue")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di ricerca (secondi)')
    plt.title('Tempo di ricerca Max')
    plt.grid(True)
    plt.legend()
    plt.show()





testMediaEsternaMaxListaOrdinata(50,2)
