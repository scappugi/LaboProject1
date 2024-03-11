class Heap:
    def __init__(self):

        self.lista = []  # dichiarata la lista che conterrà tutti i valori di heap
        self.heapSize = 0

    def add(self, valore):
        self.lista.append(valore)
        self.heapSize += 1

    def swap(self, fpos, spos):

        self.lista[fpos], self.lista[spos] = (self.lista[spos], self.lista[fpos])

    def inserisci_elemento(self, valore):

        self.lista.append(valore)
        self.heapSize += 1
        self.max_heapify(self.heapSize - 1)
        '''  def heapify_up(self, i):   posso usare questo metodo al posto di build max heap
        while i > 0:
            genitore = self.parent(i)
            if self.lista[i] > self.lista[genitore]:
                # Scambia l'elemento con il suo genitore se viola la proprietà dell'heap
                self.lista[i], self.lista[genitore] = self.lista[genitore], self.lista[i]
                i = genitore
            else:
                break'''

    def left(self, i):

        return 2 * i

    def right(self, i):

        return 2 * i + 1

    def parent(self, i):

        return i // 2

    def max_heapify(self, index):  # i è il valore della radix attuale a cui stiamo applicando la nostra funzione

        while index > 0:
            parent_index = (index - 1) // 2
            if self.lista[index] > self.lista[parent_index]:
                # Swap the current element with its parent
                self.lista[index], self.lista[parent_index] = self.lista[parent_index], self.lista[index]
                index = parent_index
            else:
                break

    def build_max_heap(self):

        self.heapSize = len(self.lista)  # qua heapSize acquisisce un valore

        for i in range(len(self.lista) // 2, 0, -1):
            self.max_heapify(i)

    def heap_sort(self):

        self.build_max_heap()

        for i in range(len(self.lista), 0, -2):
            self.lista[1], self.list[i] = self.lista[i], self.lista[1]
            self.heapSize = self.heapSize - 1
            self.max_heapify(1)

    def heap_maximum(self):

        if self.heapSize >= 1:
            return self.lista[1]

        else:
            return None  # Restituisci None se l'heap è vuoto

    def cerca_rango(self, valore):

        for i in range(1, self.heapSize + 1):  # il rango partendo da 1 facciamo cosi e non da 0
            if self.lista[i] == valore:
                return i  # Rango trovato

        return -1  # Elemento non trovato

    def aggiorna_elemento(self, indice, nuovo_valore):
        if 0 <= indice < self.heapSize:
            self.lista[indice] = nuovo_valore
            self.max_heapify(indice)

    def rimuovi_elemento(self, indice):
        if 0 <= indice < self.heapSize:
            # Sostituisci l'elemento da rimuovere con l'ultimo elemento
            self.lista[indice] = self.lista[self.heapSize - 1]
            self.heapSize -= 1
            self.max_heapify(indice)  # sufficiente max_heapify poichè aggiusto solo il sottoalbero
