from gtts import gTTS
import os
import time
from pygame import mixer
from tinytag import TinyTag
from os.path import dirname,realpath,isfile


class Narrador:

    def __init__(self):
        self.path = dirname(realpath(__file__))+'/mp3/'

    # @staticmethod
    def narrar(self , texto , filename , excluir):

        if not isfile(self.path + filename + ".mp3"):
            output = gTTS(text=texto , lang='pt-br' , slow=False )
            output.save(f'mp3/{filename}.mp3')
            # print("teve que criar")

        tag = TinyTag.get(f'mp3/{filename}.mp3')

        time.sleep(1)
        mixer.init()
        mixer.music.load(f'mp3/{filename}.mp3')
        mixer.music.play()
        time.sleep(tag.duration+1)

        if excluir:
            os.remove(self.path + filename + ".mp3")
        return True

    def rolar_dados(self):
        tag = TinyTag.get('assets/rolar_dados.mp3')
        mixer.init()
        mixer.music.load('assets/rolar_dados.mp3')
        mixer.music.play()
        time.sleep(tag.duration+1)
        return True

    def repetir(self , filename):
        tag = TinyTag.get(f'mp3/{filename}.mp3')
        time.sleep(1)
        mixer.init()
        mixer.music.load(f'mp3/{filename}.mp3')
        mixer.music.play()
        time.sleep(tag.duration+1)
        return True


# print(Narrador().narrar("teste" , "teste1"))