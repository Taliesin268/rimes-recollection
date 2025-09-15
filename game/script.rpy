# Rime's Recollection - D&D Campaign Chronicles
# Session 66: The Righteous Grove

# Character Definitions

# Party Characters
define thrall = Character("Thrall", color="#6b8e23")
define granite = Character("Granite", color="#8b7355")
define harold = Character("Harold", color="#4a90e2")
define ronin = Character("Ronin", color="#ffffe0")
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

    "Session 66: The Righteous Grove" "We return to our adventure amidst a celebration with the Reath. Laughter and music fill the air as a feast is shared, and the party does their best to move in harmony rather than risk discord."

    jump session66_scene1

# Scene 1: Reath Feast — Arrival & The Mouth
label session66_scene1:
    scene bg bonfire
    with dissolve

    "Thrall asks the Mouth how old the people of this place are. The Mouth offers to introduce him to one of the elders."

    jump session66_scene2

# Scene 2: The Walk Away From the Music
label session66_scene2:
    scene bg forest_path
    with dissolve

    "The music and laughter thin as they leave the celebration. A tent appears ahead, marked with ritual sigils, candles, incense, and wind-chimes."

    "C'cillian — the one once invited into Thrall's lamp — stands guard, casually eating berries. Chains and whips hang on him like ornaments."

    "C'cillian and the Mouth trade a few curious words in Reath that Thrall cannot understand. At the entrance, C'cillian gives Thrall a reassuring wink."

    "Immaculate furs line the threshold, pristine as new snow. Thrall is told he must walk in the presence of the elder — any magic nearby could be dangerous."

    "They undergo a more thorough cleansing than before, body and spirit both, then approach the flap."

    mouth "Their name is Shallar. They will be pleased to meet you."

    jump session66_scene3

# Scene 3: Elder's Chamber (first visit)
label session66_scene3:
    scene black
    with dissolve

    "Inside: pillars, charcoal etchings, layered iconography. A shrine of tree-like supports cradles a loosely human head."

    "Age droops every feature; bones knit together with the barest suggestion of a body, all of it clinging to a heart."

    "As Thrall steps in, he hears the dry crunch of eyelids prying open."

    thrall "How old are you?"

    "The elder rasps. The Mouth leans close to read lips and translate."

    mouth "Shallar is forty-eight years old."

    thrall "Is she comfortable?"

    mouth "She does not have the means to be uncomfortable."

    thrall "Must be nice… Wow, Mister Mouth, this one's just for you. Is this getting worse for them?"

    mouth "She will continue to worsen. This is what Rysen's bargain brought — to trade our bodies for our might."

    thrall "Did your people agree?"

    mouth "It has been the price of our safety and peace."

    "Thrall watches, weighing whether the Mouth translates faithfully. The pause could be effort — or invention."

    thrall "Mister Mouth — do you agree with the decision?"

    mouth "I am the voice of Rysen. Of course. It was the only way to keep my children safe."

    thrall "From what?"

    mouth "From the other kingdoms."

    mouth "We have chosen to remove ourselves from the struggle of power."

    thrall "Is it reversible? If you wanted to?"

    mouth "It was a pact with our gods, and thus it would only be changeable should the gods decide."

    thrall "If the rest of the world became friends, would you reverse this?"

    mouth "If I were to rule Miltaur, the gods would see fit to reverse it."

    thrall "So, if the ruler of Reath ruled Miltaur, it would be reversed?"

    mouth "If Miltaur were united, it would be reversed."

    thrall "Do you like your gods?"

    "Shallar stirs for the first time; with effort, remnants of muscle try to turn her head."

    mouth "Shallar says the gods are. It is no matter of love or hate. You could no more hate the sun or the wind."

    thrall "Why are the Reath gods different from the others?"

    mouth "They are not. All gods are one. We worship them in a different form. The gods of Miltaur, of Zeterith, of the Serene Isles — they are the same. Known by different names, seen with different faces, worshipped in different ways."

    thrall "I will go now. Tell Shallar I respect her greatly and want to help her."

    "The Mouth translates. Shallar forces out a sound."

    mouth "She asks that you stay a moment longer."

    thrall "Did she want you to remain?"

    mouth "No."

    "The Mouth steps out and lets the curtain fall. Thrall lingers at the threshold, leaning in as Shallar gathers a final whisper."

    shallar "Shar eular mialagra deshoon."

    "Thrall wheels around and sprints back to the dance floor, the drums and firelight rushing up to meet him."

    jump session66_scene4

# Scene 4: Return to Feast → Revelry Shifts to Dancing
label session66_scene4:
    scene bg bonfire
    with dissolve

    thrall "Shar eular mialagra deshoon! What does it mean?!"

    rime "My flesh burns the gods."

    rime "This is no passive devotion. It's an invocation — a call for the gods themselves to walk upon Miltaur."

    "Thrall's Thoughts" "The tales said the Reath yielded their bodies for divine strength. But this sounds different: their flesh, their suffering, offered not merely as vessels… but as summoning."

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
