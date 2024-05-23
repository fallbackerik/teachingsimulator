init offset = -2

init python:
  gui.init(1920, 1080)


## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#000000'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#aaaaaa'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#888888'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#000000'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#555555'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#aaaaaa7f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = '#666666'
define gui.hover_muted_color = '#999999'

## The colors used for dialogue and menu choice text.
define gui.text_color = '#404040'
define gui.interface_text_color = '#404040'


## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = "DejaVuSans.ttf"

## The font used for character names.
define gui.name_text_font = "DejaVuSans.ttf"

## The font used for out-of-game text.
define gui.interface_text_font = "DejaVuSans.ttf"

## The size of normal dialogue text.
define gui.text_size = 33

## The size of character names.
define gui.name_text_size = 45

## The size of text in the game's user interface.
define gui.interface_text_size = 33

## The size of labels in the game's user interface.
define gui.label_text_size = 36

## The size of text on the notify screen.
define gui.notify_text_size = 24

## The size of the game's title.
define gui.title_text_size = 75

## The images used for the main and game menus.
define gui.main_menu_background = "assets/bg02-dorm.jpg"
define gui.game_menu_background = "assets/bg02-dorm.jpg"


## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define gui.textbox_height = 278

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 1.0


## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define gui.name_xpos = 360
define gui.name_ypos = 0

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.0

## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define gui.namebox_width = None
define gui.namebox_height = None

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## If True, the background of the namebox will be tiled, if False, the
## background of the namebox will be scaled.
define gui.namebox_tile = False


## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 1116

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0
