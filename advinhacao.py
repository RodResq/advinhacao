print("Bem vindo ao jogos de adivinacao!")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

print("Voce digitou: ", chute_str)

chute_int = int(chute_str)

acertou = chute_int == numero_secreto
maior   = chute_int > numero_secreto
menor   = chute_int < numero_secreto

if(acertou):
    print("Voce acertou")
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto.")
print("Fim do jogo")