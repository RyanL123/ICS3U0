#-----------------------------------------------------------------------------
# Name:        Assignment 1
# Purpose:     Design software that is able to assist in creating a character in Pathfinder 2e
#
# Author:      767571
# Created:     Oct-25-19
# Updated:     Oct-25-19
#-----------------------------------------------------------------------------

# TODO
# When creating character object, use official names instead of user inputs

import sys
import time
import random

class Character:
    name = ""
    age = 0
    height = 0
    level = 0
    ancestry = ""
    heritage = ""
    ancestry_feat = ""
    background = ""
    character_class = ""
    backpack = []
    stats = {
        "Str": 0,
        "Dex": 0,
        "Con": 0,
        "Int": 0,
        "Wis": 0,
        "Cha": 0
    }

    # constructor
    def __init__(self, name, age, height, level, ancestry, heritage, ancestry_feat, background, character_class, backpack, stats):
        self.name = name
        self.age = age
        self.height = height
        self.level = level
        self.ancestry = ancestry
        self.heritage = heritage
        self.ancestry_feat = ancestry_feat
        self.background = background
        self.character_class = character_class
        self.backpack = backpack
        self.stats = stats


# Debriefs the user on the uses of the program
def init():
    print("Welcome to Pathfinder 2e Character Builder!\n")
    print("This program will assist you in constructing a character for playing Pathfinder 2e.")
    print("Once finished, you can create another character, or modify your current character as you go.\n")
    user_choice = ""
    while user_choice != 'Y' and user_choice != 'N':
        user_choice = input("(Y) Start | (N) Exit\n").upper()
        if user_choice == 'N':
            sys.exit()


# Returns the character's chosen name, age and height
def choose_characteristics():
    age = 0
    height = 0
    name = input("Input the desired name for your character: ")

    # Repeatedly prompt the user until they input an integer
    while True:
        try:
            age = int(input("Input the desired age for your character: "))
            break
        except:
            print("Please input an integer")
    while True:
        try:
            height = int(input("Input the desired height for your character (in cm): "))
            break
        except:
            print("Please input an integer")

    return [name, age, height]


# Returns the user's chosen ancestry
def choose_ancestry():
    ancestries = [
        "Dwarf",
        "Elf",
        "Gnome",
        "Goblin",
        "Halfling",
        "Human",
    ]
    ancestries_match_user_input = [i.upper() for i in ancestries]
    print("<<<Choose your ancestry>>>")

    # prints to the user all available options
    for i in range(len(ancestries)):
        print("%i) %s" % (i+1, ancestries[i]))

    # Repeatedly prompt the user until they enter a valid ancestry.
    # Input must be spelt correctly, but spaces and capitalization do not matter.
    choice = ""
    while choice.replace(" ", "").upper() not in ancestries_match_user_input:
        choice = input("Type in your chosen ancestry (Invalid input will cause another prompt): ")
    return choice.replace(" ", "").upper()


# Returns the user's chosen heritage
def choose_heritage(ancestry):
    dwarf = [
        "Ancient-Blooded Dwarf",
        "Anvil Dwarf",
        "Death Warden Dwarf",
        "Elemental Heart Dwarf",
        "Forge Dwarf",
        "Oathkeeper Dwarf",
        "Rock Dwarf",
        "Strong-blooded Dwarf"
    ]
    elf = [
        "Ancient Elf",
        "Arctic Elf",
        "Cavern Elf",
        "Desert Elf",
        "Seer Elf",
        "Whisper Elf",
        "Woodland Elf",
    ]
    gnome = [
        "Chameleon Gnome",
        "Fey-Touched Gnome",
        "Sensate Gnome",
        "Umbral Gnome",
        "Vivacious Gnome",
        "Wellspring Gnome"
    ]
    goblin = [
        "Charhide Goblin",
        "Irongut Goblin",
        "Razortooth Goblin",
        "Snow Goblin",
        "Tailed Goblin",
        "Treedweller Goblin",
        "Unbreakable Goblin"
    ]
    halfling = [
        "Gutsy Halfling",
        "Hillock Halfling",
        "Nomadic Halfling",
        "Twilight Halfling",
        "Wildwood Halfling"
    ]
    human = [
        "Skilled Heritage",
        "Versatile Heritage",
        "Wintertouched Heritage"
    ]
    print("<<<Choose your heritage>>>")

    # Displays the appropriate heritage for the given ancestry
    # Repeatedly prompt the user until they enter a valid heritage.
    # Input must be spelt correctly, but spaces and capitalization do not matter.
    if ancestry == "DWARF":
        for i in range(len(dwarf)):
            print("%i) %s" % (i+1, dwarf[i]))
        choice = ""
        while choice.replace(" ", "").upper() not in [i.replace(" ", "").upper() for i in dwarf]:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.replace(" ", "").upper()

    elif ancestry == "ELF":
        for i in range(len(elf)):
            print("%i) %s" % (i+1, elf[i]))
        choice = ""
        while choice.replace(" ", "").upper() not in [i.replace(" ", "").upper() for i in elf]:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.replace(" ", "").upper()

    elif ancestry == "GNOME":
        for i in range(len(gnome)):
            print("%i) %s" % (i+1, gnome[i]))
        choice = ""
        while choice.replace(" ", "").upper() not in [i.replace(" ", "").upper() for i in gnome]:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.replace(" ", "").upper()

    elif ancestry == "GOBLIN":
        for i in range(len(goblin)):
            print("%i) %s" % (i+1, goblin[i]))
        choice = ""
        while choice.replace(" ", "").upper() not in [i.replace(" ", "").upper() for i in goblin]:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.replace(" ", "").upper()

    elif ancestry == "HALFLING":
        for i in range(len(halfling)):
            print("%i) %s" % (i+1, halfling[i]))
        choice = ""
        while choice.replace(" ", "").upper() not in [i.replace(" ", "").upper() for i in halfling]:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.replace(" ", "").upper()

    elif ancestry == "HUMAN":
        for i in range(len(human)):
            print("%i) %s" % (i+1, human[i]))
        choice = ""
        while choice.replace(" ", "").upper() not in [i.replace(" ", "").upper() for i in human]:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.replace(" ", "").upper()


# Returns the user's chosen background
def choose_background():
    backgrounds = [
        "Academic",
        "Acolyte",
        "Acrobat",
        "Adherent",
        "Animal Whisperer",
        "Archaeologist",
        "Artifact Seeker",
        "Artisan",
        "Artist",
        "Aspiring Free Captain",
        "Aspiring River Monarch",
        "Barkeep",
        "Barrister",
        "Black Market Smuggler",
        "Bounty Hunter",
        "Bright Lion",
        "Charlatan",
        "Charmer",
        "Child of Squalor",
        "Child of the City",
        "Criminal",
        "Crusader",
        "Cursed Family",
        "Desert Tracker",
        "Detective",
        "Emissary",
        "Entertainer",
        "Expatriate",
        "Faithful",
        "Farmhand",
        "Field Medic",
        "Follower",
        "Fortune Teller",
        "Freed Slave",
        "Gambler",
        "Gladiator",
        "Goblinblood Orphan",
        "Grand Council Bureaucrat",
        "Guard",
        "Guerrilla",
        "Herbalist",
        "Hermit",
        "Hopeful",
        "Hunter",
        "Inlander",
        "Laborer",
        "Loyalist",
        "Lumberjack",
        "Mammoth Speaker",
        "Mantis Scion",
        "Martial Disciple",
        "Menagerie Dung Sweeper",
        "Mercenary",
        "Merchant",
        "Miner",
        "Mystic",
        "Name - Bearer",
        "Noble",
        "Nomad",
        "Onyx Trader",
        "Ooze - Tender",
        "Partisan",
        "Pearl Diver",
        "Perfection Seeker",
        "Press - Ganged",
        "Prisoner",
        "Prodigy",
        "Purveyor of the Bizarre",
        "Quick",
        "Raider",
        "Rancher",
        "Rebel",
        "Reclaimer",
        "Reformer",
        "Refugee",
        "Restorer",
        "Sailor",
        "Scavenger",
        "Schemer",
        "Scholar",
        "Scholar of the Ancients",
        "Scion",
        "Scout",
        "Secular Medic",
        "Shadow Haunted",
        "Slayer",
        "Smuggler",
        "Storm Survivor",
        "Street Urchin",
        "Survivor",
        "Tinker",
        "Trade Consortium Underling",
        "Traveler",
        "Undersea Enthusiast",
        "Unifier",
        "Wanderer",
        "Warrior",
        "Wavetouched",
        "Wildborne",
        "Winter’s Child",
        "Witch Wary",
        "Wonder Taster"
    ]
    print("<<<Choose your background>>>")
    print("Due to the amount of backgrounds, it is not feasible to print out all of them. Please refer to the "
          "rule book")
    # Prompts the user until they enter a valid background
    # Input must be spelt correctly, but spaces and capitalization do not matter.
    choice = ""
    while choice.replace(" ", "").upper() not in [i.replace(" ", "").upper() for i in backgrounds]:
        choice = input("Type in your chosen background (Invalid input will cause another prompt): ")
    return choice


def choose_class():
    classes = [
        "Alchemist",
        "Barbarian",
        "Bard",
        "Champion",
        "Cleric",
        "Druid",
        "Fighter",
        "Monk",
        "Ranger",
        "Rogue",
        "Sorcerer",
        "Wizard"
    ]
    print("<<<Choose your class>>>")

    # prints to the user all available options
    for i in range(len(classes)):
        print("%i) %s" % (i + 1, classes[i]))

    # Prompts the user until they enter a valid class
    # Input must be spelt correctly, but spaces and capitalization do not matter.
    choice = ""
    while choice.replace(" ", "").upper() not in [i.upper() for i in classes]:
        choice = input("Type in your chosen class: ")
    return choice


# Prints the name of every character
def view_characters():
    if len(characters) == 0:
        print("You haven't created anything yet!")
        return
    for i in range(len(characters)):
        print("%i) %s" % (i+1, characters[i].name))


# Displays menu
def menu():
    choice = ""
    while choice != '1' and choice != '2' and choice != '3':
        choice = input("(1) Create new character | (2) View created characters | (3) Exit program: ")
    if choice == "3":
        sys.exit()
    elif choice == "2":
        view_characters()
        menu()


def progress_bar():
    print("(█) 10%")
    time.sleep(random.randint(1, 10) / 10)
    print("Enumerating objects")
    time.sleep(random.randint(1, 10) / 10)
    print("Counting objects")
    time.sleep(random.randint(1, 10)/10)
    print("(████) 40%")
    time.sleep(random.randint(1, 10) / 10)
    print("Delta compression")
    time.sleep(random.randint(1, 10) / 10)
    print("(███████) 70%")
    time.sleep(random.randint(1, 10) / 10)
    print("Compressing objects")
    time.sleep(random.randint(1, 10) / 10)
    print("(█████████) 90%")
    time.sleep(random.randint(1, 10) / 10)
    print("Writing objects")
    time.sleep(random.randint(1, 10) / 10)
    print("Resolving deltas")
    time.sleep(random.randint(1, 10) / 10)
    print("(██████████) 100%")
    time.sleep(random.randint(1, 10) / 10)
    print("\nCharacter creation complete!")


# Global variables initialization
characters = []
global_stats = {
        "Str": 0,
        "Dex": 0,
        "Con": 0,
        "Int": 0,
        "Wis": 0,
        "Cha": 0
    }

# Main driver code
init()
while True:
    menu()
    base_characteristics = choose_characteristics()
    local_name = base_characteristics[0]
    local_age = base_characteristics[1]
    local_height = base_characteristics[2]
    local_level = 0
    print("")
    local_ancestry = choose_ancestry()
    print("")
    local_heritage = choose_heritage(local_ancestry)
    print("")
    local_ancestry_feat = ""
    print("")
    local_background = choose_background()
    print("")
    local_character_class = choose_class()
    print("")
    local_backpack = []
    characters.append(Character(local_name,
                                local_age,
                                local_height,
                                0,
                                local_ancestry,
                                local_heritage,
                                local_ancestry_feat,
                                local_background,
                                local_character_class,
                                local_backpack,
                                global_stats))
    progress_bar()
    # Sort characters by name lexicographically
    characters.sort(key=lambda x: x.name)

