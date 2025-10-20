import csv
from cabina import Cabina
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.cabine = []
        self.passeggeri = []

    def aggiorna_nome_crociera(self, nuovo_nome):
        self.nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for riga in reader:
                    if len(riga) == 3:
                        codice_passeggero = riga[0]
                        nome = riga[1]
                        cognome = riga[2]

                        passeggero = Passeggero(codice_passeggero, nome, cognome)
                        self.passeggeri.append(passeggero)

                    elif len(riga) == 4:
                        codice_cabina = riga[0]
                        num_letti = int(riga[1])
                        num_ponte = int(riga[2])
                        prezzo = int(riga[3])

                        cabina = Cabina(codice_cabina, num_letti, num_ponte, prezzo)
                        self.cabine.append(cabina)

                    elif len(riga) == 5 and riga[4].isdigit(): # Il metodo .isdigit() controlla se la stringa contiene solo cifre
                        codice_cabina = riga[0]
                        num_letti = int(riga[1])
                        num_ponte = int(riga[2])
                        prezzo = int(riga[3])
                        num_animali = int(riga[4])

                        cabina = Cabina(codice_cabina, num_letti, num_ponte, prezzo, num_animali)
                        self.cabine.append(cabina)

                    else:
                        codice_cabina = riga[0]
                        num_letti = int(riga[1])
                        num_ponte = int(riga[2])
                        prezzo = int(riga[3])
                        tipologia = riga[4]

                        cabina = Cabina(codice_cabina, num_letti, num_ponte, prezzo, tipologia)
                        self.cabine.append(cabina)

        except FileNotFoundError:
            raise FileNotFoundError(f'File {file_path} non trovato')

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

        # Trova la cabina
        cabina_trovata = None
        for c in self.cabine:
            if c.codice_cabina == codice_cabina:
                cabina_trovata = c
                break

        if cabina_trovata is None:
            raise Exception(f"Codice {codice_cabina} non presente nel sistema.")

        # Trova il passeggero
        passeggero_trovato = None
        for p in self.passeggeri:
            if p.codice_passeggero == codice_passeggero:
                passeggero_trovato = p
                break

        if passeggero_trovato is None:
            raise Exception(f"Codice {codice_passeggero} non presente nel sistema.")

        # Controllo che la cabina sia disponibile
        if not cabina_trovata.disponibilità:
            raise Exception(f"La cabina {codice_cabina} è già occupata.")

        # Controllo che il passeggero non sia già assegnato a un'altra cabina
        for c in self.cabine:
            if c.passeggero == passeggero_trovato:
                raise Exception(f"Il passeggero {passeggero_trovato.codice_passeggero} è già assegnato a una cabina.")

        # Se tutte le condizioni sono verificate, assegno il passeggero alla cabina
        cabina_trovata.passeggero = passeggero_trovato
        cabina_trovata.disponibilità = False


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        return sorted(self.cabine, key=lambda c: c.prezzo, reverse=True) # reverse=True ordina in ordine decrescente (dal più costoso al meno costoso), senza scrivere reverse=True fa il contrario

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for p in self.passeggeri:
            cabina = None
            for c in self.cabine:
                if c.passeggero == p:
                    cabina = c
                    break

            if cabina is None:
                print(f'{p.codice_passeggero}')
            else:
                print(f'{p.codice_passeggero} - {c.codice_cabina}')