class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.successivo = None


class ListaConcatenata:
    def __init__(self):
        self.testa = None

    def aggiungi_elemento(self, dato):  # inserimento in testa
        nodo = Nodo(dato)
        nodo.successivo = self.testa
        self.testa = nodo



    def ricerca_elemento(self, valoreDaCercare):
        """
        Cerca il valore nella lista e restituisce l'indice della prima occorrenza se presente.
        Restituisce -1 se il valore non è trovato.
        """
        corrente = self.testa
        indice = 0

        while corrente:
            if corrente.valore == valoreDaCercare:
                return indice  # Valore trovato, restituisce l'indice
            corrente = corrente.successivo
            indice += 1

        return -1  # Valore non trovato


    def trova_massimo(self):
        if not self.testa:
            return None  # Lista vuota

        nodo = self.testa
        massimo = nodo.valore
        corrente = nodo.successivo

        while corrente:
            if corrente.valore > massimo:
                massimo = corrente.valore
            corrente = corrente.successivo

        return massimo


    def trova_rango(self,
                    valore):  # questa funzione non ordina ma cerca solamente il rango, potrebbe essere utile guardarla anche nel caso la lista sia ordinata
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


    def aggiorna_elemento(self, posizione,
                          nuovoValore):  # la posizione specifica la posizione dove effettuare l' aggiornamento
        # devo comuque scorrere tutta la lista poichè non cè
        # modo di sapere a priori quanti elementi vi sono al suo interno

        corrente = self.testa

        for i in range(1, posizione, 1):
            if i == posizione - 1:
                if corrente:
                    corrente.valore = nuovoValore
                    return True  # elemento trovato e modificato
                else:
                    return False
            if corrente:
                corrente = corrente.successivo  # iteratore

        return False  # Elemento non trovato


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


    def cancella_in_testa(self):
        if self.testa:
            self.testa = self.testa.successivo
