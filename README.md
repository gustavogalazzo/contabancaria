# CONTA BANCARIA - ATIVIDADE DE PROGRAMAÇÃO ORIENTADA A OBJETOS

# Proposta da Atividade 

Considere que uma agência bancária tem 5 clientes e cada cliente possui uma conta.
Cliente Saldo em Conta Corrente

Marcos | R$1.000,00
Julia | R$250,00
João | R$2.500,00
Roberto | R$3.000,00
Janaína | R$4.500,00

## Atividade

O objetivo é que você complemente as funcionalidades dessa aplicação fazendo as implementações a seguir:

1. Utilize como modelo a função interacao_sacar, e implemente o método interacao_depositar.
2. Desenvolva um método na classe ContaBancaria para efetuar a operação de transferência. O usuário
deve selecionar a conta de origem e a conta de destino. Não esqueça de verificar se as contas
informadas são válidas. Utilize a assinatura abaixo:

def transferir(self, valor, conta_destino):
###instruções do método a ser desenvolvido

Este método deverá transferir o valor especificado da conta da instância atual (cujos membros podem
ser acessados utilizando self) para a conta de destino (que pode ser acessada utilizando o parâmetro
conta_destino).

3. Utilize como modelo os métodos interacao_sacar e interacao_depositar e desenvolva o método
interacao_transferir, que deverá solicitar os dados necessários para a operação de transferência e
efetuá-la. Não esqueça de verificar se as contas informadas são válidas. Utilize a assinatura abaixo:

def interacao_transferir(contas):


4. Altere a classe ContaBancaria, para incluir um atributo privado __senha (string contendo 6 caracteres
numéricos entre 0 e 9). Esta senha deve ser definida no construtor e gerada automaticamente pela
classe, através do método criar_senha utilizando geradores aleatórios. Utilize a assinatura abaixo.
Para geradores aleatórios pode ser utilizado o módulo random.

def criar_senha(self):


5. Considere que foi criado um novo imposto que deve ser aplicado às operações bancárias. Para cada
saque realizado, deve-se descontar 0.25% do valor sacado do saldo restante do cliente. Os valores
descontados devem ser acumulados em um atributo privado __cpmf, que deve ser incluído na classe
ContaBancaria. O atributo __cpmf deve ser inicializado em zero.

7. Insira na classe ContaBancaria os métodos get_senha e get_cpmf.
