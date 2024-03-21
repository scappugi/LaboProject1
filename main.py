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
        heap.inserisci_elemento(random.randint(0, dimMax))


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
    for i in range(0, dimMax, 100):
        tempo_inserimento_medio = 0
        tempo_totale = 0
        lista = ListaConcatenata()
        valuesRandomListConc2(lista, 100, dimMax)

        for j in range(numRipet):
            dato = random.randint(0, i)
            start_timer = timer()
            lista.aggiungi_elemento(dato)
            fine_timer = timer()
            lista.rimuovi_elemento(dato)
            iterationTime = fine_timer - start_timer
            tempo_totale += iterationTime

        if i % 100 == 0:
            print(f'iterazione {i}')
        tempo_inserimento_medio = tempo_totale / numRipet
        tempi_inserimento.append(tempo_inserimento_medio)
        # disegno del grafico

    asse_x = [i for i in range(0, dimMax, 100)]
    plt.plot(asse_x, tempi_inserimento, label="insert ", color="orange")
    plt.xlabel('Dimensione Lista')
    plt.ylabel('Tempo di Inserimento (secondi)')
    plt.title('Tempo di Inserimento in Lista Concatenata')
    plt.grid(True)
    plt.show()


def testAddLista1(dimMax, numRipet):
    tempi_inserimento = []  # Lista per memorizzare i tempi di inserimento
    for i in range(0, dimMax, 5):  # Modifica l'incremento a 1
        lista = valuesRandomListConc(i)
        dato = random.randint(0, i)
        tempi = timeit.repeat("lista.aggiungi_elemento(dato)", number=1, repeat=numRipet,
                              globals={"lista": lista, "dato": dato})
        tempo_medio = np.mean(tempi)
        tempi_inserimento.append(tempo_medio)
        if i % 100 == 0:
            print(f'iterazione {i}')

    plt.plot(tempi_inserimento, label="insert ", color="orange")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di Inserimento (secondi)')
    plt.title('Tempo di Inserimento in Lista Concatenata')
    plt.grid(True)
    plt.show()


def testRicercaMaxLista(dimMax, numRipet):
    tempi_inserimento = []
    for i in range(0, dimMax, 100):
        lista = valuesRandomListConc(dimensione=i)
        tempi = timeit.repeat(lambda: lista.trova_massimo(), number=1, repeat=numRipet)
        tempo_medio = np.mean(tempi)
        tempi_inserimento.append(tempo_medio)
        if i % 100 == 0:
            print(f'iterazione {i}')

    asse_x = [i for i in range(0, dimMax, 100)]
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
    for i in range(0, dimMax, 1):
        heap = valuesRandomHeap(i)
        # tempi = timeit.repeat(lambda: heap.inserisci_elemento(random.randint(0, i)), number=1, repeat=numRipet)
        tempi = timeit.repeat("heap.inserisci_elemento(random.randint(0, i+1000))", number=1, repeat=numRipet,
                              globals={"heap": heap, "i": i + 1000},
                              setup='from main import random')  # questo temp dovrebbe essere logaritmico
        if i % 100 == 0:
            print(f'iterazione {i}')
        tempo_medio = sum(tempi) / numRipet

        tempi_inserimento.append(tempo_medio)

        # Calcola i coefficienti del polinomio di grado 10
    coefficients = np.polyfit(range(dimMax), tempi_inserimento, 5)

    # Crea la funzione polinomiale
    polynomial = np.poly1d(coefficients)

    # Calcola i valori approssimati del polinomio per il tracciamento
    approx_values = polynomial(range(dimMax))

    plt.plot(tempi_inserimento, label="insert ", color="blue")
    plt.plot(approx_values, label="Polynomial Fit", color="red")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di inserimento')
    plt.title('Tempo di Inserimento in un Heap')
    plt.grid(True)
    plt.show()


def testAddHeap2(dimMax, numRipet):
    tempi_inserimento = []
    heap = Heap.Heap()
    passo = 0
    for i in range(0, dimMax, 100):
        # heap = valuesRandomHeap(i)
        valuesRandomHeap2(heap, 100)
        tempi = []
        for _ in range(numRipet):
            dato = random.randint(0, i)
            start_time = ptimer()
            heap.inserisci_elemento(dato)
            end_time = ptimer()
            heap.rimuovi_elemento_per_valore(dato)  # rimuove l' elemento inserito o uno uguale a lui
            tempi.append(end_time - start_time)

        tempo_medio = sum(tempi) / len(tempi)
        tempi_inserimento.append(tempo_medio)
        if i % 100 == 0:
            print(f'iterazione {i}')

        # Calcola i coefficienti del polinomio di grado 10
    coefficients = np.polyfit(range(0, dimMax, 100), tempi_inserimento, 10)

    # Crea la funzione polinomiale
    polynomial = np.poly1d(coefficients)

    # Calcola i valori approssimati del polinomio per il tracciamento
    approx_values = polynomial(range(0, dimMax, 100))
    plt.plot(approx_values, label="Polinomio di grado 10", color="red")

    plt.plot(tempi_inserimento, label="insert ", color="blue")
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
            heap.add(random.randint(0, 100000))
        tempi = timeit.repeat(lambda: heap.max_heapify(i - 1), number=numRipet, repeat=5)
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
    for i in range(1, dimMax, 1):
        heap = valuesRandomHeap(dimensione=i)
        tempi = timeit.repeat(lambda: heap.heap_maximum(), number=1, repeat=numRipet)
        tempo_medio = np.mean(tempi)
        tempi_inserimento.append(tempo_medio)
        if i % 100 == 0:
            print(f'iterazione {i}')

    plt.plot(tempi_inserimento, label="insert ", color="green")
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
    for i in range(0, dimMax, 10):  # Modifica l'incremento a 1
        lista = valuesRandomListaO(dimensione=i)
        dato = random.randint(0, i)
        # tempi = timeit.repeat("lista.aggiungi_elemento_o(random.randint(0, i))", number=1, repeat=numRipet,
        #                     globals=locals())  # questo temp dovrebbe essere logaritmico

        tempi = timeit.repeat(lambda: lista.aggiungi_elemento_o(random.randint(0, i)), number=1, repeat=numRipet)
        tempo_medio = sum(tempi) / len(tempi)
        tempi_inserimento.append(tempo_medio)
        if i % 100 == 0:
            print(f'iterazione {i}')

    asse_x = [i for i in range(0, dimMax, 10)]
    plt.plot(asse_x, tempi_inserimento, label="insert ", color="orange")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di Inserimento (secondi)')
    plt.title('Tempo di Inserimento in Lista Concatenata Ordinata')
    plt.grid(True)
    plt.show()


'''
        TEST PER PLOT MULTIPLI
'''


def testAllInserimenti(dimMax, numRipet):
    tempi_inserimento_lista = []  # Lista per memorizzare i tempi di inserimento
    tempi_inserimento_lista_ordinata = []
    tempi_inserimento_heap = []
    for i in range(1, dimMax, 1):  # Modifica l'incremento a 1
        lista = valuesRandomListConc(dimensione=i)
        lista_o = valuesRandomListaO(dimensione=i)
        heap = valuesRandomHeap(dimensione=i)
        dato = random.randint(0, i)
        tempi_lista = timeit.repeat(lambda: lista.aggiungi_elemento(random.randint(0, i)), number=1, repeat=numRipet)
        tempi_heap = timeit.repeat(lambda: heap.inserisci_elemento(random.randint(0, i)), number=1, repeat=numRipet)
        tempi_lista_o = timeit.repeat(lambda: lista_o.aggiungi_elemento_o(random.randint(0, i)), number=1,
                                      repeat=numRipet)
        tempo_medio_lista_o = np.mean(tempi_lista_o)
        tempo_medio_lista = np.mean(tempi_lista)
        tempo_medio_heap = np.mean(tempi_heap)
        tempi_inserimento_lista_ordinata.append(tempo_medio_lista_o)
        tempi_inserimento_lista.append(tempo_medio_lista)
        tempi_inserimento_heap.append(tempo_medio_heap)

    asse_x = [i for i in range(1, dimMax, 1)]
    plt.plot(asse_x, tempi_inserimento_lista_ordinata, label="insert list ord", color="orange")
    plt.plot(asse_x, tempi_inserimento_lista, label="insert list", color="black")
    plt.plot(asse_x, tempi_inserimento_heap, label="insert heap", color="green")
    plt.xlabel('Numero elementi')
    plt.ylabel('Tempo di Inserimento (secondi)')
    plt.title('Tempo di Inserimento')
    plt.grid(True)
    plt.legend()
    plt.show()


def testMediaEsternaAdd(dimMax, numRipet):
    tempi_inserimento = []
    tempi_media = []
    print(f'num di iterazioni totali {numRipet // 100}')
    for i in range(0, numRipet, 1):  # gestisce quante volte fare l' esperimento
        k = 0
        passo = 1
        lista = ListaConcatenata()
        if i % 100 == 0:
            print(f'iterazione {i // 100}')
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
            dato = random.randint(0, dimMax)
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
            valuesRandomListConcOrdinata(lista,10,dimMax)
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


# Esegui il test con i valori desiderati
# testAddLista2(dimMax=50000, numRipet=10000)
# testRicercaMaxLista(dimMax=5000, numRipet=1000)  # ok
# testAggiornaElementoLista(dimMax=100, numRipet=10)
# testAddHeap2(dimMax=1000, numRipet=200)

# testAddHeap2(dimMax=10000, numRipet=10000)
# testMaxheapifyHeap(10000,2000)
# testFindMaxHeap(1000, 100000)
# testAddListaO(dimMax=1000, numRipet=5000)
# testAllInserimenti(100, 50)
#testMediaEsternaAdd(1000, 1000)
testMediaEsternaHash(10000,1000)
testMediaEsternaAddListaOrdinata(1000,500)

