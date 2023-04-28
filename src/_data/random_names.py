import random 

def give_name(): 
    with open("generated_names.txt", "r") as file:
        alltext = file.read():
        words = list(map(str, alltext.split(,)))
    print(random.choice(words))

give_name()
