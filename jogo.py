from random import randint
print("Bem vindo!!!")
novo_jogo = True
while novo_jogo != False:
    numero_sorteado = randint(1,100)
    contador = 1
    while True:
        chute = int(input("Chute um numero:"))
        if chute == numero_sorteado:
            print("Parabens, voce e foda.")
            break
        else:
            
