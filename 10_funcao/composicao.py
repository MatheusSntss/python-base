""" Print only names that start whit the letter b """

names = [
    'Alice',
    'Barbara',
    'Bruno',
    'Jota',
    'Joca'
]


print(list(filter(lambda name: name[0].lower() == 'b',names)))
    
