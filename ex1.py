class ContaBancaria:
    def __init__(self, correntista, saldo):
        self.__correntista = correntista
        self.__saldo = saldo
    def depositar(self, valor):
        self.__saldo += valor
    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta_destino):
    # instruções do método a ser desenvolvido
        pass
    def criar_senha(self):
    # instruções do método a ser desenvolvido
        pass
    def get_saldo(self):
        return self.__saldo
    def exibir_info(self):
        return f"Conta de {self.__correntista} - Saldo de R$ {self.__saldo:.2f}"

def mostrar_info(contas):
    print("\nContas de todos os clientes:")
    for i in range(len(contas)):
        print(f"[{i}] {contas[i].exibir_info()}")

def interacao_sacar(contas):
    cliente_valido = False
    while not cliente_valido:
        mostrar_info(contas)
        indice_conta = int(input(f"O saque será efetuado na conta de qual cliente?
(0 a {len(contas) - 1}): "))
        
        if indice_conta >= 0 and indice_conta < len(contas):
            cliente_valido = True
        else:
            print("Índice de cliente inválido!")
    saque = float(input("Qual o valor do saque? "))
    contas[indice_conta].sacar(saque)
    print("Saque finalizado.")

def interacao_depositar(contas):
# instruções do método a ser desenvolvido
    pass
def interacao_transferir(contas):
# instruções do método a ser desenvolvido
    pass
# PROGRAMA PRINCIPAL
contas = [
    ContaBancaria( "Marcos", 1000.00),
    ContaBancaria("Júlia", 250.00),
    ContaBancaria("João", 2500.00),
    ContaBancaria("Roberto", 3000.00),
    ContaBancaria("Janaína", 4500.00)]
while True:
    print("Escolha uma operação:")
    print("(1) mostrar informações de todas as contas")
    print("(2) sacar")
    print("(3) depositar")
    print("(4) transferir")
    print("(5) sair")
    escolha = int(input("Opção escolhida: "))
    match escolha:
        case 1:
            mostrar_info(contas)
        case 2:
            interacao_sacar(contas)
        case 3:
            interacao_depositar(contas)
        case 4:
            interacao_transferir(contas)
        case 5:
            print("Fim do programa!")
            break
        case _:
            print("Opção inválida!")
    print()