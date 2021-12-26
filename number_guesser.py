import random

top_of_range = input("Tipo do número: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Por favor, digite um número maior que 0 da proxima vez")
        quit()
else:
    print("Por favor, digite um número proxima vez")
    quit()

random_number = random.randrange(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Adivinhe: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Por favor, digite um número proxima vez")
        continue

    if user_guess == random_number:
        print("Você conseguiu!")
        break
    elif user_guess > random_number:
        print("Está acima desse número")
    else:
        print("Está abaixo do número")

print("Você conseguiu", guesses, "guesses")