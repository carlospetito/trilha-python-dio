limite = 500
limite_saque = 3
usuario = {}
numero_conta = 0

#cores
VERMELHO = '\033[91m'
VERDE = '\033[92m'
RESET = '\033[0m'  # Reseta a cor para a padrão do terminal

def menu():
    menu_texto = """
    ============Menu============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar Usuário
    [c] Criar Conta
    [q] Sair
    ============================
    => """
    return input(menu_texto).lower()

def deposito(saldo, extrato):
    valor = float(input("Digite o valor do deposito: "))
    if valor > 0:
        extrato += f"Deposito: R$ {VERDE}{valor:>10.2f}{RESET}\n"
        saldo += valor
        print(f"{VERDE}Depósito efeituado com sucesso!{RESET}")
    else:
        print(f"{VERMELHO}Operação falou! Valor inválido para depósito{RESET}")
    return saldo, extrato

def saque(saldo, extrato, numero_saque):
    valor = float(input("Digite o valor do saque: "))

    if valor > saldo:
        print(f"{VERMELHO}Operação falhou! Saldo insuficiente para saque{RESET}.")
    elif valor > limite:
        print(f"{VERMELHO}Operação falhou! Excedeu o limite de saque{RESET}")
    elif numero_saque > limite_saque:
        print(f"{VERMELHO}Operação falhou! Limite de saques do dia excedido.{RESET}")
    elif valor > 0:
        numero_saque += 1
        extrato += f"Saque:    R$ {VERMELHO}{valor:>10.2f}{RESET}\n"
        saldo -= valor
        print(f"{VERDE}Saque efeituado com sucesso!{RESET}")
    return saldo, extrato, numero_saque

def exibir_extrato(extrato, saldo):
    if extrato:
        print(f"=======Saldo da Conta=======\n{saldo}\nSaldo:    R$ {extrato:>10.2f}\n============================")
    else:
        print("Nenhuma movimentação registrada.")
    
def criar_usuario():
    nome = str(input("Digite o seu nome: "))
    nascimento = input("DIgite sua data de nascimento[dd/mm/aaa]: ")
    cpf = input("DIgite o CPF: ")
    endereco = input("Endereço[logradouro, numero - bairro - cidade/sigla estado]: ")
    if cpf in usuario:
        print(f"{VERMELHO}CPF já registrado. Usuário não adicionado{RESET}")
    else:
        usuario[cpf] ={
            "nome": nome, 
            "nascimento": nascimento, 
            "endereco": endereco
        }
        print(f"{VERDE}Usuário adicionado com sucesso!{RESET}")
        print(usuario)

    return usuario

def criar_conta(usuario):
    global numero_conta
    conta = {}
    cpf = input("Digite o CFP do usuário: ")

    if cpf not in usuario:
        print(f"{VERMELHO}CPF não encontrado. Por favor adicione o usuário primeiro.{RESET}")
    else:
        numero_conta += 1
        agencia = "0001"

        chave_conta = f"{agencia}-{numero_conta}"

        conta[chave_conta] = {
            "cpf_usuario": cpf, 
            "agencia": agencia, 
            "numero_conta": numero_conta
        }
        print(f"{VERDE}Conta {chave_conta} criada e vincualda ao CPF {cpf}.{RESET}")
    return conta

def main():
    saldo = 0.0
    numero_saque = 0
    extrato = ""
    nome = ""
    
    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = deposito(saldo, extrato)  

        elif opcao == "s":
            saldo, extrato, numero_saque = saque(saldo, extrato, numero_saque)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "u":
            nome = criar_usuario()

        elif opcao == "c":
            if nome:
                criar_conta(usuario)
            else:
                print(f"{VERMELHO}Primeiro crie um usuário.{RESET}")

        elif opcao == "q":
            print("Tenha um ótimo dia!")
            break
        else:
            print(f"{VERMELHO}Opção invalida! Por favor, selecione uma das opções disponíveis no menu.{RESET}")



main()
