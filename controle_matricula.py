from flask import Flask, render_template, request, redirect

from objetos.alunos import Aluno

app = Flask(__name__)

alunos = []
alunos.append(Aluno("1","Fernando", "Python Flask", "Vespertino"))
alunos.append(Aluno("2","Julio", "Python Avançado", "Noturno"))
alunos.append(Aluno("3","Beatriz", "Python Flask", "Vespertino"))
alunos.append(Aluno("4","Carla", "Python Flask", "Vespertino"))

def get_base_context():
    return {
        "titulo": "Alunos matriculados",
        "lista_alunos": alunos,
    }

@app.route('/')
def index():
    

    context = get_base_context()

    return render_template("index.html", context=context)

@app.route("/cadastro")
def cadastro():

    context = get_base_context()

    return render_template("cadastro.html", context=context)

@app.route("/add", methods=["POST"])
def criar_novo_aluno():

    id = len(alunos) + 1
    nome = request.form["nome"]
    curso = request.form["curso"]
    horario = request.form["horario"]
    aluno = Aluno(
        id=id,
        nome=nome,
        curso=curso,
        horario=horario)

    alunos.append(aluno)

    return redirect("/")

@app.route("/detalhes")
def detalhes():
    user_id = request.args.get('id', default=0, type=int)
    context = get_base_context()

    for aluno in alunos:
        if int(aluno.id) == user_id:
            context['aluno'] = aluno
            return render_template("detalhes.html", context=context)


    return redirect("/")


    
app.run().
