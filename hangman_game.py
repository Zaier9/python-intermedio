import random
#import os

def read_data():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        datos = [line.strip("\n") for line in f]

    dict_datos = {key:value for key, value in enumerate(datos)}
    return dict_datos


def normalize(s): #Esto reemplaza las vocales con acento
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),)

    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def run():
    try:
        dict_datos = read_data()
        guess_word = normalize(dict_datos.get(random.randint(1, len(dict_datos)+1)))
        guessed_word = len(guess_word)*'-'
        print("""Bienvenido al juego del ahorcado!\n
        Adivina la siguiente palabra""")

        while guess_word != guessed_word:
            print(guessed_word)
            word = normalize(input("Ingresa una letra: "))
            if word in guess_word:
                guessed_word = list(guessed_word)
                for i,x in enumerate(guess_word):
                    if x == word:
                        guessed_word[i] = x
                guessed_word = "".join(guessed_word)
            #os.system("cls")
        print(f"Ganaste! tu plabara era {guessed_word}")

        play_again = int(input("Quieres jugar de nuevo?: \n1. Si\n2. No\n"))
        if play_again == 1:
            run()
        else:
            print("Nos vemos prnto :)")

    except ValueError:
        print("Solo se permiten letras :/")


if __name__ == '__main__':
    run()