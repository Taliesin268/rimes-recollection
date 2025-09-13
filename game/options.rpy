## This file contains options that can be changed to customize your Ren'Py
## game. It only contains the most common options... there is quite a bit more
## customization you can do.

define config.name = _("Rimes & Recollection")

define gui.show_name = True

define config.version = "1.0"

define gui.about = _p("""
A visual novel chronicling the epic adventures of our D&D party.

Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].

[renpy.license!t]
""")

define build.name = "RimesRecollection"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.after_load_transition = fade
define config.end_game_transition = fade

define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 0

default preferences.afm_time = 15

define config.save_directory = "RimesRecollection-1615846074"

define config.window_icon = "gui/window_icon.png"

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')