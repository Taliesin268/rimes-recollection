# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Define main party members - adjust names and colors as needed
define dm = Character("DM", color="#c8ffc8")
define narrator = Character(None, kind=nvl)

# Add your party members here - example characters:
define pc1 = Character("Character 1", color="#c8c8ff")
define pc2 = Character("Character 2", color="#ffc8c8")
define pc3 = Character("Character 3", color="#ffffc8")
define pc4 = Character("Character 4", color="#ffc8ff")

# The game starts here.
label start:

    scene bg tavern
    with fade

    "Welcome to the chronicles of our D&D adventures!"

    "This visual novel will document the epic tales of our party's journey through mysterious lands, dangerous dungeons, and unforgettable encounters."

    dm "Gather 'round, adventurers. Our tale begins in a bustling tavern where fate would bring together an unlikely group of heroes..."

    "Session 1 will be added here..."

    # Placeholder menu for navigation
    menu:
        "Begin Session 1":
            jump session1

        "Character Backgrounds":
            jump character_backgrounds

        "Settings":
            jump preferences

    return

# Session 1 content placeholder
label session1:
    scene bg forest
    with dissolve

    dm "Your first adventure begins as you leave the safety of the town and venture into the Whispering Woods..."

    "To be continued..."

    return

# Character backgrounds placeholder
label character_backgrounds:
    "Here you can learn about each party member's backstory and motivations."

    # Add character introductions here

    jump start

# Jump to Ren'Py's built-in preferences screen
label preferences:
    call screen preferences
    jump start