import json

class ControllerBd:
    def __init__(self):
        print("controller banco iniciado")

    def escolaExiste(self, nome):
        with open("bd/escolas.json", "r+") as f:
            data = json.load(f)
            if nome in data.keys():
                return False
            else:
                return True
        
    def getTodosProfessores(self, escola):
        with open('bd/escolas.json','r+') as f:
            data = json.load(f)
            return data[escola]['professores']


    def getSessaoAtual(self):
        with open('bd/secaoAutal.json','r+') as f:
            data = json.load(f)
            return data



#ControllerBd().getSessaoAtual()
