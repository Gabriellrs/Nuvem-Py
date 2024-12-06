#Bibliotecas Utilizadas
import random

lista_palavras = ["Harry Potter", "Meu Malvado Favorito", "Eu sou a Lenda", "Star Wars", "Clube da Luta"]

max_tentativa = 4
tentativas = 0

letras_usadas = []

tam_lista = len(lista_palavras)  # 1,2,3 ... não começa do 0

def sortear_palavra(l):
    p = random.choice(l)
    return p

palavra_sorteada = sortear_palavra(lista_palavras)

while True:
    # Mostrar a palavra com as letras já descobertas
    for letra in palavra_sorteada:
        if letra.lower() in letras_usadas:
            print(letra, end="")
        elif letra == " ":
            print(" ", end="")
        else:
            print("_", end=" ")

    print("\n")

    # Pedir palpite ao jogador
    palpite_do_jogador = input("Digite uma letra: ").lower()

    # Verificar se a letra já foi usada
    if palpite_do_jogador in letras_usadas:
        print("Essa letra já foi utilizada!")
        continue

    letras_usadas.append(palpite_do_jogador)

    # Verificar se a letra está na palavra
    if palpite_do_jogador in palavra_sorteada.lower():
        print("Essa letra está na palavra!")
    else:
        print("Essa letra não está na palavra!")
        tentativas += 1
        print(f"Tentativas Restantes: {max_tentativa - tentativas}")

    # Verificar condição de derrota
    if tentativas >= max_tentativa:
        print(f"\nVocê perdeu! O filme era: {palavra_sorteada}")
        break

    # Verificar condição de vitória
    if all(letra.lower() in letras_usadas or letra == " " for letra in palavra_sorteada):
        print(f"\nParabéns! Você acertou o filme: {palavra_sorteada}")
        break

    #all() verifica se todas as condições dentro dele retorna True ou False, se todas forem True, então ele também retorna True