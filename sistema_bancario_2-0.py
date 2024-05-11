menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuario
[c] Criar conta
[q] Sair

=> """


LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []



def depositar(extrato, saldo):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return(extrato, saldo)
    else:
        print("Operação falhou! O valor informado é inválido.")
        return(extrato, saldo)
    

def sacar (extrato = extrato, saldo = saldo, numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES):
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return(extrato, saldo, numero_saques)

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            return(extrato, saldo, numero_saques)

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            return(extrato, saldo, numero_saques)

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            return(extrato, saldo, numero_saques)
        else:
            print("Operação falhou! O valor informado é inválido.")
            return(extrato, saldo, numero_saques)
        

def extratar(extrato, saldo = saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)  # noqa: E999
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return


def validar_usuario(cpf, usuarios):
    cpf = cpf
    usuarios = usuarios
    for usuarios in usuarios:
        if usuarios["cpf"] == cpf:
            return False
        else:
            return True


def mk_user():
    nome = input("digite o nome do usuario")
    data_de_nascimento = input("digite a data de nascimento (dd-mm-aaaa)")
    cpf = input("digite o cpf do usuario")
    endereço = input("digite o endereço do usuario (logradouro, numero - bairro - cidade/sigla estado)")

    if (nome & data_de_nascimento & cpf & endereço):
        user_valido = validar_usuario(cpf, usuarios)
        if user_valido:
            usuarios.append("nome": nome, data_nascimento)
        else:
            print("Usuario ja possue cadastro!")

    else:
        print("Usuário invalido, favor preencher todos os campos")


def mk_acc():


while True:

    opcao = input(menu)

    if opcao == "d":
       extrato,saldo = depositar(extrato,saldo)

    elif opcao == "s":
        extrato, saldo, numero_saques = sacar(extrato, saldo, numero_saques, LIMITE_SAQUES)

    elif opcao == "e":
        extratar(extrato, saldo)

    elif opcao == "u":
        mk_user(usuarios)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

