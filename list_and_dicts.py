def run():
    my_list = [1, 'hello', True, 4.50]
    my_dict = {'firstname': 'Zaier', 'lastname': 'Vera'}

    super_list = [
        {'firstname': 'Zaier', 'lastname': 'Vera'},
        {'firstname': 'Agus', 'lastname': 'Vera'},
        {'firstname': 'Rosana', 'lastname': 'Silva'},
        {'firstname': 'Kiara', 'lastname': 'Salcedo'},
        {'firstname': 'Lionel', 'lastname': 'Messi'},
        {'firstname': 'Antonella', 'lastname': 'Rocuzzo'},
        {'firstname': 'Santiago', 'lastname': 'Silva'},
    ]

    super_dict = {
        'natural_nums': [1,2,3,4,5],
        'integer_nums': [-1,-2,0,3,4,5],
        'floating_nums': [1.1,2.5,3.89,4.0,5.5],
    }

    for key, value in super_dict.items():
        print(key, "->", value)
    
    print('-'*40)
    
    # for i in super_list:
    #     for key, values in i.items():
    #         print(key, ": ", values)
    for i in super_list:
        print(i.items())

if __name__ == '__main__':
    run()