from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from narrador import Narrador


train = [
    ('por favor mestre tenho duvidas sobre sobre força','duvida_for'),
    ('por favor mestre tenho duvidas sobre habilidade' , 'duvida_hab'),
    ('por favor mestre poderia repetir minha ficha','repetir_ficha'),
    ("por favor mestre tenho duvidas sobre minha armadura" , 'duvida_arm'),
    ('por favor mestre tenho duvidas sobre minha resistência' , 'duvida_res'),
    ('por favor mestre tenho duvidas sobre meu carisma' , 'duvida_carisma'),
    ('por favor mestre tenho duvidas sobre meus pontos de vida' , 'duvida_pv'),
    ('por favor mestre tenho duvidas sobre meus pontos de magia' , 'duvida_pm'),
    ('por favor mestre tenho duvidas sobre meu poder de fogo' , 'duvida_pdf'),
    ('por favor mestre tenho duvidas sobre meu dinheiro' , 'duvida_din')
]

class Classificador():
    def __init__(self):

        self.cl = NaiveBayesClassifier(train)
        self.narrador = Narrador()

    def interact_narrador(self , classficacao , ficha):
        return {
            'duvida_for' : lambda ficha: self.narrador.narrar(f"Sua força é igual a {ficha['força']} pontos" , 'duvida_for' , True) ,
            'duvida_hab' : lambda ficha: self.narrador.narrar(f"Sua habilidade é igual a {ficha['habilidade']} pontos" , 'duvida_hab' , True),
            'duvida_arm' : lambda ficha: self.narrador.narrar(f"Sua armadura é igual a {ficha['armadura']} pontos" , 'duvida_arm' , True),
            'duvida_res' : lambda ficha: self.narrador.narrar(f"Sua resistência é igual a {ficha['resistencia']} pontos" , 'duvida_res' , True),
            'duvida_carisma' : lambda ficha: self.narrador.narrar(f"Seu carisma é igual a {ficha['carisma']} pontos" , 'duvida_car' , True),
            'duvida_pv' : lambda ficha: self.narrador.narrar(f"Seus pontos de vidão são iguais a {ficha['pv']} pontos" , 'duvida_for' , True),
            'duvida_pm' : lambda ficha: self.narrador.narrar(f"Seus pontos de magia são iguais a {ficha['pm']} pontos" , 'duvida_pm' , True),
            'duvida_pdf' : lambda ficha: self.narrador.narrar(f"Seu poder de fogo é igual a {ficha['pdf']} pontos" , 'duvida_pdf' , True),
            'duvida_din' : lambda ficha: self.narrador.narrar(f"Você carrega consigo {ficha['dinheiro']} moedas" , 'duvida_din' , True)
        }.get(classficacao)(ficha)
    
    def classificar(self , texto ,ficha):

        classificacao = self.cl.classify(texto)
        # prob_dist=self.cl.prob_classify(texto)
        # self.cl.show_informative_features(5)
        # print(prob_dist.max())
        # print(round(prob_dist.prob("duvida_for"),2))
        # print(classificacao)

        self.interact_narrador(classificacao, ficha)

        return True



# ficha = {'nome': 'Victor', 'força': 1, 'habilidade': 5, 'resistencia': 1, 'armadura': 5, 'pv': 5, 'pm': 5, 'pe': 0, 'dinheiro': 56, 'pdf': 5, 'carisma': 2}
# Classificador().classificar("Tenho duvidas sobre força" , ficha )