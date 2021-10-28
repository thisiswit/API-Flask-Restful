from models import Pessoas


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


if __name__ == "__main__":
    insere_pessoas()
    # alterar_pessoa()
    # exclui_pessoa()
    consulta_pessoas()