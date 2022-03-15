# Hicimos una depuracion para ver como identificar errores que nuestro editor no nos marca porque fue por error de logica

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = int(input("Ingresa un numero: "))
    print(divisors(num))
    print("Termino el programa")


if __name__ == '__main__':
    run()