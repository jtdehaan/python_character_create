import random
import string

def stat():
    aa = random.randrange(1,6)
    ab = random.randrange(1,6)
    ac = random.randrange(1,6)
    ad = random.randrange(1,6)
    mi = min(aa, ab, ac, ad)
    ret = aa + ab +ac+ ad- mi
    return ret

def prof():
     prof_list = ["Acrobatics", "Animal Handling", "Arcana","Athletics","Deception","History","Insight","Intimidation", "Investigation","Medicine","Nature", "Perception","Performance","Persuasion","Religion","Sleight of Hand", "Stealth","Survival"]
     prof_one = random.choice(prof_list)
     prof_two = random.choice(prof_list)
     return prof_one, prof_two

def create_initial():
    lower_alphabet = string.ascii_lowercase
    initiala = random.choice(lower_alphabet)
    initiala = initiala.upper()
    return initiala

def find_weapon():
    #how many?
    weapon_list= ["Club","Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Light Crossbow","Dart", "Shortbow", "Sling"]
    weapon_one = random.choice(weapon_list)
    return weapon_one 

def print_char():
    print("Name ", initial+".")
    print("STR", s)
    print("DEX", d)
    print("CON", c)
    print("INT", i)
    print("WIS", w)
    print("CHAR", ch)
    if prof1 == prof2:
        print("Double Proficiency in "+prof1+"!")
    else:
        print("Proficiencies:", prof1+",", prof2)
    print("Weapons:" + weapon)
    print()
    print("-----------------------------------------------------------")

x = int(input("How many characters are you creating? "))

for y in range(x):
    initial= create_initial()
    s = stat()
    d = stat()
    c = stat()
    i = stat()
    w = stat()
    ch = stat()
    prof1, prof2 = prof()
    weapon = find_weapon()
    print_char()



