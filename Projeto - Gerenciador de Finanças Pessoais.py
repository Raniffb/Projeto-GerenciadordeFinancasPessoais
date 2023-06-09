//Projeto: Gerenciador de Finanças Pessoais

//Descrição: Um aplicativo de linha de comando que permite ao usuário gerenciar suas finanças pessoais. O usuário pode adicionar transações, categorizar as transações, calcular o saldo atual e gerar relatórios de gastos.

//Passos para o projeto:

//Criar uma interface de linha de comando que exibe um menu com as opções disponíveis para o usuário.
//Implementar a lógica para adicionar uma nova transação com informações como valor, categoria e data.
//Implementar a lógica para categorizar as transações em categorias predefinidas (por exemplo, alimentação, transporte, lazer, etc.).
//Implementar a lógica para calcular o saldo atual com base nas transações adicionadas.
//Implementar a lógica para gerar relatórios de gastos, mostrando o total gasto em cada categoria.
//Armazenar as transações em um arquivo para que elas possam ser recuperadas em sessões futuras.

//Aqui está um exemplo de código Python para este projeto:


import json
from datetime import datetime

def adicionar_transacao(transacoes):
    descricao = input("Digite a descrição da transação: ")
    valor = float(input("Digite o valor da transação: "))
    categoria = input("Digite a categoria da transação: ")
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transacao = {"descricao": descricao, "valor": valor, "categoria": categoria, "data": data}
    transacoes.append(transacao)
    print("Transação adicionada com sucesso!")

def calcular_saldo(transacoes):
    saldo = 0

    for transacao in transacoes:
        saldo += transacao["valor"]

    return saldo

def gerar_relatorio_gastos(transacoes):
    relatorio = {}

    for transacao in transacoes:
        categoria = transacao["categoria"]
        valor = transacao["valor"]

        if categoria in relatorio:
            relatorio[categoria] += valor
        else:
            relatorio[categoria] = valor

    print("Relatório de Gastos:")
    for categoria, valor in relatorio.items():
        print(f"{categoria}: R$ {valor:.2f}")

def salvar_transacoes(transacoes):
    with open("transacoes.json", "w") as arquivo:
        json.dump(transacoes, arquivo)

def carregar_transacoes():
    try:
        with open("transacoes.json", "r") as arquivo:
            transacoes = json.load(arquivo)
    except FileNotFoundError:
        transacoes = []
    return transacoes

def exibir_menu():
    print("Gerenciador de Finanças Pessoais")
    print("Selecione a opção:")
    print("1. Adicionar transação")
    print("2. Calcular saldo atual")
    print("3. Gerar relatório de gastos")
    print("4. Sair")

def main():
    transacoes = carregar_transacoes()

    while True:
        exibir_menu()
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            adicionar_transacao(transacoes)
        elif opcao == 2:
            saldo = calcular_saldo(transacoes)
            print("Saldo atual: R$ {:.2f}".format(saldo))
        elif opcao == 3:
            gerar_relatorio_gastos(transacoes)
        elif opcao == 4:
            salvar_transacoes(transacoes)
            print("Transações salvas. Encerrando programa.")
            break
        else:
            print("Opção inválida. Digite um número válido.")
if __name__ == "__main__":
    main()
