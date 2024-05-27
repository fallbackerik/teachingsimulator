# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Teacher = Character("Teacher Eileen", color="#c8ffc8")
define Bertram = Character("Bertram", color="ffc8c8")

# Images
image bg room = "assets/bg01-hallway.jpg"

image teacher idle = Composite(
    (556, 1000),
    (0, 0), "assets/fm01/fm01-body.png",
    (0, 0), "assets/fm01/fm01-eyes-smile.png",
    (0, 0), "assets/fm01/fm01-mouth-smile00.png",
)

image bertram idle = Composite(
    (556, 1000),
    (0, 0), im.Flip("assets/m01/m01-body.png", horizontal=True),
    (0, 0), im.Flip("assets/m01/m01-eyes-smile.png", horizontal=True),
    (0, 0), im.Flip("assets/m01/m01-mouth-smile00.png", horizontal=True),
)

image teacher hover = Composite(
    (556, 1000),
    (0, 0), "assets/fm01/fm01-body.png",
    (0, 0), "assets/fm01/fm01-eyes-wow.png",
    (0, 0), "assets/fm01/fm01-mouth-wow.png",
)

image bertram hover = Composite(
    (556, 1000),
    (0, 0), im.Flip("assets/m01/m01-body.png", horizontal=True),
    (0, 0), im.Flip("assets/m01/m01-eyes-wow.png", horizontal=True),
    (0, 0), im.Flip("assets/m01/m01-mouth-wow.png", horizontal=True),
)

# The game starts here.

label start:
    scene bg room

    "At the beginning of an exciting new day..."

    show teacher idle at left with dissolve
    pause

    Teacher "Hello [Bertram]! Did you rest well?"

    show bertram idle at right with dissolve
    pause

    Bertram "I did, thank you! And you, [Teacher]?"
    Teacher "Same, thanks for asking."
    extend "Alright, let's continue the exercises."

    Bertram "Sounds good, let's keep going..."
    pause

    window hide
    pause

    hide teacher with dissolve
    pause

    hide bertram with dissolve
    pause

    return
