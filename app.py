from os import lseek
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import random
import string
from bd.controllerBd import ControllerBd

app = Flask("app")

controllerBd = ControllerBd()
pergunta = -1
respostas = {}


@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/")
def home():
    global pergunta, respostas
    pergunta = -1
    respostas = {}
    return render_template("index.html", pergunta=getPergunta(),professores=getProfessores())

@app.route("/getPergunta")
def getPergunta():
    
    global pergunta, respostas
    try:
        if pergunta >= 0:
            respostas[str(pergunta)] = request.args.get('resposta')
        pergunta+=1
        with open('bd/perguntas.json','r+') as f:
            data = json.load(f)
            return data[str(pergunta)]
        
    except:
        return "PESQUISA FINALIZADA"


def salvaResultado(professor):
    print("to salvando resultado")
    global respostas
    respostas['professor']= professor
    with open('bd/escolas.json','r+') as f:
        data = json.load(f)
        data[controllerBd.getSessaoAtual()['escola']]['avaliacoes'].append(respostas)
        f.seek(0)
        json.dump(data,f,indent=4)
        f.truncate()
        

@app.route("/salvaRelato",methods=['POST'])
def salvaRelato():
    relato = request.json["content"]
    with open('bd/relatos.json','r+') as f:
        data = json.load(f)
        data[str(len(data.keys()))] = relato
        f.seek(0)
        json.dump(data,f,indent=4)
        f.truncate()

    return f"relato salvo,{relato}"

@app.route("/crudEscola")
def crudescola():
    return render_template("crudCriaEsola.html")

@app.route("/cadastraEscola", methods=["POST"])
def cadastraescola():
    if controllerBd.escolaExiste(request.json["escolaNome"]):
        id = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(0,8))
    
        with open("bd/escolas.json","r+") as f:
            data = json.load(f)
            data[request.json["escolaNome"]] = {
                'id':id,
                'senha':request.json["senha"]
                }
            f.seek(0)
            json.dump(data,f,indent=4)
            f.truncate()
                
        return f"{request.json['escolaNome']} cadastrada com sucesso"
    else:
        return "escola ja existe"

@app.route("/validaLogin", methods= ['POST'])
def validaLogin():
    user = request.json["usuario"]
    senha = request.json["senha"]

    with open('bd/escolas.json','r+') as f:
        data = json.load(f)
        if user in list(data.keys()):
            if senha == data[user]['senha']:
                return 'valido'
            else:
                return "senha invalida"
        else:
            return "escola nao existe"
            


def getProfessores():
    return controllerBd.getTodosProfessores(controllerBd.getSessaoAtual()['escola'])

@app.route("/resultadoFinal", methods=["POST"])
def resultadoFinal():
    salvaResultado(request.json['professor'])
    return "resultado salvo com sucesso"
app.run(host='0.0.0.0', debug=True)
