#projeto de teste
'''O usuario deverar se registra preenchendo os campos
*nome
*sobrenome
*data de nascimento
*coletar data de criação de cadasrto
*senha e confirmação de senha, opção de gerar senha aleatoria
verificar funcionalidades de senha
'''
# Importações
from datetime import datetime
# variaveis
cores = {"limpar": '\033[m', "vermelho": '\033[31m',
         "verde": '\033[32m', "amarelo": '\033[33m', "roxo": '\033[34m', "rosa": '\033[35m', "azul": '\033[36m',
         }

novo_cadastro = ''
dados_de_cadastro_do_usuario = {}

# dados do usuario


def corte_tela():
    print(20*f'{cores["amarelo"]}--{cores["limpar"]}')


def dados_de_cadastro_novo_usuario():
    def nome_usuario():
        nome = str(
            input(f'{cores["verde"]}Escreva seu nome: {cores["limpar"]}')).strip().capitalize()
        dados_de_cadastro_do_usuario['nome'] = nome

    def sobrenome_usuario():
        sobrenome = str(input(
            f'{cores["verde"]}Escreva seu sobrenome: {cores["limpar"]}')).strip().capitalize()
        dados_de_cadastro_do_usuario['sobrenome'] = sobrenome

    def data_nascimento_usuario():
        data_nascimento = datetime.strptime(
            input(f'{cores["verde"]}Escreva sua data de nascimento:{cores["amarelo"]} dia/mes/ano {cores["limpar"]}'), ('%d/%m/%Y'))
        dados_de_cadastro_do_usuario['data nascimento'] = data_nascimento.strftime(
            '%d/%m/%Y')

    def data_cadastro_usuario():
        dados_de_cadastro_do_usuario['data_cadastro'] = datetime.now().strftime(
            '%d/%m/%Y')

    def criar_senha_usuario():

        def senha_aleatoria():
            senha = {}
            from random import randint
            caracteres = '1324568907AbCDEFGHIJKLMNOP!QRSTUVXZYWaB$cdefghijklmnop#qrstuvxzwy@%*=+_?'
            # defini que a senha tera 8 digitos
            for caracter_senha in range(9):
                senha_aleatoria_1 = caracteres[randint(0, 68)]
                senha[f'senha_usuario{caracter_senha}'] = senha_aleatoria_1
            juncao_senha = senha[f'senha_usuario0']+senha[f'senha_usuario1']+senha[f'senha_usuario2']+senha[
                f'senha_usuario3']+senha[f'senha_usuario4']+senha[f'senha_usuario5']+senha[f'senha_usuario6']+senha[f'senha_usuario7']
            dados_de_cadastro_do_usuario['senha usuario'] = juncao_senha
            print(
                f"{cores['azul']}Sua nova senha é: {dados_de_cadastro_do_usuario['senha usuario']}{cores['limpar']}")

        senha_manual = str(
            input(f'{cores["verde"]}Crie sua senha:{cores["amarelo"]} Ou Digite [A] para senha aleatoria. {cores["limpar"]}'))
        if senha_manual == 'A' or senha_manual == 'a':
            senha_aleatoria()
        else:
            dados_de_cadastro_do_usuario['senha usuario'] = senha_manual

    nome_usuario()
    sobrenome_usuario()
    data_nascimento_usuario()
    data_cadastro_usuario()
    criar_senha_usuario()

# perfil

# cadastro do usuario


def confirmar_senha_usuario():
    for tentaivas in range(3):
        confirmar_senha = str(
            input(f'{cores["verde"]}Confirme sua senha para completarmos o processo:{cores["limpar"]} '))
        if confirmar_senha == dados_de_cadastro_do_usuario['senha usuario']:
            print(f'{cores["azul"]}OK!{cores["limpar"]}')
            break
        else:
            print(
                f'{cores["vermelho"]}Senha errada tente novamente.{cores["limpar"]}')


# cadastro do usuário


def cadastro_usuario():
    dados_de_cadastro_novo_usuario()
    confirmar_senha_usuario()


# campo de cadastro
corte_tela()
print(f'{cores["amarelo"]}---CADASTRO DE NOVO USUÁRIO---{cores["limpar"]}')
cadastro_usuario()

corte_tela()


# tela principal


def interacao():
    # def opcoes():

    print(
        f'{cores["amarelo"]}Bem-Vindo {dados_de_cadastro_do_usuario["nome"]}{cores["limpar"]}')
    corte_tela()

    def perfil_usuario():
        print(f'''{cores["roxo"]}Nome = {dados_de_cadastro_do_usuario['nome']}\nSobrenome = {dados_de_cadastro_do_usuario["sobrenome"]}\nData de nascimento = {dados_de_cadastro_do_usuario["data nascimento"]}{cores["limpar"]}''')
    # Editar perfil

    def editar_perfil_usuario():
        editar = str(
            input(f'{cores["verde"]}Oque devemos editar: {cores["limpar"]}')).lower()
        if editar == 'data_cadastro':
            print(
                f'{cores["vermalho"]}Não é possivel alterrar data de cadastro{cores["limpar"]}')
        else:
            confirmar_senha_usuario()
            dados_de_cadastro_do_usuario[f'{editar}'] = str(
                input(f'{cores["verde"]}Digite {editar}:{cores["limpar"]}'))

    def mostrar_perfil():
        mostrar = input(
            f'{cores["verde"]}Mostrar perfil: [1] sair [2]{cores["limpar"]}')
        if mostrar == '1':
            perfil_usuario()
            editar_perfil = input(
                f'{cores["verde"]}Editar perfil? sim[1] não[2]{cores["limpar"]}')
            if editar_perfil == '1':
                editar_perfil_usuario()
                corte_tela()
                perfil_usuario()
                interacao()
            else:
                interacao()
    mostrar_perfil()


interacao()
