# A game build by Christian Prenholato just using python to train and developer some project
import time
import random


jogadas = ['pedra', 'papel', 'tesoura']

def inicio():
    print("#"*32)
    print(" "*5,"SEJA BEM VINDO AO JOGO")
    print(" "*10,"JOKENPO")
    print("#"*32)

def clear():
    import os
    os.system('cls') or None

def sistema(escolha_jogador,escolha_bot):
    if escolha_jogador == escolha_bot:
        print("Ufaa, Houve um EMPATE")
        print("Você jogou",escolha_jogador, "e o bot jogou",escolha_bot)
        print("Tente jogar novamente...")
        time.sleep(4)
        clear()
    
    elif (escolha_jogador == 'pedra' and escolha_bot == 'tesoura') or (escolha_jogador == 'tesoura' and escolha_bot == 'papel') or (escolha_jogador == 'papel' and escolha_bot == 'pedra'):
        print("UHULLL, VOCÊ GANHOOOOUU")
        print("Você jogou",escolha_jogador, "e o bot jogou",escolha_bot)
        time.sleep(4)
        clear()
    
    else:
        print("Não foi dessa vez, você PERDEU")
        print("Você jogou",escolha_jogador, "e o bot jogou",escolha_bot)
        time.sleep(4)
        clear()

def carregamento():
    print("[-----------]")
    time.sleep(0.2)
    clear()
    print("[■----------]")
    time.sleep(0.2)
    clear()
    print("[■■---------]")
    time.sleep(0.2)
    clear()
    print("[■■■--------]")
    time.sleep(0.2)
    clear()
    print("[■■■■-------]")
    time.sleep(0.2)
    clear()
    print("[■■■■■------]")
    time.sleep(0.2)
    clear()
    print("[■■■■■■-----]")
    time.sleep(0.2)
    clear()
    print("[■■■■■■■----]")
    time.sleep(0.2)
    clear()
    print("[■■■■■■■■---]")
    time.sleep(0.2)
    clear()
    print("[■■■■■■■■■--]")
    time.sleep(0.2)
    clear()
    print("[■■■■■■■■■■-]")
    time.sleep(0.2)
    clear()
    print("[■■■■■■■■■■■]")

def main():
    inicio()
    time.sleep(1)
    nome_jogador = input("Digite seu nome Jogador:")
    print("Bem vindo",nome_jogador)
    print()

    while True:
        print("Escolha entre as opções: 'pedra', 'papel' ou 'tesoura'")
        print("Para sair, basta apertar ENTER")
        escolha_jogador = input()
        print()

        if escolha_jogador == "":
            print("O jogo será encerrado, Obrigado por jogar :D")
            break
            

        elif escolha_jogador not in jogadas:
            print("Aconteceu algo de errado com sua entrada, tente novamente :D")
        
        else:
            print("Aguardando a jogada do bot")
            escolha_bot = random.choice(jogadas)
            carregamento()
            sistema(escolha_jogador,escolha_bot)

main()
