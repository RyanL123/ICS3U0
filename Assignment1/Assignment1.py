#-----------------------------------------------------------------------------
# Name:        Assignment 1
# Purpose:     Design software that is able to assist in creating a character in Pathfinder 2e
#
# Author:      767571
# Created:     Oct-25-19
# Updated:     Oct-28-19
#-----------------------------------------------------------------------------

# TODO

import sys
import time


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
    stats = {}

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
def choose_ancestry(stats):
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

    # Repeatedly prompt the user until they enter an integer within the range of options
    choice = -1
    while not(1 <= choice <= 6):
        try:
            choice = int(input("Type in your chosen ancestry: "))
            if not(1 <= choice <= 6):
                print("Please input an integer between 1 - 6")
                continue
            break
        except:
            print("Please input an integer between 1 - 6")
    # Modify stats based on ancestry
    boost_options = [
        "Str",
        "Dex",
        "Con",
        "Int",
        "Wis",
        "Cha"
    ]
    for i in range(len(boost_options)):
        print("%i) %s" % (i + 1, boost_options[i]))
    if choice == 1:
        stats["Con"] += 2
        stats["Wis"] += 2
        stats["Cha"] -= 2
        # Lets the user pick 1 free ability boost
        free_boost(stats, boost_options)
    elif choice == 2:
        stats["Dex"] += 2
        stats["Int"] += 2
        stats["Con"] -= 2
        free_boost(stats, boost_options)
    elif choice == 3:
        stats["Con"] += 2
        stats["Cha"] += 2
        stats["Str"] -= 2
        free_boost(stats, boost_options)
    elif choice == 4:
        stats["Dex"] += 2
        stats["Wis"] += 2
        stats["Str"] -= 2
        free_boost(stats, boost_options)
    elif choice == 5:
        stats["Dex"] += 2
        stats["Wis"] += 2
        stats["Str"] -= 2
        free_boost(stats, boost_options)
    else:
        free_boost(stats, boost_options)
        free_boost(stats, boost_options)
    return ancestries[choice-1]


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
    # Repeatedly prompt the user until they an integer within the range of options
    if ancestry == "Dwarf":
        for i in range(len(dwarf)):
            print("%i) %s" % (i+1, dwarf[i]))
        choice = -1
        while not (1 <= choice <= 8):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 8):
                    print("Please input an integer between 1 - 8")
                    continue
                break
            except:
                print("Please input an integer between 1 - 8")
        return dwarf[choice - 1]

    elif ancestry == "Elf":
        for i in range(len(elf)):
            print("%i) %s" % (i+1, elf[i]))
        choice = -1
        while not (1 <= choice <= 7):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 7):
                    print("Please input an integer between 1 - 7")
                    continue
                break
            except:
                print("Please input an integer between 1 - 7")
        return elf[choice - 1]

    elif ancestry == "Gnome":
        for i in range(len(gnome)):
            print("%i) %s" % (i+1, gnome[i]))
        choice = -1
        while not (1 <= choice <= 6):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 6):
                    print("Please input an integer between 1 - 6")
                    continue
                break
            except:
                print("Please input an integer between 1 - 6")
        return gnome[choice - 1]

    elif ancestry == "Goblin":
        for i in range(len(goblin)):
            print("%i) %s" % (i+1, goblin[i]))
        choice = -1
        while not (1 <= choice <= 7):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 7):
                    print("Please input an integer between 1 - 7")
                    continue
                break
            except:
                print("Please input an integer between 1 - 7")
        return goblin[choice - 1]

    elif ancestry == "Halfling":
        for i in range(len(halfling)):
            print("%i) %s" % (i+1, halfling[i]))
        choice = -1
        while not (1 <= choice <= 5):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 5):
                    print("Please input an integer between 1 - 5")
                    continue
                break
            except:
                print("Please input an integer between 1 - 5")
        return halfling[choice - 1]

    elif ancestry == "Human":
        for i in range(len(human)):
            print("%i) %s" % (i+1, human[i]))
        choice = -1
        while not (1 <= choice <= 3):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 3):
                    print("Please input an integer between 1 - 3")
                    continue
                break
            except:
                print("Please input an integer between 1 - 3")
        return human[choice - 1]


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
    uppercase_list = [i.replace(" ", "").upper() for i in backgrounds]
    choice = ""
    while choice.replace(" ", "").upper() not in uppercase_list:
        choice = input("Type in your chosen background (Invalid input will cause another prompt): ")

    # Locates the index of the background the user gave, and return the properly formatted text
    index = -1
    for i in range(len(uppercase_list)):
        if uppercase_list[i] == choice.replace(" ", "").upper():
            index = i
            break
    return backgrounds[index]


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
    choice = -1
    while not (1 <= choice <= 12):
        try:
            choice = int(input("Type in your chosen ancestry: "))
            if not (1 <= choice <= 12):
                print("Please input an integer between 1 - 12")
                continue
            break
        except:
            print("Please input an integer between 1 - 12")
    return classes[choice - 1]


# Utility function to let the user choose free ability boosts
def free_boost(stats, boost_options):
    # Lets the user pick 1 free ability boost
    user_boost_choice = -1
    while not (1 <= user_boost_choice <= 6):
        try:
            user_boost_choice = int(input("Type in your chosen free ability boost: "))
            if not (1 <= user_boost_choice <= 6):
                print("Please input an integer between 1 - 6")
                continue
            break
        except:
            print("Please input a integer between 1 - 6")
    stats[boost_options[user_boost_choice-1]] += 2


# Prints the name of every character
def view_characters(characters):
    if len(characters) == 0:
        print("You haven't created anything yet!")
        return
    for i in range(len(characters)):
        print("%i) %s" % (i+1, characters[i].name))


# Gets detailed statistics for the given character
def character_details(characters):
    character_name = input("Please input the name of the character (Must be exact same): ")
    for i in range(len(characters)):
        if characters[i].name.upper() == character_name.upper():
            print("Name: %s" % characters[i].name)
            print("Age: %i" % characters[i].age)
            print("Height: %i" % characters[i].height)
            print("Ancestry: %s" % characters[i].ancestry)
            print("Heritage: %s" % characters[i].heritage)
            print("Ancestry Feat: %s" % characters[i].ancestry_feat)
            print("Background: %s" % characters[i].background)
            print("Class: %s" % characters[i].character_class)
            print("Str: %i" % characters[i].stats["Str"])
            print("Dex: %i" % characters[i].stats["Dex"])
            print("Con: %i" % characters[i].stats["Con"])
            print("Int: %i" % characters[i].stats["Int"])
            print("Wis: %i" % characters[i].stats["Wis"])
            print("Cha: %i" % characters[i].stats["Cha"])
            return
    print("A character with that name does not exist")


# Displays menu
def menu(characters):
    choice = ""
    while choice != '1' and choice != '2' and choice != '3' and choice != '4':
        choice = input("(1) Create new character | (2) View created characters | (3) View Character Details | "
                       "(4) Exit Program: ")
    if choice == "4":
        sys.exit()
    elif choice == "3":
        character_details(characters)
        menu(characters)
    elif choice == "2":
        view_characters(characters)
        menu(characters)


# Cool progress bar to make the user think the code actually does something
def progress_bar():
    print("(█) 10%")
    time.sleep(1/10)
    print("Enumerating objects")
    time.sleep(1/10)
    print("Counting objects")
    time.sleep(1/10)
    print("(████) 40%")
    time.sleep(1/10)
    print("Delta compression")
    time.sleep(1/10)
    print("(███████) 70%")
    time.sleep(1/10)
    print("Compressing objects")
    time.sleep(1/10)
    print("(█████████) 90%")
    time.sleep(1/10)
    print("Writing objects")
    time.sleep(1/10)
    print("Resolving deltas")
    time.sleep(1/10)
    print("(██████████) 100%")
    time.sleep(1/10)
    print("\nCharacter creation complete!")


# Main driver code
def main():
    # Avoids the use of global variables
    characters = []
    global_stats = {
        "Str": 10,
        "Dex": 10,
        "Con": 10,
        "Int": 10,
        "Wis": 10,
        "Cha": 10
    }
    init()
    while True:
        menu(characters)
        base_characteristics = choose_characteristics()
        local_name = base_characteristics[0]
        local_age = base_characteristics[1]
        local_height = base_characteristics[2]
        print("")
        local_ancestry = choose_ancestry(global_stats)
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
                                    1,
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


main()
