import sys


class Character:
    name = ""
    age = 0
    height = 0
    level = 0
    ancestry = ""
    character_class = ""
    ancestry_feat = ""
    heritage = ""
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
    def __init__(self, age, height, level, ancestry, character_class, ancestry_feat, heritage, stats):
        self.age = age
        self.height = height
        self.level = level
        self.ancestry = ancestry
        self.character_class = character_class
        self.ancestry_feat = ancestry_feat
        self.heritage = heritage
        self.stats = stats


def init():
    print("Welcome to Pathfinder 2e Character Builder!")
    user_choice = ""
    while user_choice != 'Y' and user_choice != 'N':
        user_choice = input("(Y) Start | (N) Exit").upper()
        if user_choice == 'N':
            sys.exit(0)


def choose_ancestry():
    ancestries = [
        "DWARF",
        "ELF",
        "GNOME",
        "GOBLIN",
        "HALFLING",
        "HUMAN",
    ]
    # prints to the user all available options
    for i in range(len(ancestries)):
        print("%i) %s" % (i+1, ancestries[i]))

    # Repeatedly prompt the user until they enter a valid ancestry.
    # Input must be spelt correctly, but spaces and capitalization do not matter.
    choice = ""
    while choice.replace(" ", "").upper() not in ancestries:
        choice = input("Type in your chosen ancestry (Invalid input will cause another prompt): ")
    return choice.replace(" ", "").upper()


def choose_heritage(ancestry):
    dwarf = [
        "ANCIENT-BLOODED DWARF",
        "ANVIL DWARF",
        "DEATH WARDEN DWARF",
        "ELEMENTAL HEART DWARF",
        "FORGE DWARF",
        "OATHKEEPER DWARF",
        "ROCK DWARF",
        "STRONG-BLOODED DWARF"
    ]
    elf = [
        "ANCIENT ELF",
        "ARCTIC ELF",
        "CAVERN ELF",
        "DESERT ELF",
        "SEER ELF",
        "WHISPER ELF",
        "WOODLAND ELF",
    ]
    gnome = [
        "CHAMELEON GNOME",
        "FEY-TOUCHED GNOME",
        "SENSATE GNOME",
        "UMBRAL GNOME",
        "VIVACIOUS GNOME",
        "WELLSPRING GNOME"
    ]
    goblin = [
        "CHARHIDE GOBLIN",
        "IRONGUT GOBLIN",
        "RAZORTOOTH GOBLIN",
        "SNOW GOBLIN",
        "TAILED GOBLIN",
        "TREEDWELLER GOBLIN",
        "UNBREAKABLE GOBLIN"
    ]
    halfling = [
        "GUTSY HALFLING",
        "HILLOCK HALFLING",
        "NOMADIC HALFLING",
        "TWILIGHT HALFLING",
        "WILDWOOD HALFLING"
    ]
    human = [
        "SKILLED HERITAGE",
        "VERSATILE HERITAGE",
        "WINTERTOUCHED HERITAGE"
    ]

    # Displays the appropriate heritage for the given ancestry
    # Repeatedly prompt the user until they enter a valid heritage.
    # Input must be spelt correctly, and spacing must be correct. Capitalization does not matter.
    if ancestry == "DWARF":
        for i in range(len(dwarf)):
            print("%i) %s" % (i+1, dwarf[i]))
        choice = ""
        while choice.upper() not in dwarf:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.upper()

    elif ancestry == "ELF":
        for i in range(len(elf)):
            print("%i) %s" % (i+1, elf[i]))
        choice = ""
        while choice.upper() not in elf:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.upper()

    elif ancestry == "GNOME":
        for i in range(len(gnome)):
            print("%i) %s" % (i+1, gnome[i]))
        choice = ""
        while choice.upper() not in gnome:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.upper()

    elif ancestry == "GOBLIN":
        for i in range(len(goblin)):
            print("%i) %s" % (i+1, goblin[i]))
        choice = ""
        while choice.upper() not in goblin:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.upper()

    elif ancestry == "HALFLING":
        for i in range(len(halfling)):
            print("%i) %s" % (i+1, halfling[i]))
        choice = ""
        while choice.upper() not in halfling:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.upper()

    elif ancestry == "HUMAN":
        for i in range(len(human)):
            print("%i) %s" % (i+1, human[i]))
        choice = ""
        while choice.upper() not in human:
            choice = input("Type in your chosen heritage (Invalid input will cause another prompt): ")
        return choice.upper()


def choose_background():
    options = [
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
