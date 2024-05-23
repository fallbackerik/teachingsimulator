# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")
define b = Character("Bertram", color="ffc8c8")

# Images
image bg room = "bg.png"
# TODO adapt coordinates
image eileen = Composite(
    (467, 946),
    (0, 0), "assets/fm01/fm01-body.png",
    (0, 0), "assets/fm01/fm01-eyes-smile.png",
    (0, 0), "assets/fm01/fm01-mouth-smile00.png",
)

# TODO change direction of character so both characters face each other
# TODO adapt coordinates
image bertram = Composite(
    (467, 946),
    (0, 0), "assets/m01/m01-body.png",
    (0, 0), "assets/m01/m01-eyes-smile.png",
    (0, 0), "assets/m01/m01-mouth-smile00.png",
)


# The game starts here.

label start:
    scene bg room

    show eileen happy at left with dissolve

    e "Hello there! How are you today?"

    show bertram happy at right with dissolve

    b "I'm good, thank you! And you?"
    e "I'm doing well, thanks for asking."
    b "Alright, let's get back to the main menu."

    return

# Main menu customizations

init -2:
    # buttons
    style mm_button_text:
        size 40

    # custom main menu
    screen main_menu():
        tag menu

        window:
            style "mm_window"

        frame:
            style_group "mm_window"

            has vbox

            textbutton _("Start") action Start()
            #greyed out for now
            textbutton _("Options") action None()
            textbutton _("Quit") action Quit()

    # add main menu to game
    label main_menu:
        call screen main_menu
        return

