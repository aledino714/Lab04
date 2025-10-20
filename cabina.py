class Cabina:
    def __init__(self, codice_cabina, num_letti, num_ponte, prezzo, tipologia = None, num_animali = None):
        self.codice_cabina = codice_cabina
        self.num_letti = int(num_letti)
        self.num_ponte = int(num_ponte)
        self.prezzo = int(prezzo)
        self.tipologia = tipologia
        self.num_animali = num_animali
        self.disponibilità = True # All'inizio è disponibile
        self.passeggero = None  # # Nessun passeggero assegnato all'inizio

    def __str__(self):
        return f'{self.codice_cabina} - {self.num_letti} - {self.num_ponte} - {self.prezzo} - {self.tipologia} - {self.num_animali}'


