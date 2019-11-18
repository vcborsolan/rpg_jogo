import time
import random
from personagem import Personagem
from narrador import Narrador
from classificador import Classificador
from speech_recognizer import Ouvinte


narrador = Narrador()
cl = Classificador()
ouvinte = Ouvinte()

# ================================================================================
# ================================= JOGO =========================================

narrador.narrar('O jogo vai começar', 'init' , False)
t = narrador.narrar("Qual sua palavra chave?", "palavra chave" , False)
# while t != True :
#   sleep(0.1)
# teste = ouvir_microfone()
# if teste.lower() == "teste":
if input("Digite aqui teste: \n") == "teste":
  narrador.narrar("Logado com sucesso!","login_sucess" , False)
  personagem = Personagem("" , 0 , 0 , 0 ,0 ,0, 0 , 0 , 0 , 0 ,0 ,0)
  # ^^ aqui criar uma consulta de sql do personagem
  while True:
    if personagem.nome == "":
      narrador.narrar("Parece que ainda precisamos criar sua ficha antes de começar a jogar..." , "ficha_init" , False)
      narrador.narrar("Pegue um pedaço de papel para anotações , por mais que o mestre possa te lembrar de algum detalhe caso você pergunte , ele pode se cansar e ai já viu né" , "lembrete_anotacao" , False)
      while True:
        narrador.narrar("Me diga , qual o seu nome?" , "ficha_nome_input" , False)
        # listen = ouvir_microfone()
        listen = input("Digite seu nome: \n")
        narrador.narrar(f'Tem certeza que seu nome é {listen} ?' , f"ficha_nome_confirmation_{listen}" , True)
        # confirmation = ouvir_microfone()
        confirmation = input("sim ou não? \n")
        if confirmation.lower() == "sim":
          personagem.setNome(listen)
          break
        else:
          narrador.narrar("Vamos tentar novamente então " , "ficha_nome_again" , False)
      narrador.narrar("vamos prosseguir com o jogo então...","jogo_prosseguir" , False)
      narrador.narrar("Preste bem a atenção , agora sortearemos seis dados de seis lados , cada dado a um relacionado a um atributo entre eles , força , habilidade , resistência , armadura , poder de fogo e carisma" , "ficha_explain" , False)
      narrador.narrar("caso não goste da relação sorteada , não confirme quando solicitado , para gerarmos um novo sorteio" , "ficha_explain_rerol" , False)
      
      while True:
        dados = []
        for dice in range(1 , 7):
          dados.append(random.randint(1,6))

        narrador.narrar("Vou rolar os dados" ,"dices_alert" , False)
        narrador.rolar_dados()
        narrador.narrar(f"BVocê rolou . força {dados[0]} , habilidade {dados[1]} , resistência {dados[2]} , armadura {dados[3]} , poder de fogo {dados[4]} e carisma {dados[5]}" , "rolage_ficha" , True)
        
        confirmation = input("esta de acordo? \n")
        if confirmation.lower() == "sim":
          personagem.setForça(dados[0])
          personagem.setHabilidade(dados[1])
          personagem.setResistencia(dados[2])
          personagem.setArmadura(dados[3])
          personagem.setPdF(dados[4])
          personagem.setCarisma(dados[5])
          personagem.setPv(dados[2]*5)
          personagem.setPm(dados[2]*5)
          personagem.setDinheiro(random.randint(1,100))
          break
        else:
          dados.clear()
          narrador.narrar("Vamos tentar novamente então " , "ficha_nome_again" , False)
      for i in personagem.getFicha():
        print(f"{i} |  {personagem.getFicha()[i]}")
      narrador.repetir("jogo_prosseguir")
      narrador.narrar("Você tem alguma duvida quanto a sua ficha?" , "duvidas_ficha" , False)
      print(cl.classificar(input("Digite aqui sua duvida :\n"),personagem.getFicha()))

else:
  print("Deu errado")

