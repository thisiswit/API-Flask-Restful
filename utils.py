from models import Pessoas, Usuarios


def insere_pessoas():
    pessoas = Pessoas (nome = "Guedes", idade = 23)
    print(pessoas)
    pessoas.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome = "Wictor").first()
    # print(pessoa.nome)
    # print(pessoa.idade)


def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome = "Wictor").first()
    pessoa.idade = 10
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome = "Wictor").first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == "__main__":
    insere_usuario("Marcia", "2526")
    insere_usuario("Dela", "2728")
    consulta_todos_usuarios()
    # insere_pessoas()
    # alterar_pessoa()
    # exclui_pessoa()
    consulta_pessoas()