from personagem import Personagem
import random


personagem = Personagem("Victor" , 0 , 0 , 0 ,0 ,0, 0 , 0 , 0 , 0 ,0 ,0)
dados = []
for dice in range(1 , 7):
  dados.append(random.randint(1,6))
personagem.setForça(dados[0])
personagem.setHabilidade(dados[1])
personagem.setResistencia(dados[2])
personagem.setArmadura(dados[3])
personagem.setPdF(dados[4])
personagem.setCarisma(dados[5])
personagem.setPv(dados[2]*5)
personagem.setPm(dados[2]*5)
personagem.setDinheiro(random.randint(1,100))

print(personagem.getFicha())
