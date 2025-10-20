class Passeggero:
    def __init__(self, codice_passeggero, nome, cognome):
        self.codice_passeggero = codice_passeggero
        self.nome = nome
        self.cognome = cognome

    def __eq__(self, other):
        if not isinstance(other, Passeggero):
            return False
        return self.codice_passeggero == other.codice_passeggero

    def __str__(self):
        return f'{self.codice_passeggero} - {self.nome} - {self.cognome}'

