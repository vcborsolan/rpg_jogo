import speech_recognition as sr


class Ouvinte():

    def ouvir_microfone(self):
        #Habilita o microfone para ouvir o usuario
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            #Chama a funcao de reducao de ruido disponivel na speech_recognition
            microfone.adjust_for_ambient_noise(source)
        #Avisa ao usuario que esta pronto para ouvir
        # t = narrador.narrar("Aguardando o seu comando", "espera_comando")
        # while t != True :
        #   sleep(0.1)
            print("Aguardando o seu comando: ")
        #Armazena a informacao de audio na variavel
            audio = microfone.listen(source , timeout=None)
        try:
            #Passa o audio para o reconhecedor de padroes do speech_recognition
            frase = microfone.recognize_google(audio,language='pt-BR')
            #Após alguns segundos, retorna a frase falada
            print("Você disse: " + frase)
            #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
            return frase
        except sr.UnknownValueError:
            print("Não entendi")
            return False


# Ouvinte().ouvir_microfone()