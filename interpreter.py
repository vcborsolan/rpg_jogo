import json
from json_manager import JsonManager 


class Interpreter:

        def interpretar(texto):
                jmanager = JsonManager()
                comandos_explicitos = jmanager.read_json('comandos.json')['comandos']
                for comando in comandos_explicitos:
                        if texto in comandos_explicitos[comando]:
                                print(comando)
                                return comando


Interpreter.interpretar(input("Digite o comando: \n").lower())