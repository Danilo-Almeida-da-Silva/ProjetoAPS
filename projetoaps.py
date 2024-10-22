def mostrar_operacoes(operacoes):
    for operacao in operacoes:
        tipo, acao, quantidade, preco = operacao
        valor_total = calcular_valor_total(tipo, quantidade, preco)
        print(f"{tipo.capitalize()} de {quantidade} ações da {acao} por ${preco} cada. Valor total de ações: ${valor_total:.2f}")

def calcular_valor_total(tipo, quantidade, preco):
    if tipo == 'compra' or tipo == 'venda':
        return quantidade * preco
    else:
        return 0

def validar_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Erro: Digite um número inteiro válido!!!.')

def validar_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Erro: Digite um valor decimal válido!!!.')

def validar_tipo_operacao():
    while True:
        tipo = input('Digite o tipo de operação desejada (compra/venda): ').strip().lower()
        if tipo in ['compra', 'venda']:
            return tipo
        else:
            print("Erro: Digite 'compra' ou 'venda'.")

def registrar_e_exibir_operações():
    operacoes = []
    valor_total_dia = 0
    while True:
        tipo = validar_tipo_operacao()
        acao = input('Digite o nome da ação que você quer/tem (ex: AAPL): ').upper()
        quantidade = validar_inteiro('Digite a quantidade de ações: ')
        preco = validar_float('Digite o preço unitário de cada ação: ')

        operacao = (tipo, acao, quantidade, preco)
        operacoes.append(operacao)
        valor_total_dia += calcular_valor_total(tipo, quantidade, preco)
        continuar = input('Deseja adicionar outra operação? (s/n): ').lower()
        if continuar != 's':
            break
    print('Operações realizadas no dia:')
    mostrar_operacoes(operacoes)
    print(f'Valor total de todas as operações: ${valor_total_dia:.2f}')

def main():
  while True:
    print('Menu de Operações')
    print('1. Iniciar o regrito de operações')
    print('2. Sair do programa.')

    opcao_menu = input('escolha opção 1 ou 2: ')

    if opcao_menu == '1':
      registrar_e_exibir_operações()
    elif opcao_menu == '2':
      print('Saindo do programa!...')
      print('Obrigado por utilizar o programa')
      break
    else:
      print('Erro: Opção invalida!, por favor digite opção 1 ou 2.')
main()