# Rime's Recollection - D&D Campaign Chronicles
# Session 66: The Righteous Grove

# Character Definitions
define dm = Character("DM", color="#c8ffc8")
define narrator = Character(None, color="#ffffff")

# Party Characters
define thrall = Character("Thrall", color="#8b4a9c")
define granite = Character("Granite", color="#8b7355")
define harold = Character("Harold", color="#4a90e2")
define ronin = Character("Ronin", color="#cc5500")
define rime = Character("Rime", color="#87ceeb")  # Echo Form

# NPCs
define mouth = Character("The Mouth", color="#daa520")  # Voice of Rysen
define rysen = Character("Rysen", color="#ffd700")
define ccillian = Character("C'cillian", color="#9acd32")
define shallar = Character("Shallar", color="#d2b48c")
define tsheek = Character("T'sheek", color="#dc143c")
define helios = Character("Helios", color="#ff4500")

# Groups
define children_of_reath = Character("Children of Reath", color="#98fb98")
define host_family = Character("Host Family", color="#dda0dd")

# Main Menu
label start:
    scene bg room
    with fade

    menu:
        "What would you like to experience?"

        "Session 66: The Righteous Grove":
            jump session_66

        "Other Sessions":
            "No other sessions available yet."
            jump start

        "Quit":
            return

# Session 66 Main Entry
label session_66:
    scene black
    with fade

    "Session 66: The Righteous Grove"
    "We return to our adventure at a celebration with the Reath. A feast is underway, and the party are trying their best to blend in."

    jump session66_scene1

# Scene 1: Reath Feast — Arrival & The Mouth
label session66_scene1:
    scene bg bonfire  
    with dissolve

    "Thrall asks the mouth who the oldest person in Reath is."

    jump session66_scene2

# Scene 2: The Walk Away From the Music
label session66_scene2:
    scene bg forest_path
    with dissolve

    "Thrall walks with The Mouth away from the music to find the Elder - meeting C'Cillian along the way."

    jump session66_scene3

# Scene 3: Elder's Chamber (first visit)
label session66_scene3:
    scene black 
    with dissolve

    "Thrall meets the elder Shallar, who speaks through the Mouth."

    jump session66_scene4

# Scene 4: Return to Feast → Revelry Shifts to Dancing
label session66_scene4:
    scene bg bonfire
    with dissolve

    "One of the Reath cast a spell to light the bonfire, and dancing commences."

    jump session66_scene5

# Scene 5: Rime's Warning & The Split
label session66_scene5:
    scene bg bonfire
    with dissolve

    "Rime confides in Thrall that he senses danger. The party splits up to investigate separately."

    jump session66_scene6

# Scene 6: Reconnaissance Menu System
label session66_scene6:
    scene bg bonfire
    with dissolve

    menu:
        "6A) Thrall's Second Visit to the Elder":
            jump session66_scene6a

        "6B) Granite's Throne-Room Reconnaissance":
            jump session66_scene6b

        "6C) Harold's Search":
            jump session66_scene6c

        "Continue":
            jump session66_scene7

# Scene 6A: Thrall's Second Visit to the Elder
label session66_scene6a:
    scene black 
    with dissolve

    "Thrall returns to Shallar, and gets C'cillian's permission to enter and speak with her."

    jump session66_scene6

# Scene 6B: Granite's Throne-Room Reconnaissance
label session66_scene6b:
    scene bg throne_room 
    with dissolve

    "Searching for T'sheek and the Titansbane Maul; Granite discovers the caverns, but with no obvious entrance"

    jump session66_scene6

# Scene 6C: Harold's Search
label session66_scene6c:
    scene bg reath_home
    with dissolve

    "Harold is welcomed and given the baby to care for, but eventually they find Harold suspicious and ask him to leave"

    jump session66_scene6

# Scene 7: Convergence on T'sheek
label session66_scene7:
    scene bg forest_path
    with dissolve

    "Granite eavesdrops: T'sheek + unseen ally plan to kill Rysen tonight"

    jump session66_scene8

# Scene 8: Regroup at the Dancefloor & Underground Escape Attempt
label session66_scene8:
    scene bg bonfire
    with dissolve

    "The group reconvene, then move to dig and descend underground to slip away"

    jump session66_scene9

# Scene 9: C'cillian's Interception & The Keyword
label session66_scene9:
    scene bg cavern_entrance  # Placeholder - will be bg_caverns or underground
    with dissolve

    "C'cillian grabs Granite, explains the plan in Common, gives the keyword 'revelry.' Party returns to the dance floor to set the stage"

    jump session66_scene10

# Scene 10: The Revelation: Time Stop & The Duel
label session66_scene10:
    scene bg bonfire
    with dissolve

    "Brief dancing; T'sheek halts the revelry; Helios stops time and delivers his speech; blades clash with Rysen to close the session"

    menu:
        "Return to Main Menu":
            jump start

        "Quit":
            return
