print("Bem vindo ao meu quiz")

playing = input("Você quer jogá-lo? ")

if playing.lower() != "yes":
    quit()

print("Ok! vamos jogar:)")
score = 0

answer = input("O que significa CPU? ")
if answer.lower() == "Central de processamento únitário":
    print('correto')
    score += 1
else:
    print('Incorreto')

answer = input("O que é uma GPU? ")
if answer.lower() == "Processador de gráficos únitário":
    print('correto')
    score += 1
else:
    print('Incorreto')

answer = input("O que significa memória RAM? ")
if answer.lower() == "Acesso a memoria Randomica":
    print('correto')
    score += 1
else:
    print('Incorreto')

answer = input("O que significa PSU? ")
if answer.lower() == "Fonte de energia":
    print('correto')
    score += 1
else:
    print('Incorreto')

print("Você conseguiu" + str(score) + "pontos")
print("Você conseguiu" + str((score / 4) * 100) + "%.")