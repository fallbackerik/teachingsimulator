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
