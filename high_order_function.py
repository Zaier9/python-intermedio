from functools import reduce

def high():
    my_list = [1,2,3,4,5,7,9,12,35,80,88,90]

    #odd = [i for i in my_list if i % 2 != 0]
    
    # Trabajando con la funcion filter nos olvidamos de usar el ciclo for, la funcion filter retorna un iterador.
    odd = list(filter(lambda x: x%2 != 0, my_list))

    print(odd)


def order():
    my_list = [1,2,3,4,5]

    # Trabajando con la funcion map.
    squares = list(map(lambda x: x**2, my_list))

    print(squares)


def function():
    my_list = [2,2,2,2,5,4]

    #Trabajando con reduce, debemos importar la funcion para poder usarla.
    all_multiplied = reduce(lambda a, b: a * b, my_list)

    print(all_multiplied)

if __name__ == '__main__':
    high()
    order()
    function()