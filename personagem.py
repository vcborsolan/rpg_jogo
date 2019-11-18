class Personagem:

    def __init__(self , nome , força , habilidade , resistencia , armadura , pf , pv , pm , pe , dinheiro , carisma , pdf):    
        self.nome = nome    
        self.força = força  
        self.habilidade = habilidade 
        self.resistencia = resistencia 
        self.armadura = armadura 
        self.pf = pf   
        self.pv = pv 
        self.pm = pm 
        self.pe = pe
        self.dinheiro = dinheiro
        self.carisma = carisma
        self.poderdefogo = pdf
        
    def setNome(self , nome):
        self.nome = nome

    def setCarisma(self, carisma):
        self.carisma = carisma

    def setForça(self , força):
        self.força = força

    def setDinheiro(self , dinheiro):
        self.dinheiro = dinheiro
    
    def setHabilidade(self , habilidade):
        self.habilidade = habilidade

    def setResistencia(self , resistencia):
        self.resistencia = resistencia

    def setArmadura(self , armadura):
        self.armadura = armadura

    def setPdF(self , pdf):
        self.poderdefogo = pdf

    def setPf(self , pf):
        self.pf = pf

    def setPv(self , pv):
        self.pv = pv

    def setPm(self , pm):
        self.pm = pm

    def setPe(self , pe):
        self.pe = pe

    def getnome(self):
        return self.nome

    def getDinheiro(self):
        return self.dinheiro

    def getForça(self):
        return self.força
    
    def getHabilidade(self):
        return self.habilidade

    def getResistencia(self):
        return self.resistencia

    def getArmadura(self):
        return self.armadura

    def getPf(self):
        return self.pf

    def getPv(self):
        return self.pv

    def getPm(self):
        return self.pm

    def getPdF(self):
        return self.poderdefogo

    def getPe(self):
        return self.pe
    
    def getCarisma(self):
        return self.carisma

    def getFicha(self):
        return {
            "nome": self.nome,
            "força": self.força,
            "habilidade": self.habilidade,
            "resitencia": self.resistencia,
            "armadura": self.armadura,
            "pv": self.pv,
            "pm": self.pm,
            "pe": self.pe,
            "dinheiro": self.dinheiro,
            "pdf": self.poderdefogo,
            "carisma": self.carisma
        }