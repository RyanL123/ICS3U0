# -----------------------------------------------------------------------------
# Name:        Assignments 2
# Purpose:     Design software that is able to assist in creating a character in Pathfinder 2e
#
# Author:      767571
# Created:     Jan-6-20
# Updated:     Jan-16-20
# -----------------------------------------------------------------------------

# Apologies in advance to anyone trying to understand this spaghetti code

import sys
import time
import logging

logging.basicConfig(filename="log.txt", level=logging.NOTSET, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.info("Start of program")


class Character:
    name = ""
    age = 0
    height = 0
    level = 0
    gold = 0
    ancestry = ""
    heritage = ""
    ancestry_feat = ""
    background = ""
    character_class = ""
    spells = []
    backpack = []
    stats = {}

    # constructor
    def __init__(self,
                 name,
                 age,
                 height,
                 level,
                 gold,
                 ancestry,
                 heritage,
                 ancestry_feat,
                 background,
                 character_class,
                 spells,
                 backpack,
                 stats):
        self.name = name
        self.age = age
        self.height = height
        self.level = level
        self.gold = gold
        self.ancestry = ancestry
        self.heritage = heritage
        self.ancestry_feat = ancestry_feat
        self.background = background
        self.character_class = character_class
        self.spells = spells
        self.backpack = backpack
        self.stats = stats


def init():
    """
    Basic instructions on how to use the program

    Displays a menu to the user. Asks the user if they want to run the program, then continues or exits based on their choice

    Parameters:
    ----------
    None

    Returns:
    ----------
    None
    """
    print("Welcome to Pathfinder 2e Character Builder!\n")
    print("This program will assist you in constructing a character for playing Pathfinder 2e.")
    print("Once finished, you can create another character, or view existing characters.\n")
    user_choice = ""
    while user_choice != 'Y' and user_choice != 'N':
        user_choice = input("(Y) Start | (N) Exit\n").upper()
        if user_choice == 'N':
            logging.info("Exiting program")
            sys.exit()


def choose_characteristics():
    """
    Gets basic information on the character

    Prompts the user for character age, name and height and returns all 3 as a list

    Parameters:
    ----------
    None

    Returns:
    ----------
    None
    """
    age = 0
    height = 0
    name = input("Input the desired name for your character: ")

    # Repeatedly prompt the user until they input an integer
    while True:
        try:
            age = int(input("Input the desired age for your character: "))
            if not age > 0:
                print("Please input a positive integer")
                continue
            break
        except ValueError:
            print("Please input a positive integer")
    while True:
        try:
            height = int(input("Input the desired height for your character (in cm): "))
            if not height > 0:
                print("Please input a positive integer")
                continue
            break
        except ValueError:
            print("Please input a positive integer")

    return [name, age, height]


def choose_ancestry(stats):
    """
    Gets the user's choice of ancestry

    Prompts the user for their ancestry chosen from a list of 6 options and returns it

    Parameters:
    ----------
    stats: dictionary
        Dictionary containing the character's statistics

    Returns:
    ----------
    String
        The chosen ancestry as an index of the ancestries list

    Raises:
    ------
    TypeError
        if stats is not a dictionary
    """
    ancestries = [
        "Dwarf",
        "Elf",
        "Gnome",
        "Goblin",
        "Halfling",
        "Human",
    ]
    print("⮘━━━━━━━Choose your ancestry━━━━━━━⮚")

    if not isinstance(stats, dict):
        logging.critical("Expecting stats to be a dictionary, but found " + str(type(stats)) + " instead")
        raise TypeError("Expecting stats to be a dictionary")

    # prints to the user all available options
    for i in range(len(ancestries)):
        print("%i) %s" % (i + 1, ancestries[i]))

    logging.debug("Starting choose ancestry with the current stats: " + str(stats))

    # Repeatedly prompt the user until they enter an integer within the range of options
    choice = -1
    while not (1 <= choice <= 6):
        try:
            choice = int(input("Type in your chosen ancestry: "))
            if not (1 <= choice <= 6):
                print("Please input an integer between 1 - 6")
                continue
            break
        except ValueError:
            print("Please input an integer between 1 - 6")
    # Modify stats based on ancestry
    boost_options = [
        "Strength",
        "Dexterity",
        "Constitution",
        "Intelligence",
        "Wisdom",
        "Charisma"
    ]
    print("\n⮘━━━━━━━Choose stat boost━━━━━━━⮚")
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

    logging.debug("Chosen ancestry: " + ancestries[choice - 1])
    logging.debug("Current stats: " + str(stats))
    return ancestries[choice - 1]

# assert choose_ancestry(
#     {
#         "Str": 10,
#         "Dex": 10,
#         "Con": 10,
#         "Int": 10,
#         "Wis": 10,
#         "Cha": 10
#     }
# ) == "Dwarf", "Expecting Dwarf to be returned when option 1 is chosen"

# assert choose_ancestry(
#     {
#         "Str": 10,
#         "Dex": 10,
#         "Con": 10,
#         "Int": 10,
#         "Wis": 10,
#         "Cha": 10
#     }
# ) == "Elf", "Expecting Dwarf to be returned when option 1 is chosen"


def choose_heritage(ancestry):
    """
    Gets the user's choice of heritage based on their chosen ancestry

    Prompts the user for their heritage based on the ancestry they chose. Uses data returned from the choose_ancestry() function

    Parameters:
    ----------
    ancestry: String
        The ancestry of the character object currently being created

    Returns:
    ----------
    String
        The chosen heritage as an index of the appropriate heritage list

    Raises
    ------
    TypeError
        if ancestry is not a string
    """
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

    # Make sure parameter is string
    if not isinstance(ancestry, str):
        logging.critical("Expecting ancestry to be a string, but found " + str(type(ancestry)) + " instead")
        raise TypeError("Expecting ancestry to be a string")
    logging.debug("Starting choose ancestry with the current ancestry: " + ancestry)

    print("⮘━━━━━━━Choose your heritage━━━━━━━⮚")

    # Displays the appropriate heritage for the given ancestry
    # Repeatedly prompt the user until they an integer within the range of options
    if ancestry == "Dwarf":
        for i in range(len(dwarf)):
            print("%i) %s" % (i + 1, dwarf[i]))
        choice = -1
        while not (1 <= choice <= 8):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 8):
                    print("Please input an integer between 1 - 8")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 8")
        logging.debug("Chosen heritage: " + dwarf[choice - 1])
        return dwarf[choice - 1]

    elif ancestry == "Elf":
        for i in range(len(elf)):
            print("%i) %s" % (i + 1, elf[i]))
        choice = -1
        while not (1 <= choice <= 7):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 7):
                    print("Please input an integer between 1 - 7")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 7")
        logging.debug("Chosen heritage: " + elf[choice - 1])
        return elf[choice - 1]

    elif ancestry == "Gnome":
        for i in range(len(gnome)):
            print("%i) %s" % (i + 1, gnome[i]))
        choice = -1
        while not (1 <= choice <= 6):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 6):
                    print("Please input an integer between 1 - 6")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 6")
        logging.debug("Chosen heritage: " + gnome[choice - 1])
        return gnome[choice - 1]

    elif ancestry == "Goblin":
        for i in range(len(goblin)):
            print("%i) %s" % (i + 1, goblin[i]))
        choice = -1
        while not (1 <= choice <= 7):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 7):
                    print("Please input an integer between 1 - 7")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 7")
        logging.debug("Chosen heritage: " + goblin[choice - 1])
        return goblin[choice - 1]

    elif ancestry == "Halfling":
        for i in range(len(halfling)):
            print("%i) %s" % (i + 1, halfling[i]))
        choice = -1
        while not (1 <= choice <= 5):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 5):
                    print("Please input an integer between 1 - 5")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 5")
        logging.debug("Chosen heritage: " + halfling[choice - 1])
        return halfling[choice - 1]

    elif ancestry == "Human":
        for i in range(len(human)):
            print("%i) %s" % (i + 1, human[i]))
        choice = -1
        while not (1 <= choice <= 3):
            try:
                choice = int(input("Type in your chosen ancestry: "))
                if not (1 <= choice <= 3):
                    print("Please input an integer between 1 - 3")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 3")
        logging.debug("Chosen heritage: " + human[choice - 1])
        return human[choice - 1]

# assert choose_heritage("Dwarf") == "Ancient-Blooded Dwarf", \
#     "Expecting Ancient-Blooded Dwarf when option 1 is chosen under the Dwarf ancestry"

# assert choose_heritage("Dwarf") == "Anvil Dwarf", \
#     "Expecting Ancient-Blooded Dwarf when option 1 is chosen under the Dwarf ancestry"


def choose_ancestry_feat(ancestry):
    """
    Get the user's choice of ancestry feat

    Prompts the user for their ancestry feat based on the ancestry they chose.
    Uses data returned from the choose_ancestry() function

    Parameters:
    ----------
    ancestry: String
        The ancestry of the character object currently being created

    Returns:
    ----------
    String
        The chosen heritage as an index of the appropriate heritage list

    Raises:
    ------
    TypeError
        if ancestry is not a string
    """
    dwarf = [
        "Avenge In Glory",
        "Clan’s Edge",
        "Dwarven Lore",
        "Dwarven Weapon Familiarity",
        "Forge-Day’s Rest",
        "Rock Runner",
        "Stonecunning",
        "Surface Culture",
        "Unburdened Iron",
        "Vengeful Hatred"
    ]
    elf = [
        "Ancestral Longevity",
        "Elemental WrathFeat",
        "Elven Lore",
        "Elven Verve",
        "Elven Weapon Familiarity",
        "Forlorn",
        "Nimble Elf",
        "Share Thoughts",
        "Otherworldly Magic",
        "Unwavering Mien",
        "Wildborn Magic",
        "Woodcraft"
    ]
    gnome = [
        "Animal Accomplice",
        "Burrow Elocutionist",
        "Fey Fellowship",
        "Fey World Magic",
        "Gnome Obsession",
        "Gnome Polyglot",
        "Gnome Weapon Familiarity",
        "Grim Insight",
        "Illusion Sense",
        "Inventive Offensive",
        "Life-Giving Magic",
        "Natural Performer",
        "Theoretical Acumen",
        "Unexpected Shift",
        "Vibrant Display",

    ]
    goblin = [
        "Bouncy Goblin",
        "Burn It!",
        "City Scavenger",
        "Fang Sharpener",
        "Goblin Lore",
        "Goblin Scuttle",
        "Goblin Song",
        "Goblin Weapon Familiarity",
        "Hard Tail",
        "Junk Tinker",
        "Rough Rider",
        "Very Sneaky"
    ]
    halfling = [
        "Adroit Manipulation",
        "Distracting Shadows",
        "Halfling Lore",
        "Halfling Luck",
        "Halfling Weapon Familiarity",
        "Innocuous",
        "Intuitive Cooperation",
        "Sure Feet",
        "Titan Slinger",
        "Unassuming Dedication",
        "Unfettered Halfling",
        "Watchful Halfling"
    ]
    human = [
        "Adapted Cantrip",
        "Arcane Tattoos",
        "Astrology",
        "Construct Summoner",
        "Cooperative Nature",
        "Courteous Comeback",
        "Devil’s Advocate",
        "Dragon Spit",
        "General Training",
        "Gloomseer",
        "Haughty Obstinacy",
        "Keep Up Appearances",
        "Know Oneself",
        "Natural Ambition",
        "Natural Skill",
        "Spirit Bond",
        "Unconventional Weaponry",
        "Viking Shieldbearer",
        "Witch Warden"
    ]

    # Make sure parameter is string
    if not isinstance(ancestry, str):
        logging.critical("Expecting ancestry to be a string, but found " + str(type(ancestry)) + " instead")
        raise TypeError("Expecting ancestry to be a string")

    print("⮘━━━━━━━Choose your ancestry feat━━━━━━━⮚")

    # Displays the appropriate heritage for the given ancestry
    # Repeatedly prompt the user until they an integer within the range of options
    if ancestry == "Dwarf":
        for i in range(len(dwarf)):
            print("%i) %s" % (i + 1, dwarf[i]))
        choice = -1
        while not (1 <= choice <= 10):
            try:
                choice = int(input("Type in your chosen ancestry feat: "))
                if not (1 <= choice <= 10):
                    print("Please input an integer between 1 - 10")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 10")
        logging.debug("Chosen ancestry feat: " + dwarf[choice - 1])
        return dwarf[choice - 1]

    elif ancestry == "Elf":
        for i in range(len(elf)):
            print("%i) %s" % (i + 1, elf[i]))
        choice = -1
        while not (1 <= choice <= 12):
            try:
                choice = int(input("Type in your chosen ancestry feat: "))
                if not (1 <= choice <= 12):
                    print("Please input an integer between 1 - 12")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 12")
        logging.debug("Chosen ancestry feat: " + elf[choice - 1])
        return elf[choice - 1]

    elif ancestry == "Gnome":
        for i in range(len(gnome)):
            print("%i) %s" % (i + 1, gnome[i]))
        choice = -1
        while not (1 <= choice <= 15):
            try:
                choice = int(input("Type in your chosen ancestry feat: "))
                if not (1 <= choice <= 15):
                    print("Please input an integer between 1 - 15")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 15")
        logging.debug("Chosen ancestry feat: " + gnome[choice - 1])
        return gnome[choice - 1]

    elif ancestry == "Goblin":
        for i in range(len(goblin)):
            print("%i) %s" % (i + 1, goblin[i]))
        choice = -1
        while not (1 <= choice <= 12):
            try:
                choice = int(input("Type in your chosen ancestry feat: "))
                if not (1 <= choice <= 12):
                    print("Please input an integer between 1 - 12")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 12")
        logging.debug("Chosen ancestry feat: " + goblin[choice - 1])
        return goblin[choice - 1]

    elif ancestry == "Halfling":
        for i in range(len(halfling)):
            print("%i) %s" % (i + 1, halfling[i]))
        choice = -1
        while not (1 <= choice <= 12):
            try:
                choice = int(input("Type in your chosen ancestry feat: "))
                if not (1 <= choice <= 12):
                    print("Please input an integer between 1 - 12")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 12")
        logging.debug("Chosen ancestry feat: " + halfling[choice - 1])
        return halfling[choice - 1]

    elif ancestry == "Human":
        for i in range(len(human)):
            print("%i) %s" % (i + 1, human[i]))
        choice = -1
        while not (1 <= choice <= 19):
            try:
                choice = int(input("Type in your chosen ancestry feat: "))
                if not (1 <= choice <= 19):
                    print("Please input an integer between 1 - 19")
                    continue
                break
            except ValueError:
                print("Please input an integer between 1 - 19")
        logging.debug("Chosen ancestry feat: " + human[choice - 1])
        return human[choice - 1]


# assert choose_ancestry_feat("Dwarf") == "Avenge In Glory", \
#     "Expecting Avenge In Glory when option 1 is chosen under the Dwarf ancestry"

# assert choose_ancestry_feat("Dwarf") == "Grim Insight", \
#     "Expecting Avenge In Glory when option 1 is chosen under the Dwarf ancestry"

def choose_background():
    """
    Get the user's choice of background

    Prompts the user for their background choice. Spelling must exactly match the options in the backgrounds[] list

    Parameters:
    ----------
    None

    Returns:
    ----------
    String
        The chosen background as an index of the appropriate backgrounds list
    """
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
    print("⮘━━━━━━━Choose your background━━━━━━━⮚")
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
    logging.debug("Chosen background: " + backgrounds[index])
    return backgrounds[index]

# assert choose_background() == "Barkeep", "Expecting barkeep to be returned when barkeep is chosen"
# assert choose_background() == "Traveler", "Expecting barkeep to be returned when barkeep is chosen"


def choose_class():
    """
    Gets the user's choice of class

    Prompts the user for their class of choice, based on a list of 12 classes

    Parameters:
    ----------
    None

    Returns:
    ----------
    String
        The chosen class as an index of the appropriate classes list
    """
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
    print("⮘━━━━━━━Choose your class━━━━━━━⮚")

    # prints to the user all available options
    for i in range(len(classes)):
        print("%i) %s" % (i + 1, classes[i]))

    # Repeatedly prompt the user until they an integer within the range of options
    choice = -1
    while not (1 <= choice <= 12):
        try:
            choice = int(input("Type in your chosen ancestry: "))
            if not (1 <= choice <= 12):
                print("Please input an integer between 1 - 12")
                continue
            break
        except ValueError:
            print("Please input an integer between 1 - 12")
    logging.debug("Chosen class: " + classes[choice - 1])
    return classes[choice - 1]


# assert choose_class() == "Wizard", "Expecting wizard to be returned when 12 is selected"
# assert choose_class() == "Rogue", "Expecting wizard to be returned when 12 is selected"


def choose_spells(character_class):
    """
    Gets the user's choice of spells

    Prompts the user for their choice of spells. The user must have a class that can use spells, or else this step is skipped

    Parameters:
    ----------
    character_class: String
        The class of the character object currently being created

    Returns:
    ----------
    List
        The chosen spell embedded in a list

    Raises:
    ------
    TypeError
        if character_class is not a string
    """
    spells = [
        "Acid Splash",
        "Air Bubble",
        "Alarm",
        "Ant Haul",
        "Bane",
        "Bless",
        "Burning Hands",
        "Charm",
        "Chill Touch",
        "Color Spray",
        "Command",
        "Create Water",
        "Dancing Lights",
        "Daze",
        "Detect Alignment",
        "Detect Magic",
        "Detect Poison",
        "Disrupt Undead",
        "Disrupting Weapons",
        "Divine Lance",
        "Electric Arc",
        "Fear",
        "Feather Fall",
        "Fleet Step",
        "Floating Disk",
        "Forbidding Ward",
        "Ghost Sound",
        "Goblin Pox",
        "Grease",
        "Grim Tendrils",
        "Guidance",
        "Gust of Wind",
        "Harm",
        "Heal",
        "Hydraulic Push",
        "Illusory Disguise",
        "Illusory Object",
        "Item Facade",
        "Jump",
        "Know Direction",
        "Light",
        "Lock",
        "Longstrider",
        "Mage Armor",
        "Mage Hand",
        "Magic Aura",
        "Magic Fang",
        "Magic Missile",
        "Magic Weapon",
        "Mending",
        "Message",
        "Mindlink",
        "Negate Aroma",
        "Pass Without Trace",
        "Pest Form",
        "Phantom Pain",
        "Prestidigitation",
        "Produce Flame",
        "Protection",
        "Purify Food and Drink",
        "Ray of Enfeeblement",
        "Ray of Frost",
        "Read Aura",
        "Sanctuary",
        "Shield",
        "Shillelagh",
        "Shocking Grasp",
        "Sigil",
        "Sleep",
        "Soothe",
        "Spider Sting",
        "Spirit Link",
        "Stabilize",
        "Summon Animal",
        "Summon Construct",
        "Summon Fey",
        "Summon Plant or Fungus",
        "Tanglefoot",
        "Telekinetic Projectile",
        "True Strike",
        "Unseen Servant",
        "Ventriloquism"
    ]

    if not isinstance(character_class, str):
        logging.critical("Expecting class to be a string, but found " + str(type(character_class)) + " instead")
        raise TypeError("Expecting class to be a string")

    # These classes cannot choose spells
    invalid_classes = ["ALCHEMIST", "BARBARIAN", "FIGHTER", "MONK", "RANGER", "ROGUE"]
    if character_class.upper() in invalid_classes:
        return

    logging.info("The chosen class " + character_class + " needs to choose spells")

    print("⮘━━━━━━━Choose your spells━━━━━━━⮚")
    print("Due to the amount of spells, it is not feasible to print out all of them. Please refer to the "
          "rule book")
    # Prompts the user until they enter a valid background
    # Input must be spelt correctly, but spaces and capitalization do not matter.
    uppercase_list = [i.replace(" ", "").upper() for i in spells]
    choice = ""
    while choice.replace(" ", "").upper() not in uppercase_list:
        choice = input("Type in your chosen spells (Invalid input will cause another prompt): ")

    # Locates the index of the background the user gave, and return the properly formatted text
    index = -1
    for i in range(len(uppercase_list)):
        if uppercase_list[i] == choice.replace(" ", "").upper():
            index = i
            break
    logging.debug("Chosen spell: " + spells[index])
    return [spells[index]]

# assert choose_spells("Wizard") == ["Heal"], \
#     "Expecting function to correctly return heal when the wizard class is chosen and heal is chosen in selecting spells"

# assert choose_spells("Wizard") == ["Sleep"], \
#     "Expecting function to correctly return heal when the wizard class is chosen and heal is chosen in selecting spells"


def free_boost(stats, boost_options):
    """
    Utility function to let the user choose free ability boosts

    Used to add stats to classes that are eligible for free stat boosts

    Parameters:
    ----------
    stats: dictionary
        Dictionary containing the character's statistics
    boost_options: list
        List containing all available options for boosting

    Returns:
    ----------
    None

    Raises:
    ------
    TypeError
        if stats is not a dictionary
    TypeError
        if boost_options is not a dictionary
    """

    if not isinstance(stats, dict):
        logging.critical("Expected stats to be a dictionary, but found " + str(type(stats)) + " instead")
        raise TypeError("Expected stats to be a dictionary")
    if not isinstance(boost_options, list):
        logging.critical("Expected boost_options to be a list, but found " + str(type(boost_options)) + " instead")
        raise TypeError("Expected stats to be a list")

    user_boost_choice = -1
    while not (1 <= user_boost_choice <= 6):
        try:
            user_boost_choice = int(input("Type in your chosen free ability boost: "))
            if not (1 <= user_boost_choice <= 6):
                print("Please input an integer between 1 - 6")
                continue
            break
        except ValueError:
            print("Please input a integer between 1 - 6")
    logging.debug("Adding 2 points for " + boost_options[user_boost_choice - 1])
    stats[boost_options[user_boost_choice - 1][0:3]] += 2


def buy_items(money):
    """
    Utility function to let the user buy items

    Shop system for allowing the user to buy items using a menu and money system

    Parameters
    ----------
    money: int
        Amount of money user has

    Returns
    -------
    List:
        list of items the player bought

    Raises:
    ------
    TypeError
        if money is not an int
    """
    items_name_with_cost = {
        "Jellyfish Lamp": 2,
        "Pesh": 1,
        "Swim Fins": 5,
        "Archaic Wayfinder": 30,
        "Black Pearl Aeon Stone": 2000,
        "Blessed Tattoo": 90,
        "Final Blade": 40,
    }
    items_name = [
        "Jellyfish Lamp",
        "Pesh",
        "Swim Fins",
        "Archaic Wayfinder",
        "Black Pearl Aeon Stone",
        "Blessed Tattoo",
        "Final Blade",
    ]
    cart = []
    remaining_money = money

    if not isinstance(money, int):
        logging.critical("Expecting money to be an int, but found " + str(type(money)) + " instead")
        raise TypeError("Expecting money to be an int")

    # prints to the user all available options
    print("⮘━━━━━━━Buy items━━━━━━━⮚")
    for i in range(len(items_name)):
        print("%i) %s: %i" % (i + 1, items_name[i], items_name_with_cost[items_name[i]]))

    # Repeatedly prompt the user until they an integer within the range of options
    choice = -1
    while not (1 <= choice <= 7):
        try:
            choice = int(input("Type in the item you would like to purchase (0 to exit): "))
            if choice == 0:
                break
            elif not (1 <= choice <= 7):
                print("Please input an integer between 1 - 7")
                continue
            elif items_name_with_cost[items_name[choice - 1]] > remaining_money:
                print("You don't have enough money for that item!")
                choice = -1  # Resets choice for loop to keep running
                continue
            remaining_money -= items_name_with_cost[items_name[choice - 1]]  # Deduct money
            print("Purchased %s x1. Remaining money (in gp): %i" % (items_name[choice - 1], remaining_money))
            cart.append(items_name[choice-1])  # Add item to cart
            choice = -1  # Resets choice for loop to keep running
        except ValueError:
            print("Please input an integer between 1 - 7")

    logging.debug(str(len(cart)) + " items were bought")
    logging.debug("There is " + str(remaining_money) + " gp remaining")
    return [cart, remaining_money]


# assert buy_items(40) == [["Final Blade"], 0], \
#     "Expecting only final blade to be in inventory when only one final blade is purchased"

# assert buy_items(40) == [["Final Blade, Pesh"], 0], \
#     "Expecting only final blade to be in inventory when only one final blade is purchased"


def view_characters(characters):
    """
    Displays every created character by their name

    Parameters:
    ----------
    characters: list
        List of characters being iterated through for collecting data

    Returns:
    ----------
    None

    Raises:
    ------
    TypeError
        if characters is not a list
    """

    if not isinstance(characters, list):
        logging.critical("Expecting characters to be a list, but found " + str(type(characters)) + " instead")
        raise TypeError("Expecting characters to be a list")

    if len(characters) == 0:
        print("You haven't created anything yet!")
        return
    logging.debug("Viewing characters, " + str(len(characters)) + " characters have been created")
    for i in range(len(characters)):
        print("%i) %s" % (i + 1, characters[i].name))


def character_details(character):
    """
    Gets detailed statistics for the given character

    Takes character object and prints its attributes

    Parameters:
    character: list
        List of characters being iterated through for collecting data

    Returns:
    None

    Raises:
    ------
    TypeError
        if character is not a list
    """

    if not isinstance(character, list):
        logging.critical("Expecting list, but found" + str(type(character)) + " instead")
        raise TypeError("Expecting character to be a list")

    character_name = input("Please input the name of the character (Must be exact same): ")
    logging.info("Getting character details for " + character_name)
    for i in range(len(character)):
        if character[i].name.upper() == character_name.upper():
            print("Name: %s" % character[i].name)
            print("Age: %i" % character[i].age)
            print("Height: %i" % character[i].height)
            print("Level: %i" % character[i].level)
            print("Gold: %i" % character[i].gold)
            print("Ancestry: %s" % character[i].ancestry)
            print("Heritage: %s" % character[i].heritage)
            print("Ancestry Feat: %s" % character[i].ancestry_feat)
            print("Background: %s" % character[i].background)
            print("Class: %s" % character[i].character_class)
            if character[i].spells is None:
                print("Spells: None")
            else:
                print("Spells: %s" % ", ".join(character[i].spells))
            print("Str: %i" % character[i].stats["Str"])
            print("Dex: %i" % character[i].stats["Dex"])
            print("Con: %i" % character[i].stats["Con"])
            print("Int: %i" % character[i].stats["Int"])
            print("Wis: %i" % character[i].stats["Wis"])
            print("Cha: %i" % character[i].stats["Cha"])
            if character[i].backpack is None:
                print("Items: None")
            else:
                print("Items: %s" % ", ".join(character[i].backpack))
            return
    print("A character with that name does not exist")


def menu(characters):
    """
    Displays menu

    Allows the user to choose what they want to do next. Nested within a infinite loop until user exits

    Parameters:
    ----------
    character: list
        List of characters being iterated through for collecting data

    Returns:
    ----------
    None

    Raises:
    ------
    TypeError
        if character is not a list
    """
    if not isinstance(characters, list):
        logging.critical("Expecting list, but found" + str(type(characters)) + " instead")
        raise TypeError("Expecting character to be a list")

    choice = ""
    while choice != '1' and choice != '2' and choice != '3' and choice != '4':
        choice = input("(1) Create new character | (2) View created characters | (3) View Character Details | "
                       "(4) Exit Program: ")
    if choice == "4":
        logging.info("Exiting program")
        sys.exit()
    elif choice == "3":
        character_details(characters)
        menu(characters)
    elif choice == "2":
        view_characters(characters)
        menu(characters)


def progress_bar():
    """
    Cool progress bar to make the user think the code actually does something

    Parameters:
    ----------
    None

    Returns:
    ----------
    None
    """
    print("(█) 10%")
    time.sleep(1 / 10)
    print("Enumerating objects")
    time.sleep(1 / 10)
    print("Counting objects")
    time.sleep(1 / 10)
    print("(████) 40%")
    time.sleep(1 / 10)
    print("Delta compression")
    time.sleep(1 / 10)
    print("(███████) 70%")
    time.sleep(1 / 10)
    print("Compressing objects")
    time.sleep(1 / 10)
    print("(█████████) 90%")
    time.sleep(1 / 10)
    print("Writing objects")
    time.sleep(1 / 10)
    print("Resolving deltas")
    time.sleep(1 / 10)
    print("(██████████) 100%")
    time.sleep(1 / 10)
    print("\nCharacter creation complete!")


# Main driver code
def main():
    # Avoids the use of global variables
    characters = []
    default_stats = {
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
        logging.info("Starting to choose ancestry")
        local_ancestry = choose_ancestry(default_stats)
        logging.info("Completed choosing ancestry")
        print("")
        logging.info("Starting to choose heritage")
        local_heritage = choose_heritage(local_ancestry)
        logging.info("Completed choosing heritage")
        print("")
        logging.info("Starting to choose ancestry feat")
        local_ancestry_feat = choose_ancestry_feat(local_ancestry)
        logging.info("Completed choosing ancestry feat")
        print("")
        logging.info("Starting to choose background")
        local_background = choose_background()
        logging.info("Completed choosing background")
        print("")
        logging.info("Starting to choose class")
        local_character_class = choose_class()
        logging.info("Completed choosing class")
        print("")
        logging.info("Starting to choose spells")
        local_character_spells = choose_spells(local_character_class)
        logging.info("Completed choosing spells")
        print("")
        logging.info("Starting to buy items")
        backpack_money_tuple = buy_items(15)
        logging.info("Completed buying items")
        local_backpack = backpack_money_tuple[0]
        local_money = backpack_money_tuple[1]
        characters.append(Character(local_name,
                                    local_age,
                                    local_height,
                                    1,
                                    local_money,
                                    local_ancestry,
                                    local_heritage,
                                    local_ancestry_feat,
                                    local_background,
                                    local_character_class,
                                    local_character_spells,
                                    local_backpack,
                                    default_stats))
        progress_bar()
        # Sort characters by name lexicographically
        characters.sort(key=lambda x: x.name)


main()

