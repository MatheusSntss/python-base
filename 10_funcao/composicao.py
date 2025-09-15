""" Print only names that start whit the letter b """

names = [
    'Alice',
    'Barbara',
    'Bruno',
    'Jota',
    'Joca'
]

def names_with_b(name):
    return name[0].lower() == 'b'

print(list(filter(names_with_b,names)))
    
