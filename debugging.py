# Hicimos una depuracion para ver como identificar errores que nuestro editor no nos marca porque fue por error de logica y a la vez probamos manejar un error del tipo ValueError

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("Termino el programa")
    except ValueError:
        print("Debes ingresar un numero!")


if __name__ == '__main__':
    run()