

myList = ["cat","dog","cow"]

animalDictionary = [
    {
        'name':'cat',
        'sound':'meow'
    },
    {
        'name':'dog',
        'sound':'bowwowow'
    },
    {
        'name':'cow',
        'sound':'moo'
    }
]


for animal in myList:
    # Find the dictionary entry with the same name as the current animal
    for entry in animalDictionary:
        if entry['name'] == animal:
            print(f"The sound of {animal} is '{entry['sound']}'")
            break