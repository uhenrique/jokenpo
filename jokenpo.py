from random import choice
from time import sleep

def linha(num):
    print('\033[31m-=\033[m'*num)

def cabeçalho():
    linha(25)
    print('JO KEN PO'.center(50))
    linha(25)

def jogar():
    cabeçalho()
    global jogada
    jogada = str(input('Escolha sua jogada: ')).lower().strip()
    global computador
    computador = choice(['pedra', 'papel', 'tesoura'])

def main():
    jogar()
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    linha(25)
    print(f'Jogador: {jogada}')
    print(f'Computador: {computador}')
    linha(25)

def resultado(jogada, computador):
    if jogada == computador:
        return 'Empate'
    elif jogada == 'pedra':
        if computador == 'papel':
            return 'Computador'
        else:
            return 'Jogador'
    elif jogada == 'papel':
        if computador == 'tesoura':
            return 'Computador'
        else:
            return 'Jogador'
    elif jogada == 'tesoura':
        if computador == 'pedra':
            return 'Computador'
        else:
            return 'Jogador'
        

confirm = 'S'
while confirm == 'S':
    
    main()
    
    if resultado(jogada, computador) == 'Empate':
        print("EMPATE!")
    else:
        if resultado(jogada, computador) == 'Computador':
            print("O computador ganhou :(")
        else:
            print("VOCÊ GANHOU!!! :D")
    
    confirm = input('Deseja jogar novamente? [S/N]: ').upper()
    while confirm not in 'SN':
        confirm = input('Deseja jogar novamente? [S/N]: ').upper()
    if confirm == 'N':
        print('Até a próxima! ;)')
        break