def run():
    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # print(squares)

    # LIST COMPREHENSIONS
    squares = [i**2 for i in range(1,101) if i % 3 != 0]

    print(squares)

    print('='*70)

    # List comprehension de un numero que es divisible por 4, 6 y 9
    multiple = [i for i in range(1,10000) if i % 36 == 0]

    print(multiple)


if __name__ == '__main__':
    run()