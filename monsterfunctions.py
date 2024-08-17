def create_monster_cast():
    return {}

def add_cast_member(monsters, character, cast_member):
    monsters[character] = cast_member
    return monsters

def get_cast_member(monsters, character):
    cast_member = monsters[character]
    return cast_member
def get_cast_size(monsters):
    i = 0
    for i in range(len(monsters)):
        i = i +1
    return i

def change_cast_member(monsters, character, cast_member):
    monsters[character] = cast_member
    return monsters

def has_character(monsters, character):
    return character in monsters

def has_cast_member(monsters, cast_member):
    return cast_member in monsters.values()

def get_longest_cast_member(monsters):
    longest_cast_member = ""  # Initialize with an empty string

    for cast_member in monsters.values():
        if len(cast_member) > len(longest_cast_member):
            longest_cast_member = cast_member  # Update with the longer name

    return longest_cast_member
def get_longest_character(monsters):
    longest_character = ""  # Initialize with an empty string

    for character_name in monsters.keys():
        if len(character_name) > len(longest_character):
            longest_character = character_name  # Update with the longer name

    return longest_character
