# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define characters.teacher = Character("Teacher Eileen", color="#c8ffc8")
define characters.bertram = Character("Bertram", color="ffc8c8")

# Images
image bg room = "assets/bg01-hallway.jpg"

image eileen idle = Composite(
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

image eileen hover = Composite(
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

    show characters.teacher at left with dissolve
    pause

    teacher "Hello [bertram]! Did you rest well?"

    show bertram at right with dissolve
    pause

    bertram "I did, thank you! And you, [teacher]?"
    teacher "Same, thanks for asking."
    extend "Alright, let's continue the exercises."

    bertran "Sounds good, let's keep going..."
    pause

    hide teacher with dissolve
    pause

    hide bertram with dissolve
    pause

    return
