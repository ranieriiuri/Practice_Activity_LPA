# <-------------------------- Atividade Prática - Lógica de Programação e Algoritmos ---------------------------->
"""
# Resposta da < Questão 1 >

#Prints iniciais com identificador pessoal
print('<--------------------- Loja do Iuri Ranieri! ---------------------->\n            A casa dos descontos que cabem no seu bolso!  ')
print('\nCalcule o preço final da sua compra abaixo! \n')

desconto = 0 #Definindo variável global para receber desconto definido nas condicionais a seguir

while True: #Laço para verificação de padrões definidos
    try: #Tentar executar entrada de dados dentro do padrão

        #Inserindo dados em números flutuantes do preço dos produtos e quantidade em números inteiros
        preco = float(input('Insira o preço deste produto:                  '))
        qnt = int(input('Insira a quantidade que estais comprando produto:  '))
        #Condicional para verificar se preço e quantidade de produtos estão dentro da condição de números positivos
        if (preco > 0) and (qnt > 0):
            # Definindo condicionais aninhadas para aplicar diferentes percentuais de desconto conforme quantidade de produtos(Exigência 1 de 1).
            if (qnt <= 9):
                 desconto = 0.00
                 break #Instrução para quebra do laço no caso de opção correta
            elif (qnt <= 99):
                desconto = 0.05
                break  # Instrução para quebra do laço no caso de opção correta
            elif (qnt <= 999):
                desconto = 0.10
                break #Instrução para quebra do laço no caso de opção correta
            else:
                desconto = 0.15
                break #Instrução para qubra do laço no caso de opção correta

        else: #Caso de valores inseridos nos inputs abaixo de 0
            print('\nDados inseridos não são passíveis de cálculo!\n')
    except ValueError:
        print('\nDados inválidos.\nInsira valores dentro do padrão definido!\n')
#Somando o total sem desconto
preco_sem_desconto = preco * qnt
#Operação de valor total da compra com desconto aplicado
preco_com_desconto = preco_sem_desconto - preco_sem_desconto * desconto
#Fazendo operação para pegar a porcentagem de desconto por unindade
desconto_por_unidade = desconto * 100

#Apresentando total sem desconto
print('\nO preço de {} unidade(s) deste produto sem desconto é R$ {:.2f}!'.format(qnt, preco_sem_desconto))
#Apresentando quantidade total de produtos escolhidos com o valor total com desconto aplicado e o percentual de desconto adquirido.
print('O preço total de {} unidade(s) deste produto com o percentual de desconto adquirido fica R$ {:.2f}!\nO desconto adquirido foi de {}% por unidade!'.format(qnt, preco_com_desconto, desconto_por_unidade))
print('<------------------------  ========  ------------------------------>')

# Resposta da < Questão 2 >

#Prints com apresentação da tabela de itens da lanchonete
print('<--------------------- Bem-vindo a Lanchonete do Iuri Ranieri! ---------------------->\n           "Venha se deliciar com nossas opções!" ')
print('\n-------------------------------------------------\n| Código |        Descrição        |  Valor R$  |\n-------------------------------------------------')
print('|  100   |     Cachorro-Quente     |    9,00    |\n|  101   | Cachorro-Quente duplo   |    11,00   |\n|  102   |          X-Egg          |    12,00   |\n|  103   |         X-Salada        |    13,00   |\n|  104   |         X-Bacon         |    14,00   |\n|  105   |          X-Tudo         |    17,00   |\n|  200   |    Refrigerante Lata    |    5,00    |\n|  201   |        Chá Gelado       |    4,00    |\n-------------------------------------------------')

#Definindo variáveis do código de cada item utilizando conjuntos para agregar dois valores: nome(string) e preço(number)
codigo100 = ['Cachorro-Quente', 9.00]
codigo101 = ['Cachorro-Quente duplo', 11.00]
codigo102 = ['X-Egg', 12.00]
codigo103 = ['X-Salada', 13.00]
codigo104 = ['X-Bacon', 14.00]
codigo105 = ['X-Tudo', 17.00]
codigo200 = ['Refrigerante Lata', 5.00]
codigo201 = ['Chá Gelado', 4.00]

valor_total = 0 #Variável para somar o total dos pedidos

while True: #Laço para fazer repetir pedidos e guardar dados
    pedido = (input('Insira o código do seu pedido:\n >> '))

    #Condicioais definindo códigos a serem aceitos no programa para acessar cada variável criada globalmente
    if pedido == '100':
        print('Você escolheu um {} de R${:.2f}.'.format(codigo100[0], codigo100[1])) #Acessando elementos das listas
        valor_total += codigo100[1] #Incrementando valor do item pego pelo índice da lista à variável 'valor_total', para somar após o laço
        #Repito o mesmo padrão nas condicionais abaixo
    elif pedido == '101':
        print('Você escolheu um {} de R${:.2f}\n'.format(codigo101[0], codigo101[1]))
        valor_total += codigo101[1]
    elif pedido == '102':
        print('Você escolheu um {} de R${:.2f}\n'.format(codigo102[0], codigo102[1]))
        valor_total += codigo102[1]
    elif pedido == '103':
        print('Você escolheu um {} de R${:.2f}\n'.format(codigo103[0], codigo103[1]))
        valor_total += codigo103[1]
    elif pedido == '104':
        print('Você escolheu um {} de R${:.2f}\n'.format(codigo104[0], codigo104[1]))
        valor_total += codigo104[1]
    elif pedido == '105':
        print('Você escolheu um {} de R${:.2f}\n'.format(codigo105[0], codigo105[1]))
        valor_total += codigo105[1]
    elif pedido == '200':
        print('Você escolheu um {} de R${:.2f}\n'.format(codigo200[0], codigo200[1]))
        valor_total += codigo200[1]
    elif pedido == '201':
        print('Você escolheu um {} de R$ {:.2f}\n'.format(codigo201[0], codigo201[1]))
        valor_total += codigo201[1]
    else: #Opção pra o caso do valor inserido ser diferente dos valores padrões definidos
        print('O dado inserido é inválido.\n'
              'Escolha pelo código correspondente ao item disponível no cardápio.\n')
        continue #Instrução para retornar à pergunta inicial do laço

    #Input para acrescentar itens ou fechar a conta
    pergunta = input('Quer pedir mais alguma coisa?\nDigite "1" para Sim ou "2" para Não.\n >> ')
    if pergunta == '1':
        continue #Instrução para voltar ao início do laço
    elif pergunta == '2':
        break #Instrução para quebrar o laço e ir ao próximo passo
    else:
        print('Resposta inválida.\nSiga o modelo abaixo para incluir mais itens ao pedido ou fechar a conta.\n')
        pergunta = input('Quer pedir mais alguma coisa?\nDigite "1" para Sim ou "2" para Não.\n >> ') #Chama novo input para decisão de adicionar itens ao pedido ou pedir a conta, no caso de dados inválidos inseridos

#Chamando variável 'valor_total' pra somar o total dos itens escolhidos no pedido e apresentar resultado ao usuário
print('O total a pagar é de R$ {:.2f}'.format(valor_total))

"""
# Resposta da < Questão 3 >

print('<--------------------- Iuri Ranieri Operações Logísticas S.A. --------------------->') #Identificador pessoal
def dimensoesObjeto(): #Função p/ definir limites de dimensões
    while True: #Laço p/ verificação
        try: #Tentar receber dados corretamente

            #Inputs p/ pegar dados em números inteiros
            alt = int(input('\nQuantos cm de altura seu objeto tem?\n>> '))
            larg = int(input('Quantos cm de largura seu objeto tem?\n>> '))
            comp = int(input('Quantos cm de comprimento seu objeto tem?\n>> '))
            calcVolume = alt * larg * comp #variável para calcular objeto em cm³

        except ValueError: #Tratamento no caso de valor inserido fora dos padrões numéricos definidos
            print('Valor fora do modelo foi identificado.\nInsira valores postitivos e inteiros em cm para calcularmos as dimensões e o preço exato referente a operação logística para seu objeto!')

        else: #Se não houverem erros, seguimos abaixopras condicionais de definições de limites
            if (calcVolume > 100000): #Caso exceda limite definido
                print('O total de {} cm³ excede nosso limite de dimensões de objetos para transporte!\nTente outro objeto.'.format(calcVolume))
                continue #Instrução que volta ao início do laço
            elif (calcVolume > 0) and (calcVolume < 1000): #Caso dimensões resultem entre 1 e 999 cm³
                print('O volume do objeto é de {} cm³.'.format(calcVolume))
                return 10.00 #variável retorna valor ao programa principal
            elif (calcVolume >= 1000) and (calcVolume < 10000): #Caso dimensões resultem entre 1000 e 9999 cm³
                print('O volume do objeto é de {} cm³.'.format(calcVolume))
                return 20.00 #retorna ao programa principal
            elif (calcVolume >= 10000) and (calcVolume < 30000): #Caso dimensões resultem entre 10000 e 29999 cm³
                print('O volume do objeto é de {} cm³.'.format(calcVolume))
                return 30.00 #retorna ao programa principal
            elif (calcVolume >= 30000) and (calcVolume < 100000): #Caso dimensões resultem entre 30000 e 99999 cm³
                print('O volume do objeto é de {} cm³.'.format(calcVolume))
                return 50.00 #retorna ao programa principal
            else:
                print('Valor não aceito. Insira valores entre 1 cm e 100000 cm para seguirmos com os cálculos referentes a sua operação logística!')
                continue #Instrução retornar ao início da função

def pesoObjeto(): #Define padrões e calcula se o peso do objeto se encaixa nos limites de transporte
    while True: #Laço p verificação
        try: #Tenta pegar os dados numéricos flutuantes sobre o peso do objeto
            peso = float(input('\nQuantos Kg pesa seu objeto?\n>> '))

        except ValueError: #Trata caso haja erro de valor inserido
            print('Valor fora do modelo foi identificado.\nInsira o peso entre 0.1 kg e 29.9 kg para conseguirmos calcular se o peso do seu objeto se encaixa em nossos limites logísticos!')

        else: #Se executar sem erros
            if (peso <= 0): #Define '0' ou abaixo como dado inexistente
                print('Este peso não existe. Insira um peso válido!')
                continue #Executa instrução de retornar ao início do laço
            elif (peso <= 0.1):
                return 1 #Caso 'peso' seja maior de 0 e menor ou igual a 0.1, retorna ao programa principal o multiplicador '1'
            elif (peso > 0.1) and (peso < 1):
                return 1.5 #Caso 'peso' seja maior de 0.1 e menor que 1, retorna ao programa principal o multiplicador '1,5'
            elif (peso >= 1) and (peso < 10):
                return 2 #Caso 'peso' seja maior ou igual a 1 e menor que 10, retorna ao programa principal o multiplicador '2'
            elif (peso >= 10) and (peso < 30):
                return 3 #Caso 'peso' seja maior ou igual a 10 e menor que 30, retorna ao programa principal o multiplicador '3'
            else:
                print('Este peso extrapola nossos limites para operação logística.\nTente novamente!')
                continue #Em caso de 'peso' extrapolar os limites definidos, usa a instrução 'continue' p retornar ao início do laço
def rotaObjeto(): #Função p definir e calcular rotas
    while True: #Laço para fazer as verificações necessárias

        rota = input('\nQual a sigla para rota de viagem do seu objeto?\n-----------------------------------------------\n| Sigla |                Rota                 |\n-----------------------------------------------\n|  MS   |   Maceió - S.Miguel dos Milagres    |\n|  MP   |          Maceió - Penedo            |\n|  PS   |   Penedo - S.Miguel dos Milagres    |\n-----------------------------------------------\n>> ') #Apresenta informações sobre rotas e sua respectivas siglas
        rota = rota.upper() #Método para aceitar o input de 'rota' em maiúsculo, caso seja digitado minúsculo
        if (rota != 'MS') and (rota != 'MP') and (rota != 'PS'): #condicional que define como inválido se o usuário inserir algum dado fora das 3 siglas definidas pras rotas usadas pelo programa
            print('Dado inválido. Escolha entre as siglas das 3 rotas disponíveis para finalizar o cálculo!')
        elif (rota == 'MS'):
            return 1 #Neste caso, a instrução retona 'rota' com o multiplicador '1' ao programa principal
        elif (rota == 'MP'):
            return 1.2 #Neste caso, a instrução retona 'rota' com o multiplicador '1.2' ao programa principal
        else:
            return 1.5 #Sobra apenas a rota 'PS', definida anteriormente, neste caso, a instrução retona 'rota' com o multiplicador '1.5' ao programa principal

#Definindo variáveis para chamar as funções criadas acima ao programa principal
resultadoVolume = dimensoesObjeto()
resultadoPeso = pesoObjeto()
resultadoRota = rotaObjeto()

totalGeral = resultadoVolume * resultadoPeso * resultadoRota #Faz o cálculo final do total a ser pago, baseado nos valores colhidos pelas funções

print('Preço por volume do objeto: R$ {:.2f}, multiplicado por {} (pela tabela de peso do objeto), multiplado por {} (pela rota escolhida)\n >> O total a pagar por esta operação logística será de R$ {:.2f}. <<'.format(resultadoVolume, resultadoPeso, resultadoRota, totalGeral)) #Apresenta ao usuário o resumo de fórmula usada e o valor total a ser pago pela operação logística

"""
#Respota da questão 4
print('\n|--------------------> \U0001f6b2   Bem-vindo de volta à Bicicletaria IRB  \U0001f6b2  <--------------------|\n                        Grupo Iuri Ranieri Batista de Operações Ltda.\n ')

#Definindo variável globais 'pecas' como lista vazia e 'codigo' para contagem das peças a partir do código 100
pecas = []
codigo = 99

#Criando 3 funções usadas no programa
def cadastrarPeca(codigo):
    #Laço principal da função
    while True:
        #Tratamento de erro principal da função
        try:
            print('|-------------------------------|  Menu de Cadastro de Peças |------------------------------|')
            #Inserindo uma pergunta principal da função, levando em conta que é uma função de cadastro e teoricamente precisaria voltar ao ínicio várias vezes
            cadastrar = input('\nContinuar cadastro de peças no sistema?\n  (S) - p/ seguir cadastro\n  (N) - p/ retornar ao Menu Principal\n >> ')
            #condicionais abaixo definem as opções 'N' para voltar ao Menu principal ou 'S' para acessar as perguntas do menu de cadastro
            if cadastrar.upper() == 'N':
                break #Sair do laço
            elif cadastrar.upper() == 'S':
                #inputs de cadastro. 2 de Strings e uma de números flutuantes (p/ receber os preços das peças)
                nome = input('Informe o nome da peça que será cadastrada:\n >> ')
                fabricante = input('Qual o fabricante desta peça?\n >> ')
                valor = float(input('Qual o preço (em R$) desta peça?\n >> '))
            else:
                #Definindo a opção de tipo de dado string, mas que não seja 'S' ou 'N'
                print('Dado inválido. Siga o modelo proposto!\n')
                continue #Caso aconteça, retorna para a pergunta principal

        #Definindo tratamento para caso de tipo de dado inserido errado
        except ValueError:
            print('Dado inserido não é válido.\nInsira dados válidos para cada campo respectivamente!\n')
        #Caso os dados inseridos não caiam nos erros definidos anteriormente
        else:
            codigo += 1 #Acrescentar + 1 a variável global código em cada peça cadastrada
            dic = {'Codigo': codigo, 'Nome': nome, 'Fabricante': fabricante, 'Valor': valor} #Criando dicionário e definindo o código incrementado acima e os inputs nome, fabricante e valor às chaves(de mesmo nome, p/ facilitar)
            pecas.append(dic.copy()) #Copiando dicionário 'dic' pra dentro da lista vazia 'peças'(definida no início)
            print('O código da peça será: {}\n'.format(codigo)) #Print que será apresentado após a criação de cada peça

def consultarPeca(codigo):
    #Laço principal
    while True:
        #Tratamento de erro
        try:
            consultar = int(input('|----------------------------------|  Menu de Consulta de Peças |----------------------------------|\nEscolha entre 0 e 3 para realizar uma de nossas operações de consulta ou retornar ao Menu Principal:\n  0- Retornar ao Menu Principal\n  1- Consultar todas as peças disponíveis\n  2- Consultar peça individualmente pelo código\n  3- Consultar peça por fabricante\n >> ')) #Input inicial da função defininido em 'int'

            if consultar == 0:
                break # '0' como saída p/ Menu principal
            elif consultar == 1:
                #Condicional aninhada p/ definir instrução p/ o caso de usuário querer acessar consulta antes de ter produtos cadastrados
                if len(pecas) == 0:
                    print('Nosso cadastro está vazio.\nAcesse o Menu de Cadastro de Peças p/ cadastrar antes de consultar!\n')
                else: #Se cadastro não estiver vazio
                    print('Lista das peças cadastradas em nosso sistema:\n')
                    for peca in pecas: #Laço p/ acessar items dentro da lista 'peças'
                        print('<', '-' * 96, '>') #Visual de como o resultado será apresentado, caso os dados inseridos entre na opção em questão
                        for chave, valor in peca.items(): #Laço aninhado pra pegar cada chave e valor dos itens dentro de 'peças'
                            print('{} : {}'.format(chave, valor))
                        print('<', '-' * 96, '>')
            elif consultar == 2:
                if len(pecas) == 0: #uso o mesmo padrão que usei acima p/ verificar se tem itens cadastrados
                    print('Nosso cadastro está vazio.\nAcesse o Menu de Cadastro de Peças p/ cadastrar antes de consultar!\n')
                else:
                    consultaPorCodigo = int(input('Insira o código da peça para consultar informações referentes à ela:\n >> ')) #
                    for peca in pecas: #Uso o mesmo padrão da opção de apresentar a lista completa dos itens cadastrados
                        if peca['Codigo'] == consultaPorCodigo: #Utilizando o índice do dicionário para verificar se o código condiz com o input 'consultaPorCodigo'
                            print('Informações da peça buscada:\n')
                            print('<', '-' * 96, '>')
                            for chave, valor in peca.items(): #Mesmo padrão de acesso e apresentação dos itens utilizando laço 'for in', só que agora relacionados ao código definido no cadastro
                                print('{} : {}'.format(chave, valor))
                            print('<', '-' * 96, '>')
            elif consultar == 3: #Defini a opção '3' p/ consulta por 'Fabricante'
                if len(pecas) == 0: #Mesmo padrão de verificação se tem itens cadastrados antes da consulta
                    print('Nosso cadastro está vazio.\nAcesse o Menu de Cadastro de Peças p/ cadastrar antes de consultar!\n')
                else:
                    consultarPorFabricante = input('Insira o nome do Fabricante para consultar quais peças fabricadas por ele temos cadastradas no sistema:\n >> ')
                    for peca in pecas: #Utilizando o mesmo padrão de laço p/ acessar elementos no dicionário
                        if peca['Fabricante'] == consultarPorFabricante: #Condicional p/ verificar por chave 'Fabricante'
                            print('Pecas do Fabricante {}:\n'.format(consultarPorFabricante))
                            print('<', '-' * 96, '>') #Padrão visual de apresentação
                            for chave, valor in peca.items(): #Laço p/ pegar itens do elemento acessado por chave 'Fabricante'
                                print('{} : {}'.format(chave, valor))
                            print('<', '-' * 96, '>')
            else:
                print('Escolha uma opção válida entre 0 e 3!') #Opção de mensagem no caso do usuário inserir número inteiro diferente de 0 a 3

        except ValueError: #Tratamento de erro para valor diferente do input int principal da função
            print('Dado inserido não é válido.\nTente novamente!')
def removerPeca(codigo):
    while True: #Laço principal da função
        try: #Tentativa de execução da função
            remover = int(input('|-----------------------------------|  Menu de Remoção de Peças |---------------------------------|\nEscolha entre 0 e 2 para realizar uma de nossas operações de remoção ou retornar ao Menu Principal:\n0- Retornar ao Menu Principal\n1- Remover peça por código\n2- Remover todas as peças\n >> '))
            if remover == 0:
                break #Instrução que sai do laço no caso da opção '0'
            elif remover == 1:
                if len(pecas) == 0: #Verificação pro caso do usuário acessar a função 'removerPeca' antes do cadastro de peças
                    print('Nosso cadastro está vazio.\nAcesse o Menu de Cadastro de Peças p/ cadastrar antes de remover!\n')
                else:
                    while True: #Laço para o caso do usuário querer retornar ao menu anterior com '0' ou remover elemento por código
                        removerPorCodigo = int(input('Insira o código da peça a ser removida ou pressione "0" para retornar:\n >> '))
                        if removerPorCodigo == 0:
                            break #Instrução p/ qubrar laço e retornar ao laço principal da função
                        else:
                            for peca in pecas: #Laço p/ acessar elementos dentro da lista 'peças'
                                if peca['Codigo'] == removerPorCodigo: #Condicional pra verificar se o código inserido no início do laço existe dentro de 'peças'
                                    pecas.remove(peca) #Instrução pra remover o item do código em questão
                                    print('Peça referente ao código {} foi removida com sucesso!\n'.format(removerPorCodigo)) #Msg de confirmação da remoção
                                    break #Instrução pra sair do laço no caso da remoção do elemento ter sido concluída

            elif remover == 2: #Opção de remover todos os dados cadastrados
                if len(pecas) == 0: #Verificação no mesmo padrão utilizado nas condicionais acima, p/ o caso do usuário acessar função 'removerPeca' antes de ter itens cadastrados
                    print(
                        'Nosso cadastro está vazio.\nAcesse o Menu de Cadastro de Peças p/ cadastrar antes de remover!\n')
                else: #Se já houver itens cadastrados
                    while True: #Laço pra avisar que o usuário está prestes a apagar todos as peças cadastradas no sistema
                        verificacaoSeguranca = input('* Essa opção limpará todos os dados cadastrados no sistema!\nTem certeza disso?\n(S) - p/ Limpar todos os dados das peças cadastradas no sistema\n(N) - p/ Retornar ao Menu de Remoção de Peças\n >> ')
                        if verificacaoSeguranca.upper() == 'S': #Se 'S'(maiúsculo ou minúsculo)
                            pecas.clear() #Apagar todos os elementos cadastrados
                            break #Sair do laço de verificação
                        elif verificacaoSeguranca.upper() == 'N': #Se 'N'(maiúsculo ou minúsculo)
                            break #Sair do laço de verificação sem apagar
                        else: #Se dados inseridos no input 'verficacaoDeSeguranca' fugir de 'S','s', 'N' ou 'n', repete início do laço de verificação
                            print('Dados inseridos são inválidos. Siga os padrões de "S" p/ SIM ou "N" p/ NÃO!\n')
        except ValueError: #Tratamento de erro de tipo de dados inseridos, neste caso, retorna input 'remover' no início do laço
            print('Dados inválidos. Siga o padrão proposto!')

#Programa principal
while True: #Laço pra criação do Menu Principal do programa
    try: #Tentativa de execução do Input 'int' principal
        print('|--------------------> Menu Principal de Operações da Bicicletaria IRB <--------------------|\n')
        perguntaInicial = int(input('Escolha entre 0 e 3 para acessar algum dos menus de operação disponíveis ou sair do sistema:\n  0- Sair\n  1- Menu de Cadastro de Peças\n  2- Menu de Consulta de Peças\n  3- Menu de Remoção de Peças\n >> '))
        if perguntaInicial == 0: #Opção de sair do programa
            print('Finalizando operações do sistema...\nTenha um ótimo dia!')
            break #Instrução p/ sair do laço
        elif perguntaInicial == 1: #Caso de escolher função de cadastro das peças
            cadastrarPeca(codigo) #Instrução p/ chamar função
        elif perguntaInicial == 2: #Caso de escolher função de consulta de peças
            consultarPeca(codigo) #Instrução p/ chamar função
        elif perguntaInicial == 3:#Caso de escolher função de remoção de peças
            removerPeca(codigo) #Instrução p/ chamar função
        else: #Caso seja escolhido um número fora de 0 a 3
            print('Essa opção não existe em nosso Menu!\nEscolha dentre as opções do Menu Principal.')

    except ValueError: #Tratamento de erro pra o caso de dado inserido fora do padrão de tipo definido
        print('Dado inválido.\nSiga o nosso modelo padrão, escolha entre 0 e 3!')

    finally: #Instruções que executam independente dos resultados do Menu Principal
        #variável 'slogan' para definir slogan da bicicletaria e acessá-lo de forma mais fácil
        slogan = '          Bicicletaria IRB - A casa da segurança e qualidade que você merece!            '
        tam = len(slogan) #Pegando tamanho total do slogan pra facilitar a formatação visual
        #Abaixo, prints de formatação visual do slogan
        print('\n\n\n<', '-' * tam, '>')
        print('<', slogan, '>')
        print('<', '-' * tam, '>\n')
"""