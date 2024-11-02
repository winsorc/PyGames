def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}:")
    return user_input


index = int(input("Enter a number [0-3] to select text. Enter -1 to quit:"))
if  index == 0:
    pnoun1 = get_input("plural noun")
    noun1 = get_input("noun")
    pnoun2 = get_input("plural noun")
    adjective1 = get_input("adjective")
    noun2 = get_input("noun")
    adjective2 = get_input("adjective")
    noun3 = get_input("noun")
    quote = f"""
    The {pnoun1} want my {noun1}.
    but I'll give them naught but {pnoun2}. 
    Let him be king over {adjective1} {noun2} and {adjective2} {noun3}. 
    Let him be the king of {noun1}.
    """
elif index == 1:
    adjective1 = get_input("adjective")
    animals = get_input("animal (plural)")
    noun1 = get_input("noun")
    animal = get_input("animal (singular)")
    adjective2 = get_input("adjective")
    verb1 = get_input("verb")
    adjective3 = get_input("adjective")
    adjective4 = get_input("adjective")
    noun2 = get_input("noun")
    quote = q1 = f""" The {adjective1} {animals} have closed their {noun1}, but the {animal} sees the truth. 
{adjective2} powers waken. Shadows {verb1}. 
An age of {adjective3} and {adjective4} will soon be upon us, an age for gods and {noun2}.
"""
elif index == 2:
    verb1 = get_input("verb")
    noun1 = get_input("noun")
    noun2 = get_input("noun(plural)")
    verb2 = get_input("verb")
    clothing_item = get_input("Clothing Item")
    verb3 = get_input("verb")
    noun3 = get_input("noun")
    place = get_input("place")
    weapon = get_input("weapon")
    quote = f""" Night gathers, and now my {verb1} begins. 
It shall not end until my death. I shall take no {noun1}, hold no {noun2}, {verb2} no children. 
I shall wear no {clothing_item} and {verb3} no {noun3}. I shall live and die at my {place}. I am the {weapon} in the darkness.
"""
elif index == 3:
    noun1 = get_input("noun(plural)")
    adjective1 = get_input("adjective")
    adjective2 = get_input("adjective")
    noun2 = get_input("noun")
    noun3 = get_input("noun(plural)")
    adjective3 = get_input("adjective")
    quote = q3 = f""" {noun1} live their lives {adjective1} in an {adjective2} {noun2}, 
between the {noun3} of memory and the sea of {adjective3} that is all we know of the days to come.
"""
elif index == -1:
    print('Quitting...')
    exit




print(quote)

