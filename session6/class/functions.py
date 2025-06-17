
dictionary = {
        'somon': 'A',
        'yunus': 'B',
        'elsu': '-A',
        'jonathan': '+A',
        'merim': 'C',
        'abdul': 'F'
    }

def function():
    try:
        inp = input('put the name of a student: ')
        print(dictionary[inp])
    except KeyError:
        print('The name is not in the dictionary')

function()