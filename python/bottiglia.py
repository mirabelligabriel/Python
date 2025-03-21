class Bottiglia:
    def __init__(self, capacita):
        self.quantita = 0
        self.capacita = capacita

    def __str__(self):
        #return str(self.quantita)+"/"+ str(self.capacita)
        return f"{self.quantita}/{self.capacita}"
    
    def riempi(self,q):
        self.quantita += q
        if self.quantita > self.capacita:
            self.quantita = self.capacita
    def svuota(self,q):
        self.quantita -= q
        if self.quantita < 0:
            self.quantita = 0

class BottigliaConTappo(Bottiglia):
    def __init__(self, capacita):
        super().__init__(capacita)
        self.aperta = True
    def apri(self):
        self.aperta = True
    
    def chiudi(self):
        self.aperta = False
    
    def __str__(self):
        return super().__str__() + f" aperta: {self.aperta}"
    
    def riempi(self,q):
        if self.aperta:
            super().riempi(q)
    
    def svuota(self,q):
        if self.aperta:
            super().svuota(q)