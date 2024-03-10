class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.successivo = None


class ListaConcatenataOrdinata:  # la lista è ordinata dal valore maggiore al valore minore
    def __init__(self):
        self.testa = None

    def aggiungi_elemento(self, nuovo_valore):
        nuovo_nodo = Nodo(nuovo_valore)

        # Caso in cui la lista è vuota o il nuovo valore è maggiore del valore in testa
        if not self.testa or nuovo_valore > self.testa.valore:
            nuovo_nodo.successivo = self.testa
            self.testa = nuovo_nodo
            return

        # Trova il nodo precedente all'inserto
        precedente = None
        corrente = self.testa
        while corrente and corrente.valore < nuovo_valore:
            precedente = corrente
            corrente = corrente.successivo

        # Inserisci il nuovo nodo tra il nodo precedente e il nodo corrente
        nuovo_nodo.successivo = corrente
        precedente.successivo = nuovo_nodo

    def trova_massimo(self):
        if not self.testa:
            return None  # Lista vuota

        return self.testa.valore  # ritorna il primo valore

    def trova_rango(self, valore):
        if not self.testa:
            return None  # Lista vuota

        nodo = self.testa
        rango = 1

        while nodo:
            if nodo.valore == valore:
                return rango
            rango = rango + 1
            nodo = nodo.successivo

        return -1  # se l' elemento non esiste nella lista alloraa torna con -1

    def ricerca_sequenziale(self, valore):
        corrente = self.testa

        while corrente:
            if corrente.valore == valore:
                return True  # Elemento trovato

            corrente = corrente.successivo

        return False  # Elemento non trovato

    # manca aggiornamento di un element

    def rimuovi_elemento(self, valore_da_rimuovere):
        corrente = self.testa
        precedente = None

        while corrente:
            if corrente.valore == valore_da_rimuovere:
                if precedente:
                    precedente.successivo = corrente.successivo
                else:
                    self.testa = corrente.successivo
                return
            precedente = corrente
            corrente = corrente.successivo
