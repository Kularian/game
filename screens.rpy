################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language
    #kerning 0.2
    line_spacing -5.3
    line_leading -8

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        if tbnarrator == 1:
            style "narrator"
            id "narrator"
        else:
            style "window"
            id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox4.png", xalign=0.5, yalign=1.0)

style narrator:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textboxn.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
        properties gui.text_properties("dialogue")

        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos
        #yalign 0.5
        line_spacing 19

        adjust_spacing False

style nsay_dialogue is say_dialogue:
        ypos 600

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.3
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

#    imagemap:
#        auto "gui/menu2_%s.png"
    add gui.main_menu_background

#    hotspot (154, 188, 265, 124) action Start()
#    hotspot (44, 374, 336, 117) action Jump("loadsave")
#    hotspot (173, 565, 340, 103) action Jump("preferences")
#    hotspot (40, 759, 315, 103) action Jump("extra")

    imagebutton xpos 120 ypos 159 action Start() idle "gui/NewGameBase.png" hover "gui/NewGameHover.png"
    imagebutton xpos 22 ypos 359 action Jump("loadsave") idle "gui/LoadGameBase.png" hover "gui/LoadGameHover.png"
    imagebutton xpos 171 ypos 542 action Jump("preferences") idle "gui/OptionsBase.png" hover "gui/OptionsHover.png"
    imagebutton xpos 37 ypos 743     action Jump("extra") idle "gui/ExtraBase.png" hover "gui/ExtraHover.png"
    #imagebutton xpos 835 ypos 1000 action Quit(confirm=not main_menu) idle "gui/QuitBase.png" hover "gui/QuitHover.png"

    timer 60.0 action Jump("Introcutscenes")

    ## This empty frame darkens the main menu.
#    frame:
#        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
#    use navigation

#    if gui.show_name:

#        vbox:
#            style "main_menu_vbox"

#            text "[config.name!t]":
#                style "main_menu_title"

#            text "[config.version]":
#                style "main_menu_version"


#style main_menu_frame is empty
#style main_menu_vbox is vbox
#style main_menu_text is gui_text
#style main_menu_title is main_menu_text
#style main_menu_version is main_menu_text

#style main_menu_frame:
#    xsize 420
#    yfill True

#    background "gui/overlay/main_menu.png"

#style main_menu_vbox:
#    xalign 1.0
#    xoffset -30
#    xmaximum 1200
#    yalign 1.0
#    yoffset -30

#style main_menu_text:
#    properties gui.text_properties("main_menu", accent=True)

#style main_menu_title:
#    properties gui.text_properties("title")

#style main_menu_version:
#    properties gui.text_properties("version")


## Pre Menu Screen #############################################################

screen pre_menu:
    add "gui/menu1.png"
    imagebutton action Jump("main_menu") idle "gui/Menu1press.png" hover "gui/Menu1press.png" at anybuttonfade
    timer 60.0 action Jump("Introcutscenes")

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


## Custom Screens ###############################################################

## Location #####################################################################

screen header:
    zorder 10
#    add "gui/location2.png"
    add "gui/watch.png" ypos 0
#    add "gui/flair.png"
#    text "[location]" at loc
    text "After School" font "Fonts/digital-7.ttf" size 42 at phase1
    text "09/18" font "Fonts/digital-7.ttf" size 42 at phase2

## Bottom ######################################################################

screen Flair:
    zorder 100
    add "gui/flair.png"

## Choices #####################################################################

screen choices():
    zorder 15
    add "gui/textboxn.png"
    if lines == 1:
        text "[choicetext]" at choicetext
    elif lines == 2:
        text "[choicetext]" at choicetext2 line_spacing 19
    fixed:
        imagebutton idle "gui/choices.png" hover "gui/choicesb.png" action Return(1) xpos 600 ypos 275
        text _("[choice1]") xpos 670 ypos 310
    fixed:
        imagebutton idle "gui/choices.png" hover "gui/choicesb.png" action Return(2) xpos 600 ypos 450
        text _("[choice2]") xpos 670 ypos 485

## St. Hermelin #############################################################

screen HermelinFloor1:
    imagemap:
        idle "maps/HermelinFloor1.png"
        hover "maps/HermelinFloor1b.png"
        ground "maps/HermelinFloor1.png"

        hotspot (162, 224, 513, 186) action Jump("label002") #Class 1-2
        hotspot (708, 227, 511, 180) action Jump("label003") #Class 1-3
        hotspot (1249, 224, 510, 184) action Jump("label004") #Class 1-4
        hotspot (160, 434, 514, 187) action Jump("label005") #Class 1-6
        hotspot (704, 435, 517, 184) action Jump("label006") #Courtyard
        hotspot (1246, 437, 514, 189) action Jump("label007") #Teacher's Lounge
        hotspot (157, 642, 521, 191) action Jump("label008") #Principal's Office
        hotspot (704, 641, 520, 192) action Jump("label001") #Infirmary
        hotspot (1248, 644, 517, 189) action Jump("label009") #1F Passageway
        imagebutton xpos 30 ypos 435 idle "maps/MoveLeft.png" hover "maps/MoveLeftb.png" action Jump("label033") #Entryway
    imagebutton xpos 1800 ypos 435 idle "maps/MoveRight.png" hover "maps/MoveRightb.png" action Jump("callSportsBuilding") #SportsBuilding
    imagebutton xpos 925 ypos 50 idle "maps/StairUp.png" hover "maps/StairUpb.png" action Jump("callHermelinFloor2") #2f

screen HermelinFloor2:
    imagemap:
        idle "maps/HermelinFloor2.png"
        hover "maps/HermelinFloor2b.png"
        ground "maps/HermelinFloor2.png"

        hotspot (165, 227, 506, 178) action Jump("label018") #Class 2-1
        hotspot (708, 229, 507, 179) action Jump("label019") #Class 2-2
        hotspot (1251, 226, 505, 182) action Jump("label020") #Class 2-4
        hotspot (165, 437, 506, 182) action Jump("label021") #Class 2-5
        hotspot (1249, 435, 511, 183) action Jump("label022") #Cafeteria
        hotspot (707, 435, 509, 178) action Jump("label023") #Home Ec Room
        hotspot (706, 646, 512, 180) action Jump("label024") #Empty Classroom | Reiji

    imagebutton xpos 925 ypos 50 idle "maps/StairUp.png" hover "maps/StairUpb.png" action Jump("callHermelinFloor3") #3f
    imagebutton xpos 925 ypos 850 idle "maps/StairDown.png" hover "maps/StairDownb.png" action Jump("callHermelinFloor1") #1f

screen HermelinFloor3:
    imagemap:
        idle "maps/HermelinFloor3.png"
        hover "maps/HermelinFloor3b.png"
        ground "maps/HermelinFloor3.png"

        hotspot (163, 226, 510, 178) action Jump("label026") #Class 3-1
        hotspot (707, 229, 509, 179) action Jump("label027") #Class 3-3
        hotspot (1251, 230, 508, 177) action Jump("label028") #Class 3-6
        hotspot (160, 438, 508, 178) action Jump("label029") #Class 3-7
        hotspot (704, 434, 514, 181) action Jump("label030") #Library
        hotspot (1251, 437, 503, 179) action Jump("label031") #Student Council
        hotspot (706, 645, 509, 182) action Jump("label032") #Art Room

    imagebutton xpos 925 ypos 850 idle "maps/StairDown.png" hover "maps/StairDownb.png" action Jump("callHermelinFloor2") #2f

screen HermelinSportsBuilding:
    imagemap:
        idle "maps/SportsBuilding.png"
        hover "maps/SportsBuildingb.png"
        ground "maps/SportsBuilding.png"

        hotspot (165, 227, 503, 181) action Jump("label009") #1F Passageway
        hotspot (708, 226, 507, 182) action Jump("label011") #Gymnasium
        hotspot (1252, 226, 507, 182) action Jump("label012") #Drama Club
        hotspot (163, 435, 507, 184) action Jump("label013") #Boxing Club
        hotspot (708, 435, 508, 181) action Jump("label014") #Archery Club
        hotspot (1249, 437, 510, 176) action Jump("label015") #Fencing Club
        hotspot (707, 645, 506, 180) action Jump("label016") #Ballet Club

    imagebutton xpos 30 ypos 435 idle "maps/MoveLeft.png" hover "maps/MoveLeftb.png" action Jump("callHermelinFloor1") #1F

## Mikage-Cho #############################################################

screen OverworldMap1:
    imagemap:
        auto "gui/overworldmap1_%s.png"
        hover "gui/overworldmap1.png"
        selected_idle "gui/overworldmap1.png"
        selected_hover "gui/overworldmap1.png"
        ground "gui/overworldmap1_%s.png"

        hotspot (812, 43, 311, 227) action Jump("label040") #Mikage Sun Mall
        hotspot (31, 163, 332, 241) action Jump("label038") #Alaya Shrine
        hotspot (496, 247, 321, 264) action Jump("label033") #School
        hotspot (1103, 249, 317, 248) action Jump("label048") #Historical Society
        hotspot (1562, 173, 290, 229) action Jump("label066") #Agastya Tree
        hotspot (22, 412, 331, 234) action Jump("label035") #Kaneda mansion
        hotspot (1592, 405, 297, 221) action Jump("label051") #Mikage Ruins
        hotspot (533, 519, 214, 219) action Jump("label037") #Yin-Yan
        hotspot (1120, 522, 284, 219) action Jump("label039") #Esumi Clinic
        hotspot (101, 639, 352, 242) action Jump("label036") #Himeno Residence
        hotspot (1509, 668, 304, 211) action Jump("label050") #Police Station
        hotspot (833, 463, 260, 225) action Jump("label046") #Velvet Room
        hotspot (793, 794, 303, 268) action Jump("wardonetotwo")

screen OverworldMap2:
    imagemap:
        auto "gui/overworldmap2_%s.png"
        hover "gui/overworldmap2.png"
        selected_idle "gui/overworldmap2.png"
        selected_hover "gui/overworldmap2.png"
        ground "gui/overworldmap2_%s.png"

        hotspot (109, 191, 302, 220) action Jump("label064") #Esumi Clinic
        hotspot (1485, 183, 318, 257) action Jump("label065") #Arcade
        hotspot (114, 613, 303, 243) action Jump("label066") #Agastya Tree
        hotspot (500, 490, 303, 235) action Jump("label052") #Joy Street
        hotspot (1102, 497, 318, 243) action Jump("hospitalcheck") #Hospital
        hotspot (1466, 590, 352, 210) action Jump("label063") #Abandoned Factory
        hotspot (793, 794, 303, 268) action Jump("label062") #Sebec
        hotspot (817, 371, 269, 227) action Jump("label059") #Velvet Room
        hotspot (835, 0, 259, 210) action Jump("wardtwotoone")

## Mikage Sun Mall #############################################################

screen MikageSunMall:
    imagemap:
        idle "mikagesunmall.png"
        hover "mikagesunmall.png"
        ground "mikagesunmall.png"

        hotspot (266, 29, 279, 368) action Jump("label041") #sennen mannen-do
        hotspot (548, 29, 268, 368) action Jump("label042") #peace diner
        hotspot (993, 29, 324, 370) action Jump("label043") #rosacandida
        hotspot (1321, 662, 317, 375) action Jump ("label044") #satomi tadashi
        hotspot (998, 659, 317, 381) action Jump ("label045") #Judgment 1999
        hotspot (549, 661, 267, 379) action Jump ("label046") #Velvet Room
        hotspot (278, 664, 267, 375) action Jump ("label047") #Agastya Tree
        hotspot (74, 402, 198, 250) action Jump ("calloverworld")
        hotspot (1641, 404, 169, 253) action Jump ("calloverworld")

## Joy Street Mall #############################################################

screen JoyStreetMall:
    imagemap:
        idle "joystreetmall.png"
        hover "joystreetmall.png"
        ground "joystreetmall.png"

        hotspot (1532, 744, 233, 201) action Jump ("label053") #Rosa Candida
        hotspot (1532, 328, 233, 202) action Jump ("label054") #Sennen Mannen-Do
        hotspot (1533, 128, 232, 200) action Jump ("label055") #Yin & Yan
        hotspot (1046, 128, 229, 198) action Jump ("label056") #Peace Diner
        hotspot (1046, 332, 228, 195) action Jump ("label057") #Satomi Tadashi
        hotspot (1043, 746, 232, 204) action Jump ("label058") #Esumi Clinic
        hotspot (581, 329, 231, 200) action Jump ("label059") #Velvet Room
        hotspot (581, 746, 234, 198) action Jump ("label060") #Agastya Tree
        hotspot (348, 746, 233, 201) action Jump ("label061") #Judgment 1999
        hotspot (4, 530, 268, 213) action Jump ("calloverworld")
        hotspot (1275, 950, 256, 127) action Jump ("calloverworld")
        hotspot (1277, 6, 252, 119) action Jump ("calloverworld")
        hotspot (1767, 529, 150, 215) action Jump ("calloverworld")

## Hospital #############################################################

screen HospitalNav:
    imagemap:
        idle "maps/HospitalNav.png"
        hover "maps/HospitalNavb.png"
        ground "maps/HospitalNav.png"

        hotspot (447, 233, 508, 178) action Jump("label067") #Reception
        hotspot (994, 231, 506, 180) action Jump("label068") #Examination Room
        hotspot (449, 443, 508, 178) action Jump("label069") #2F Lobby
        hotspot (994, 443, 502, 178) action Jump("label070") #2F Nurse station
        hotspot (165, 649, 506, 178) action Jump("label071") #3F Lobby
        hotspot (710, 648, 505, 179) action Jump("label072") #3F Nurse station
        hotspot (1251, 649, 506, 174) action Jump("label073") #Room 302

## Interactions #############################################################

screen Infirmary:
    if label001nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label001natsumi == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label001saeko == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label001yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label001mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(5)
    imagebutton xpos npc1x ypos npc1y idle "natsumi/walking/DRStanding1.png" hover "natsumi/walking/DRStanding2.png" action Return(1) #Natsumi
    imagebutton xpos npc2x ypos npc2y idle "saeko/walking/DRStanding1.png" hover "saeko/walking/DRStanding2.png" action Return(2) #Saeko
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DLStanding1.png" hover "yukino/walking/DLStanding2.png" action Return(4) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(5) #Mark
    imagebutton xpos 840 ypos 225 idle "gui/Talking/Talk_Idle.png" hover "gui/Talking/Talk_Hover.png" action Return(6) #Agastya
    imagebutton xpos 1200 ypos 750 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(7) #Leave

screen Class12:
    if label002nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label002student == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label002yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label002mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(1) #Yukino
    imagebutton xpos npc1x ypos npc1y idle "students/7/DLStanding1.png" hover "students/7/DLStanding2.png" action Return(2) #Student
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(3) #Mark
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(4) #Nanjo
    imagebutton xpos 1600 ypos 580 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen Class13:
    if label003nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label003student == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label003yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label003mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DLStanding1.png" hover "yukino/walking/DLStanding2.png" action Return(1) #Yukino
    imagebutton xpos npc1x ypos npc1y idle "students/8/DLStanding1.png" hover "students/8/DLStanding2.png" action Return(2) #Student
    imagebutton xpos markx ypos marky idle "mark/walking/URStanding1.png" hover "mark/walking/URStanding2.png" action Return(3) #Mark
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DRStanding1.png" hover "nanjo/walking/DRStanding2.png" action Return(4) #Nanjo
    imagebutton xpos 1600 ypos 580 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen Class14:
    if label004nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label004student == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label004yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label004mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(1) #Yukino
    imagebutton xpos npc1x ypos npc1y idle "students/6/DRStanding1.png" hover "students/6/DRStanding2.png" action Return(2) #Student
    imagebutton xpos markx ypos marky idle "mark/walking/URStanding1.png" hover "mark/walking/URStanding2.png" action Return(3) #Mark
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DRStanding1.png" hover "nanjo/walking/DRStanding2.png" action Return(4) #Nanjo
    imagebutton xpos 1600 ypos 580 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen Class16:
    if label005nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label005student == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label005yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label005mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DLStanding1.png" hover "yukino/walking/DLStanding2.png" action Return(1) #Yukino
    imagebutton xpos npc1x ypos npc1y idle "students/9/DRStanding1.png" hover "students/9/DRStanding2.png" action Return(2) #Student
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(3) #Mark
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(4) #Nanjo
    imagebutton xpos 1600 ypos 580 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen Courtyard:
    if label006nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label006student == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label006yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label006mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    if label006ooishi == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label006hiremon == 0:
        imagebutton xpos 1350 ypos 350 idle "exclamation" hover "exclamation" action Return(6)
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DLStanding1.png" hover "yukino/walking/DLStanding2.png" action Return(1) #Yukino
    imagebutton xpos npc1x ypos npc1y idle "students/4/DRStanding1.png" hover "students/4/DRStanding2.png" action Return(2) #Student
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(3) #Mark
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(4) #Nanjo
    imagebutton xpos npc2x ypos npc2y idle "ooishi/walking/URStanding1.png" hover "ooishi/walking/URStanding2.png" action Return(5) #ooishi
    imagebutton xpos 1350 ypos 425 idle "gui/Talking/Talk_Idle.png" hover "gui/Talking/Talk_Hover.png" action Return(6) #Hiremon Stone
    imagebutton xpos 250 ypos 850 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(7) #Leave

screen TeacherLounge:
    if label007nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label007teacher == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label007yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label007mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    if label007elly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(5)
    if label007ayase == 0:
        imagebutton xpos ayasex ypos ayasey-50 idle "exclamation" hover "exclamation" action Return(6)
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(1) #Yukino
    imagebutton xpos npc1x ypos npc1y idle "students/teacher/DLStanding1.png" hover "students/teacher/DLStanding2.png" action Return(2) #Teacher
    imagebutton xpos markx ypos marky idle "mark/walking/URStanding1.png" hover "mark/walking/URStanding2.png" action Return(3) #Mark
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DLStanding1.png" hover "nanjo/walking/DLStanding2.png" action Return(4) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DLStanding1.png" hover "elly/walking/DLStanding2.png" action Return(5) #Elly
    imagebutton xpos ayasex ypos ayasey idle "ayase/walking/DRStanding1.png" hover "ayase/walking/DRStanding2.png" action Return(6) #Ayase
    imagebutton xpos 1250 ypos 650 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(7) #Leave

screen PrincipalOffice:
    if label008nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label008yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label008mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(2)
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(1) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(2) #Mark
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DLStanding1.png" hover "nanjo/walking/DLStanding2.png" action Return(3) #Nanjo
    imagebutton xpos 1250 ypos 770 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(4) #Leave

screen Passageway1F:
    if label009nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label009hanya == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label009yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label009mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(1) #Yukino
    imagebutton xpos npc1x ypos npc1y idle "hanya/walking/URStanding1.png" hover "hanya/walking/URStanding2.png" action Return(2) #Hanya
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(3) #Mark
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(4) #Nanjo
    imagebutton xpos 410 ypos 600 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave
    imagebutton xpos 900 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen Gymnasium:
    if label011nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label011student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label011student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label011yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label011mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos npc1x ypos npc1y idle "students/1/DLStanding1.png" hover "students/1/DLStanding2.png" action Return(5) #Student1
    imagebutton xpos npc2x ypos npc2y idle "students/3/DRStanding1.png" hover "students/3/DRStanding2.png" action Return(2) #Student2
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/URStanding1.png" hover "nanjo/walking/URStanding2.png" action Return(4) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(1) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(3) #Mark
    imagebutton xpos 1350 ypos 850 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen DramaClub:
    if label012nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label012student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label012student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label012student3 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(6)
    if label012yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label012mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos npc2x ypos npc2y idle "students/6/DLStanding1.png" hover "students/6/DLStanding2.png" action Return(5) #Student2
    imagebutton xpos npc1x ypos npc1y idle "students/4/DRStanding1.png" hover "students/4/DRStanding2.png" action Return(2) #Student1
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/URStanding1.png" hover "nanjo/walking/URStanding2.png" action Return(4) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DLStanding1.png" hover "yukino/walking/DLStanding2.png" action Return(1) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(3) #Mark
    imagebutton xpos npc3x ypos npc3y idle "students/3/URStanding1.png" hover "students/3/URStanding2.png" action Return(6) #Student3
    imagebutton xpos 1150 ypos 720 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(7) #Leave

screen BoxingClub:
    if label013nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label013student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label013yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label013mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos npc1x ypos npc1y idle "students/7/DRStanding1.png" hover "students/7/DRStanding2.png" action Return(2) #Student1
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/URStanding1.png" hover "nanjo/walking/URStanding2.png" action Return(4) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(1) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/URStanding1.png" hover "mark/walking/URStanding2.png" action Return(3) #Mark
    imagebutton xpos 1150 ypos 720 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen ArcheryClub:
    if label014nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label014student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label014yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label014mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos npc1x ypos npc1y idle "students/8/DRStanding1.png" hover "students/8/DRStanding2.png" action Return(2) #Student1
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DLStanding1.png" hover "nanjo/walking/DLStanding2.png" action Return(4) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DLStanding1.png" hover "yukino/walking/DLStanding2.png" action Return(1) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(3) #Mark
    imagebutton xpos 1150 ypos 720 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen FencingClub:
    if label015nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label015tamaki == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label015tadashi == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label015student1 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(6)
    if label015student2 == 0:
        imagebutton xpos npc4x ypos npc4y-50 idle "exclamation" hover "exclamation" action Return(7)
    if label015yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label015mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(2)
    imagebutton xpos npc2x ypos npc2y idle "tadashi/walking/ULStanding1.png" hover "tadashi/walking/ULStanding2.png" action Return(5) #Tadashi
    imagebutton xpos npc1x ypos npc1y idle "tamaki/walking/DRStanding1.png" hover "tamaki/walking/DRStanding2.png" action Return(4) #Tamaki
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/URStanding1.png" hover "nanjo/walking/URStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(1) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(2) #Mark
    imagebutton xpos npc3x ypos npc3y idle "students/1/DRStanding1.png" hover "students/1/DRStanding2.png" action Return(6) #Student3
    imagebutton xpos npc4x ypos npc4y idle "students/2/DRStanding1.png" hover "students/2/DRStanding2.png" action Return(7) #Student3
    imagebutton xpos 1150 ypos 720 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(8) #Leave

screen BalletClub:
    if label016nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label016student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label016student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label016yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label016mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos npc1x ypos npc1y idle "students/0/DRStanding1.png" hover "students/0/DRStanding2.png" action Return(2) #Student1
    imagebutton xpos npc2x ypos npc2y idle "students/2/DRStanding1.png" hover "students/2/DRStanding2.png" action Return(5) #Student2
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DLStanding1.png" hover "nanjo/walking/DLStanding2.png" action Return(4) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(1) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(3) #Mark
    imagebutton xpos 1150 ypos 720 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen Class21:
    if label018nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label018student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label018yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label018mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/5/DRStanding1.png" hover "students/5/DRStanding2.png" action Return(4) #Student1
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(1) #Mark
    imagebutton xpos 1600 ypos 580 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen Class22:
    if label019nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label019student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label019yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label019mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/8/DLStanding1.png" hover "students/8/DLStanding2.png" action Return(4) #Student1
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DLStanding1.png" hover "nanjo/walking/DLStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/URStanding1.png" hover "mark/walking/URStanding2.png" action Return(1) #Mark
    imagebutton xpos 1600 ypos 580 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen Class25:
    if label021nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label021student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label021student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label021yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label021mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/0/DRStanding1.png" hover "students/0/DRStanding2.png" action Return(4) #Student1
    imagebutton xpos npc2x ypos npc2y idle "students/9/DRStanding1.png" hover "students/9/DRStanding2.png" action Return(5) #Student2
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/URStanding1.png" hover "nanjo/walking/URStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DLStanding1.png" hover "yukino/walking/DLStanding2.png" action Return(2) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(1) #Mark
    imagebutton xpos 1150 ypos 720 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen EmptyClass:
    if label024nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label024yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label024mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/URStanding1.png" hover "nanjo/walking/URStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(1) #Mark
    imagebutton xpos 1150 ypos 720 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(4) #Leave

screen Cafeteria:
    if label022nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label022toro == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label022student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label022yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label022mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "toro/walking/DLStanding1.png" hover "toro/walking/DLStanding2.png" action Return(4) #Toro
    imagebutton xpos npc2x ypos npc2y idle "students/7/URStanding1.png" hover "students/7/URStanding2.png" action Return(5) #Student2
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DRStanding1.png" hover "nanjo/walking/DRStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(1) #Mark
    imagebutton xpos 1650 ypos 650 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen HomeEcRoom:
    if label023nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label023student == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label023yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label023mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/4/URStanding1.png" hover "students/4/URStanding2.png" action Return(4) #Students
    imagebutton xpos npc2x ypos npc2y idle "students/8/DLStanding1.png" hover "students/8/DLStanding2.png" action Return(4) #Student2
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DRStanding1.png" hover "nanjo/walking/DRStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(1) #Mark
    imagebutton xpos 1450 ypos 630 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen Class31:
    if label026nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label026student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label026student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label026yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label026mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/1/DLStanding1.png" hover "students/1/DLStanding2.png" action Return(4) #Toro
    imagebutton xpos npc2x ypos npc2y idle "students/2/URStanding1.png" hover "students/2/URStanding2.png" action Return(5) #Student2
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DRStanding1.png" hover "nanjo/walking/DRStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(1) #Mark
    imagebutton xpos 1585 ypos 585 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen Class33:
    if label027nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label027student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label027student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label027yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label027mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/0/ULStanding1.png" hover "students/0/ULStanding2.png" action Return(4) #Student1
    imagebutton xpos npc2x ypos npc2y idle "students/9/DLStanding1.png" hover "students/9/DLStanding2.png" action Return(5) #Student2
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DLStanding1.png" hover "nanjo/walking/DLStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(1) #Mark
    imagebutton xpos 1585 ypos 585 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen Class36:
    if label028nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label028student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label028yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label028mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/6/DRStanding1.png" hover "students/6/DRStanding2.png" action Return(4) #Student1
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos 1585 ypos 585 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen Class37:
    if label029nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label029student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label029student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label029yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label029mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/1/ULStanding1.png" hover "students/1/ULStanding2.png" action Return(4) #Student1
    imagebutton xpos npc2x ypos npc2y idle "students/8/DRStanding1.png" hover "students/8/DRStanding2.png" action Return(5) #Student2
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/URStanding1.png" hover "nanjo/walking/URStanding2.png" action Return(3) #Nanjo
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(1) #Mark
    imagebutton xpos 1585 ypos 585 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen Library:
    if label030nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label030tsutomu == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label030student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label030student3 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(6)
    if label030student4 == 0:
        imagebutton xpos npc4x ypos npc4y-50 idle "exclamation" hover "exclamation" action Return(7)
    if label030yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label030mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "tsutomu/walking/DLStanding1.png" hover "tsutomu/walking/DLStanding2.png" action Return(4) #Tsutomu
    imagebutton xpos npc2x ypos npc2y idle "students/5/DRStanding1.png" hover "students/5/DRStanding2.png" action Return(5) #Student1
    imagebutton xpos npc3x ypos npc3y idle "students/3/ULStanding1.png" hover "students/3/ULStanding2.png" action Return(6) #Student2
    imagebutton xpos npc4x ypos npc4y idle "students/2/DRStanding1.png" hover "students/2/DRStanding2.png" action Return(7) #Student3
    imagebutton xpos 1385 ypos 535 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(8) #Leave

screen StudentCouncil:
    if label031nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label031student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label031student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label031student3 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(6)
    if label031student4 == 0:
        imagebutton xpos npc4x ypos npc4y-50 idle "exclamation" hover "exclamation" action Return(7)
    if label031yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label031mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DLStanding1.png" hover "nanjo/walking/DLStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "students/5/DLStanding1.png" hover "students/5/DLStanding2.png" action Return(4) #PResident
    imagebutton xpos npc2x ypos npc2y idle "students/6/DRStanding1.png" hover "students/6/DRStanding2.png" action Return(5) #Student1
    imagebutton xpos npc3x ypos npc3y idle "students/7/ULStanding1.png" hover "students/7/ULStanding2.png" action Return(6) #Student2
    imagebutton xpos npc4x ypos npc4y idle "students/4/DLStanding1.png" hover "students/4/DLStanding2.png" action Return(7) #Student3
    imagebutton xpos 1200 ypos 780 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(8) #Leave

screen ArtRoom:
    if label032nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label032student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label032yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label032mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "students/9/DLStanding1.png" hover "students/9/DLStanding2.png" action Return(4) #Student
    imagebutton xpos 1385 ypos 635 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen Entryway:
    if label033nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label033student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label033student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label033yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label033mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DRStanding1.png" hover "nanjo/walking/DRStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc2x ypos npc2y idle "students/2/DRStanding1.png" hover "students/2/DRStanding2.png" action Return(5) #Student
    imagebutton xpos npc1x ypos npc1y idle "students/3/DLStanding1.png" hover "students/3/DLStanding2.png" action Return(4) #Student
    imagebutton xpos 500 ypos 420 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(7) #LeaveCity
    imagebutton xpos 1250 ypos 650 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #LeaveSchool

###### MIKAGE-CHO WARD ONE ###########

screen YY1: #Worldmap
    if label037nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label037yinyan == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label037yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label037mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DRStanding1.png" hover "nanjo/walking/DRStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "merchants/yinyan/stand1.png" hover "merchants/yinyan/stand2.png" action Return(4) #Clerk
    imagebutton xpos 1450 ypos 650 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #LeaveCity

screen Clinic1: #worldmap
    if label039nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label039physician == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label039yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label039mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label039nurse == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "hospital/physician/DRStanding1.png" hover "hospital/physician/DRStanding2.png" action Return(4) #Doctor
    imagebutton xpos npc2x ypos npc2y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(5) #Nurse
    imagebutton xpos 1250 ypos 750 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #LeaveCity

#### MIKAGE MALL ####

screen SMD1: #Mikage Mall
    if label041nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label041smd == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label041yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label041mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos markx ypos marky idle "mark/walking/URStanding1.png" hover "mark/walking/URStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "merchants/smd/Stand1.png" hover "merchants/smd/Stand2.png" action Return(4) #merchant
    imagebutton xpos 575 ypos 775 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #LeaveCity

screen PD1: #Mikage Mall
    if label042nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label042pd == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label042yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label042mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label042woman == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/URStanding1.png" hover "mark/walking/URStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc2x ypos npc2y idle "merchants/pd/Stand1.png" hover "merchants/pd/Stand2.png" action Return(5) #merchant
    imagebutton xpos npc1x ypos npc1y idle "townies/woman1/URStanding1.png" hover "townies/woman1/URStanding2.png" action Return(4) #Girl
    imagebutton xpos 550 ypos 725 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen ST1: #Mikage Mall
    if label044nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label044st == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label044yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label044mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label044woman == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc2x ypos npc2y idle "merchants/st/Stand1.png" hover "merchants/st/Stand2.png" action Return(5) #merchant
    imagebutton xpos npc1x ypos npc1y idle "townies/woman2/URStanding1.png" hover "townies/woman2/URStanding2.png" action Return(4) #Girl
    imagebutton xpos 770 ypos 780 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen JD1: #Mikage Mall
    if label045nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label045jd1 == 0:
        imagebutton xpos npc4x ypos npc4y-50 idle "exclamation" hover "exclamation" action Return(7)
    if label045yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label045mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label045jd2 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(6)
    if label045man1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label045student == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "townies/man1/DLStanding1.png" hover "townies/man1/DLStanding2.png" action Return(4) #man
    imagebutton xpos npc2x ypos npc2y idle "students/ifm/DRStanding1.png" hover "students/ifm/DRStanding2.png" action Return(5) #student
    imagebutton xpos npc3x ypos npc3y idle "merchants/jd1/Stand1.png" hover "merchants/jd1/Stand2.png" action Return(6) #jd1
    imagebutton xpos npc4x ypos npc4y idle "merchants/jd2/Stand1.png" hover "merchants/jd2/Stand2.png" action Return(7) #jd2
    imagebutton xpos 770 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(8) #Leave

#### MIKAGE-CHO ####

screen HistoricalSociety1: #Historical Society Outer
    if label048nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label048yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label048mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label048woman1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "merchants/hs/Stand1.png" hover "merchants/hs/Stand2.png" action Return(4) #receptionist
    imagebutton xpos 1230 ypos 500 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #LeaveInner
    imagebutton xpos 1270 ypos 680 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #LeaveCity

screen HistoricalSociety2: #Historical Society Inner
    if label049nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label049yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label049mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label049girl1 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label049ifstu1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DLStanding1.png" hover "nanjo/walking/DLStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc2x ypos npc2y idle "townies/girl1/ULStanding1.png" hover "townies/girl1/ULStanding2.png" action Return(5) #girl student
    imagebutton xpos npc1x ypos npc1y idle "students/ifm/DRStanding1.png" hover "students/ifm/DRStanding2.png" action Return(4) #IF Student
    imagebutton xpos 460 ypos 730 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

#### JOY STREET MALL ####

screen RC2: #Joystreet Mall
    if label053nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label053yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label053mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label053rc1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DLStanding1.png" hover "nanjo/walking/DLStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "merchants/rc/Stand1.png" hover "merchants/rc/Stand2.png" action Return(4) #merchant
    imagebutton xpos 1230 ypos 720 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen SMD2: #Joystreet Mall
    if label054nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label054yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label054mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label054smd == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label054oldman1 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "merchants/smd/Stand1.png" hover "merchants/smd/Stand2.png" action Return(4) #merchant
    imagebutton xpos npc2x ypos npc2y idle "townies/oldman1/DRStanding1.png" hover "townies/oldman1/DRStanding2.png" action Return(5) #oldman
    imagebutton xpos 700 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen YY2: #Joystreet Mall
    if label055nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label055yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label055mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label055yy == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    if reijimom == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "merchants/yinyan/Stand1.png" hover "merchants/yinyan/Stand2.png" action Return(5) #merchant
    imagebutton xpos npc2x ypos npc2y idle "townies/reijimom/DRStanding1.png" hover "townies/reijimom/DRStanding2.png" action Return(4) #reiji's mom
    imagebutton xpos 1480 ypos 650 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen PD2: #Joystreet Mall
    if label056nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label056yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label056mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label056pd == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label056stu == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/URStanding1.png" hover "nanjo/walking/URStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "merchants/pd/Stand1.png" hover "merchants/pd/Stand2.png" action Return(4) #Clerk
    imagebutton xpos npc2x ypos npc2y idle "students/5/DRStanding1.png" hover "students/5/DRStanding2.png" action Return(5) #Student
    imagebutton xpos 500 ypos 750 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen ST2: #Joystreet Mall
    if label057nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label057yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label057mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label057st == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label057man == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc2x ypos npc2y idle "merchants/st/Stand1.png" hover "merchants/st/Stand2.png" action Return(5) #merchant
    imagebutton xpos npc1x ypos npc1y idle "townies/man1/URStanding1.png" hover "townies/man1/URStanding2.png" action Return(4) #man
    imagebutton xpos 770 ypos 780 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen Clinic2: #Joystreet Mall
    if label058nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label058yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label058mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label058doctor == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label058nurse == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "hospital/physician/DRStanding1.png" hover "hospital/physician/DRStanding2.png" action Return(4) #Doctor
    imagebutton xpos npc2x ypos npc2y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(5) #Nurse
    imagebutton xpos 1250 ypos 750 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #LeaveCity

screen JD2: #Joystreet Mall
    if label061nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label061yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label061mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label061guy1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label061guy2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label061guy3 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(6)
    if label061jd1 == 0:
        imagebutton xpos npc4x ypos npc4y-50 idle "exclamation" hover "exclamation" action Return(7)
    if label061jd2 == 0:
        imagebutton xpos npc5x ypos npc5y-50 idle "exclamation" hover "exclamation" action Return(8)
    imagebutton xpos markx ypos marky idle "mark/walking/DLStanding1.png" hover "mark/walking/DLStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "townies/man1/DLStanding1.png" hover "townies/man1/DLStanding2.png" action Return(4) #man
    imagebutton xpos npc3x ypos npc3y idle "students/9/DRStanding1.png" hover "students/9/DRStanding2.png" action Return(5) #student
    imagebutton xpos npc2x ypos npc2y idle "students/ifm/DRStanding1.png" hover "students/ifm/DRStanding2.png" action Return(6) #student
    imagebutton xpos npc4x ypos npc4y idle "merchants/jd1/Stand1.png" hover "merchants/jd1/Stand2.png" action Return(7) #jd1
    imagebutton xpos npc5x ypos npc5y idle "merchants/jd2/Stand1.png" hover "merchants/jd2/Stand2.png" action Return(8) #jd2
    imagebutton xpos 770 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(9) #Leave

#### MIKAGE-CHO ####

screen Clinic3: #Overworld
    if label064nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label064yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label064mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label064doctor == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label064nurse == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "hospital/physician/DRStanding1.png" hover "hospital/physician/DRStanding2.png" action Return(4) #Doctor
    imagebutton xpos npc2x ypos npc2y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(5) #Nurse
    imagebutton xpos 1660 ypos 830 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #LeaveCity

screen Hospital1: #reception
    if label067nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label067yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label067mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label067sec == 0:
        imagebutton xpos clerk1x ypos clerk1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label067girl1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(6)
    if label067guy1 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label067guy2 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(7)
    if label067girl2 == 0:
        imagebutton xpos npc4x ypos npc4y-50 idle "exclamation" hover "exclamation" action Return(8)
    if label067yama == 0:
        imagebutton xpos npc5x ypos npc5y-50 idle "exclamation" hover "exclamation" action Return(9)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/URStanding1.png" hover "nanjo/walking/URStanding2.png" action Return(3) #Nanjo
    imagebutton xpos clerk1x ypos clerk1y idle "merchants/nurse2/Stand1.png" hover "merchants/nurse2/Stand2.png" action Return(4) #secretary
    imagebutton xpos npc1x ypos npc1y idle "townies/woman3/DLStanding1.png" hover "townies/woman3/DLStanding2.png" action Return(5) #man
    imagebutton xpos npc2x ypos npc2y idle "townies/injuredman/ulsitting.png" hover "townies/injuredman/ulsitting.png" action Return(6) #man
    imagebutton xpos npc3x ypos npc3y idle "townies/businessman/URStanding1.png" hover "townies/businessman/URStanding2.png" action Return(7) #man
    imagebutton xpos npc4x ypos npc4y idle "townies/woman4/DLStanding1.png" hover "townies/woman4/DLStanding2.png" action Return(8) #man
    imagebutton xpos npc5x ypos npc5y idle "yamaoka/walking/URStanding1.png" hover "yamaoka/walking/URStanding2.png" action Return(9) #yamaoka
    imagebutton xpos 300 ypos 850 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(10) #LeaveOutside
    imagebutton xpos 600 ypos 350 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(11) #LeaveInside

screen Hospital3: #2f waiting room
    if label069nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label069yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label069mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label069nurse == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label069oldman == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/URStanding1.png" hover "yukino/walking/URStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DLStanding1.png" hover "nanjo/walking/DLStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc2x ypos npc2y idle "hospital/nurse2/DLStanding1.png" hover "hospital/nurse2/DLStanding2.png" action Return(4) #Nurse
    imagebutton xpos npc1x ypos npc1y idle "townies/oldman1/DRStanding1.png" hover "townies/oldman1/DRStanding2.png" action Return(5) #oldman
    imagebutton xpos 400 ypos 390 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #LeaveOutside

screen Hospital5: #3f waiting room
    if label071nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label071yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label071mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label071oldman == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "townies/oldman1/DRStanding1.png" hover "townies/oldman1/DRStanding2.png" action Return(4) #oldman
    imagebutton xpos 0 ypos 400 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #LeaveOutside

screen Hospital6: #3f Nurse Station
    if label072nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label072yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label072mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label072nurse1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label072nurse2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc2x ypos npc2y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(5) #Nurse
    imagebutton xpos npc1x ypos npc1y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(4) #Nurse
    imagebutton xpos 1250 ypos 790 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #LeaveOutside

screen IHospital0: #2F Lobby
    if label074nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label074yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label074mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos 0 ypos 400 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(4) #LeaveOutside

screen IHospital1: #Nurse 2F
    if label075nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label075yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label075mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label075doctor == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    if label075nurse1 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label075nurse2 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(6)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc2x ypos npc2y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(5) #Nurse
    imagebutton xpos npc3x ypos npc3y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(6) #Nurse
    imagebutton xpos npc1x ypos npc1y idle "hospital/physician/DRStanding1.png" hover "hospital/physician/DRStanding2.png" action Return(4) #Doctor
    imagebutton xpos 1350 ypos 820 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(7) #LeaveOutside

screen IHospital2: #Nurse 3F
    if label077nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label077yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label077mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label077patient == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label077nurse == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(4) #Nurse
    imagebutton xpos npc2x ypos npc2y idle "townies/oldman1/DRStanding1.png" hover "townies/oldman1/DRStanding2.png" action Return(5) #oldman
    imagebutton xpos 1450 ypos 790 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #LeaveOutside

screen IHospital3: #Maki's Room
    if label078nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label078yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label078mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label078painting == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos 1400 ypos 170 idle "gui/Talking/Talk_Idle.png" hover "gui/Talking/Talk_Hover.png" action Return(4) #Painting
    imagebutton xpos 1350 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #LeaveOutside

screen IHospital4: #Waiting Room 2F
    if label079nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label079yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label079mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label079oldman == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "townies/oldman1/DRStanding1.png" hover "townies/oldman1/DRStanding2.png" action Return(4) #oldman
    imagebutton xpos 750 ypos 250 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #LeaveOutside

screen IHospital5: #ExamRoom
    if label081nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label081yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label081mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label081doctor == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label081nurse == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos npc1x ypos npc1y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(4) #Nurse
    imagebutton xpos npc2x ypos npc2y idle "hospital/physician/DRStanding1.png" hover "hospital/physician/DRStanding2.png" action Return(5) #Doctor
    imagebutton xpos 1340 ypos 780 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #LeaveOutside

screen IHospital6: #Reception
    if label083nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label083yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label083mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label083elly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos 150 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #LeaveOutside

##########################Post-Hospital Mikage-Cho With Demons##################################################

screen Sebec2: #ReijiEncounter
    if label083nanjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label083yukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label083mark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label083elly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos 150 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #LeaveOutside

screen SMD2a: #Joystreet Sennen Mannen Do after demons
    if label054amark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label054ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label054ananjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label054aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label054asmd1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label054aoldman1 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(6)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos npc1x ypos npc1y idle "merchants/smd/Stand1.png" hover "merchants/smd/Stand2.png" action Return(5) #merchant
    imagebutton xpos npc2x ypos npc2y idle "townies/oldman1/DRStanding1.png" hover "townies/oldman1/DRStanding2.png" action Return(6) #oldman
    imagebutton xpos 150 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(7) #LeaveOutside

screen ST2a: #Joystreet Satomi Tadashi after demons
    if label057amark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label057ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label057ananjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label057aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label057ast1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label057acustomer1 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(6)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos npc1x ypos npc1y idle "merchants/st/Stand1.png" hover "merchants/st/Stand2.png" action Return(5) #merchant
    imagebutton xpos npc2x ypos npc2y idle "townies/oldman1/DRStanding1.png" hover "townies/oldman1/DRStanding2.png" action Return(6) #oldman
    imagebutton xpos 150 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(7) #LeaveOutside

screen YY2a: #Joystreet Yin-Yan after demons
    if label055amark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label055ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label055ananjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label055aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label055ayy1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label055acustomer1 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(6)
    if label055acustomer2 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(7)
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DRStanding1.png" hover "nanjo/walking/DRStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos npc1x ypos npc1y idle "merchants/yinyan/stand1.png" hover "merchants/yinyan/stand2.png" action Return(5) #Clerk
    imagebutton xpos npc2x ypos npc2y idle "townies/man1/URStanding1.png" hover "townies/man1/URStanding2.png" action Return(6) #man
    imagebutton xpos npc3x ypos npc3y idle "townies/man1/URStanding1.png" hover "townies/man1/URStanding2.png" action Return(7) #man
    imagebutton xpos 1770 ypos 480 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(8) #LeaveCity

screen Clinic2a: #Joystreet Esumi Clinic after demons
    if label058amark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label058ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label058ananjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label058aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label058anurse == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label058adoctor == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(6)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos npc1x ypos npc1y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(5) #Nurse
    imagebutton xpos npc2x ypos npc2y idle "hospital/physician/DRStanding1.png" hover "hospital/physician/DRStanding2.png" action Return(6) #Doctor
    imagebutton xpos 1660 ypos 830 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(7) #LeaveCity

screen JD2a: #Joystreet Mall Judgment after demons
    if label061amark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label061ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label061ananjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label061aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label061ajd1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(7)
    if label061ajd2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(8)
    if label061acustomer1 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label061acustomer2 == 0:
        imagebutton xpos npc4x ypos npc4y-50 idle "exclamation" hover "exclamation" action Return(6)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos npc1x ypos npc1y idle "townies/man1/URStanding1.png" hover "townies/man1/URStanding2.png" action Return(5) #man
    imagebutton xpos npc2x ypos npc2y idle "townies/man1/URStanding1.png" hover "townies/man1/URStanding2.png" action Return(6) #man
    imagebutton xpos npc3x ypos npc3y idle "merchants/jd1/Stand1.png" hover "merchants/jd1/Stand2.png" action Return(7) #jd1
    imagebutton xpos npc4x ypos npc4y idle "merchants/jd2/Stand1.png" hover "merchants/jd2/Stand2.png" action Return(8) #jd2
    imagebutton xpos 1780 ypos 850 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(9) #Leave

screen Clinic3a: #Overworld after demons
    if label064amark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label064ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label064ananjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label064aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label064anurse == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label064adoctor == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(6)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos npc1x ypos npc1y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(5) #Nurse
    imagebutton xpos npc2x ypos npc2y idle "hospital/physician/DRStanding1.png" hover "hospital/physician/DRStanding2.png" action Return(6) #Doctor
    imagebutton xpos 1660 ypos 830 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(7) #LeaveCity

screen SMD1a: #Mikage Mall SMD after demons
    if label041amark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label041ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label041ananjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label041aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label041asmd1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos npc1x ypos npc1y idle "merchants/smd/Stand1.png" hover "merchants/smd/Stand2.png" action Return(5) #merchant
    imagebutton xpos 620 ypos 700 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen ST1a: #Mikage Mall Satomi Tadashi after demons
    if label044amark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label044ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label044ananjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label044aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label044ast1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos npc1x ypos npc1y idle "merchants/st/Stand1.png" hover "merchants/st/Stand2.png" action Return(5) #merchant
    imagebutton xpos 650 ypos 680 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #Leave

screen JD1a: #Mikage Mall
    if label045amark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label045ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label045ananjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label045aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label045ajd1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(6)
    if label045ajd2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(7)
    if label045student1 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(5)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos npc3x ypos npc3y idle "townies/man1/URStanding1.png" hover "townies/man1/URStanding2.png" action Return(5) #man
    imagebutton xpos npc1x ypos npc1y idle "merchants/jd1/Stand1.png" hover "merchants/jd1/Stand2.png" action Return(6) #jd1
    imagebutton xpos npc2x ypos npc2y idle "merchants/jd2/Stand1.png" hover "merchants/jd2/Stand2.png" action Return(7) #jd2
    imagebutton xpos 1780 ypos 650 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(8) #Leave

screen YY1a: #World Map
    if label037amark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label037ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label037ananjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label037aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(5)
    if label037ayy1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos markx ypos marky idle "mark/walking/DRStanding1.png" hover "mark/walking/DRStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/DRStanding1.png" hover "yukino/walking/DRStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/DRStanding1.png" hover "nanjo/walking/DRStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos npc1x ypos npc1y idle "merchants/yinyan/stand1.png" hover "merchants/yinyan/stand2.png" action Return(5) #Clerk
    imagebutton xpos 1450 ypos 700 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(6) #LeaveCity

screen Clinic1a: #worldmap
    if label039amark == 0:
        imagebutton xpos markx ypos marky-50 idle "exclamation" hover "exclamation" action Return(1)
    if label039ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label039ananjo == 0:
        imagebutton xpos nanjox ypos nanjoy-50 idle "exclamation" hover "exclamation" action Return(3)
    if label039aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(4)
    if label039anurse == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(5)
    if label039adoctor == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(6)
    imagebutton xpos markx ypos marky idle "mark/walking/ULStanding1.png" hover "mark/walking/ULStanding2.png" action Return(1) #Mark
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos nanjox ypos nanjoy idle "nanjo/walking/ULStanding1.png" hover "nanjo/walking/ULStanding2.png" action Return(3) #Nanjo
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos npc1x ypos npc1y idle "hospital/physician/DRStanding1.png" hover "hospital/physician/DRStanding2.png" action Return(6) #Doctor
    imagebutton xpos npc2x ypos npc2y idle "hospital/nurse2/DRStanding1.png" hover "hospital/nurse2/DRStanding2.png" action Return(5) #Nurse
    imagebutton xpos 1660 ypos 830 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(7) #LeaveCity

screen AlayaShrineb: #World Map
    if label038aelly == 0:
        imagebutton xpos ellyx ypos ellyy-50 idle "exclamation" hover "exclamation" action Return(1)
    if label038ayukino == 0:
        imagebutton xpos yukinox ypos yukinoy-50 idle "exclamation" hover "exclamation" action Return(2)
    if label038abutterfly == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(3)
    if label038asetsuko == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos ellyx ypos ellyy idle "elly/walking/DRStanding1.png" hover "elly/walkering/DRStanding2.png" action Return(4) #Elly
    imagebutton xpos yukinox ypos yukinoy idle "yukino/walking/ULStanding1.png" hover "yukino/walking/ULStanding2.png" action Return(2) #Yukino
    imagebutton xpos npc1x ypos npc1y idle "gui/Talking/Talk_Idle.png" hover "gui/Talking/Talk_Hover.png" action Return(3) #Butterfly
    imagebutton xpos npc2x ypos npc2y idle "Setsuko/Walking/DLStanding1.png" hover "Setsuko/Walking/DLStanding2.png" action Return(4) #Setsuko
    imagebutton xpos 1450 ypos 700 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

#=========================School Post-Hospital=========================#

screen Infirmaryb:
    if label001anatsumi == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label001asaeko == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label001asetsuko == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(3)
    if label001aagastya == 0:
        imagebutton xpos npc4x ypos npc4y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos npc1x ypos npc1y idle "Natsumi/Walking/DLStanding1.png" hover "Natsumi/Walking/DLStanding2.png" action Return(1) #Natsumi
    imagebutton xpos npc2x ypos npc2y idle "Saeko/Walking/DLStanding1.png" hover "Saeko/Walking/DLStanding2.png" action Return(2) #Saeko
    imagebutton xpos npc3x ypos npc3y idle "Setsuko/Walking/Bed.png" hover "Setsuko/Walking/Bed.png" action Return(3) #Setsuko
    imagebutton xpos 885 ypos 120 idle "gui/Talking/Talk_Idle.png" hover "gui/Talking/Talk_Hover.png" action Return(4) #Agastya
    imagebutton xpos 1400 ypos 850 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen PrincipalOfficeb:
    if label008aooishi == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label008ahanya == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    imagebutton xpos npc1x ypos npc1y idle "Ooishi/Walking/DLStanding1.png" hover "Ooishi/Walking/DLStanding2.png" action Return(1) #Ooishi
    imagebutton xpos npc2x ypos npc2y idle "Hanya/Walking/DLStanding1.png" hover "Hanya/Walking/DLStanding2.png" action Return(2) #Hanya
    imagebutton xpos 1600 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(3) #Leave

screen TeacherLoungeb:
    if label007ateacher == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos 315 ypos 370 idle "students/teacher/DLStanding1.png" hover "students/teacher/DLStanding2.png" action Return(1) #Teacher
    imagebutton xpos 1280 ypos 740 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(2) #Leave

screen Courtyardb:
    if label006astudent == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label006asign == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    imagebutton xpos npc1x ypos npc1y idle "students/4/DRStanding1.png" hover "students/4/DRStanding2.png" action Return(1) #Student
    imagebutton xpos npc2x ypos npc2y idle "gui/Talking/Talk_Idle.png" hover "gui/Talking/Talk_Hover.png" action Return(2) #Sign
    imagebutton xpos 0 ypos 700 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(3) #Leave

screen Class12b:
    if label002astudent == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/7/DLStanding1.png" hover "students/7/DLStanding2.png" action Return(1) #Student
    imagebutton xpos 1500 ypos 850 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(2) #Leave

screen Class13b:
    if label003astudent == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/8/DLStanding1.png" hover "students/8/DLStanding2.png" action Return(1) #Student
    imagebutton xpos 1500 ypos 850 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(2) #Leave

screen Class14b:
    if label004astudent == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/6/DRStanding1.png" hover "students/6/DRStanding2.png" action Return(1) #Student
    imagebutton xpos 1500 ypos 850 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(2) #Leave

screen Class16b:
    if label005astudent == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/9/DRStanding1.png" hover "students/9/DRStanding2.png" action Return(1) #Student
    imagebutton xpos 1450 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(2) #Leave

screen Gymnasiumb:
    if label011astudent == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/3/DRStanding1.png" hover "students/3/DRStanding2.png" action Return(1) #Student2
    imagebutton xpos 1500 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(2) #Leave

screen DramaClubb:
    if label012astudent1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label012astudent2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label012astudent3 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos npc2x ypos npc2y idle "students/6/DLStanding1.png" hover "students/6/DLStanding2.png" action Return(2) #Student2
    imagebutton xpos npc1x ypos npc1y idle "students/4/DRStanding1.png" hover "students/4/DRStanding2.png" action Return(1) #Student1
    imagebutton xpos npc3x ypos npc3y idle "students/3/URStanding1.png" hover "students/3/URStanding2.png" action Return(3) #Student3
    imagebutton xpos 1500 ypos 700 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(4) #Leave

screen FencingClubb:
    if label015atamaki == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label015atadashi == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label015astudent1 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(3)
    if label015astudent2 == 0:
        imagebutton xpos npc4x ypos npc4y-50 idle "exclamation" hover "exclamation" action Return(4)
    imagebutton xpos npc2x ypos npc2y idle "tadashi/walking/ULStanding1.png" hover "tadashi/walking/ULStanding2.png" action Return(5) #Tadashi
    imagebutton xpos npc1x ypos npc1y idle "tamaki/walking/DRStanding1.png" hover "tamaki/walking/DRStanding2.png" action Return(4) #Tamaki
    imagebutton xpos npc3x ypos npc3y idle "students/1/DRStanding1.png" hover "students/1/DRStanding2.png" action Return(6) #Student3
    imagebutton xpos npc4x ypos npc4y idle "students/2/DRStanding1.png" hover "students/2/DRStanding2.png" action Return(6) #Student3
    imagebutton xpos 1550 ypos 650 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(5) #Leave

screen Class22b:
    if label019astudent == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/8/DLStanding1.png" hover "students/8/DLStanding2.png" action Return(1) #Student1
    imagebutton xpos 1300 ypos 850 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(2) #Leave

screen Class24b:
    if label020astudent == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/8/DLStanding1.png" hover "students/8/DLStanding2.png" action Return(1) #Student1
    imagebutton xpos 1300 ypos 850 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(2) #Leave

screen Cafeteriab:
    if label022atoro == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label022astudent2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    imagebutton xpos npc1x ypos npc1y idle "toro/walking/DLStanding1.png" hover "toro/walking/DLStanding2.png" action Return(1) #Toro
    imagebutton xpos npc2x ypos npc2y idle "students/7/URStanding1.png" hover "students/7/URStanding2.png" action Return(2) #Student2
    imagebutton xpos 1340 ypos 770 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(3) #Leave

screen Class25b:
    if label021astudent1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label021astudent2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    imagebutton xpos npc1x ypos npc1y idle "students/0/DRStanding1.png" hover "students/0/DRStanding2.png" action Return(1) #Student1
    imagebutton xpos npc2x ypos npc2y idle "students/9/DRStanding1.png" hover "students/9/DRStanding2.png" action Return(2) #Student2
    imagebutton xpos 1300 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(3) #Leave

screen Class33b:
    if label027astudent1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label027astudent2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    imagebutton xpos npc1x ypos npc1y idle "students/0/ULStanding1.png" hover "students/0/ULStanding2.png" action Return(1) #Student1
    imagebutton xpos npc2x ypos npc2y idle "students/9/DLStanding1.png" hover "students/9/DLStanding2.png" action Return(2) #Student2
    imagebutton xpos 1340 ypos 770 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(3) #Leave

screen Class37b:
    if label029astudent1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label029astudent2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    imagebutton xpos npc1x ypos npc1y idle "students/1/ULStanding1.png" hover "students/1/ULStanding2.png" action Return(1) #Student1
    imagebutton xpos npc2x ypos npc2y idle "students/8/DRStanding1.png" hover "students/8/DRStanding2.png" action Return(2) #Student2
    imagebutton xpos 980 ypos 830 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(3) #Leave

screen ArtRoomb:
    if label032astudent1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/9/DLStanding1.png" hover "students/9/DLStanding2.png" action Return(1) #Student
    imagebutton xpos 950 ypos 880 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(2) #Leave

screen StudentCouncilb:
    if label031student1 == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label031student2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    imagebutton xpos npc1x ypos npc1y idle "students/6/DRStanding1.png" hover "students/6/DRStanding2.png" action Return(1) #Student1
    imagebutton xpos npc2x ypos npc2y idle "students/7/ULStanding1.png" hover "students/7/ULStanding2.png" action Return(2) #Student2
    imagebutton xpos 1700 ypos 600 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(3) #Leave

screen Libraryb:
    if label030atsutomu == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    if label030astudent2 == 0:
        imagebutton xpos npc2x ypos npc2y-50 idle "exclamation" hover "exclamation" action Return(2)
    if label030astudent3 == 0:
        imagebutton xpos npc3x ypos npc3y-50 idle "exclamation" hover "exclamation" action Return(3)
    imagebutton xpos npc1x ypos npc1y idle "tsutomu/walking/DLStanding1.png" hover "tsutomu/walking/DLStanding2.png" action Return(1) #Tsutomu
    imagebutton xpos npc2x ypos npc2y idle "students/5/DRStanding1.png" hover "students/5/DRStanding2.png" action Return(2) #Student1
    imagebutton xpos npc3x ypos npc3y idle "students/3/ULStanding1.png" hover "students/3/ULStanding2.png" action Return(3) #Student2
    imagebutton xpos 1700 ypos 870 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(4) #Leave

screen Gymnasiumc:
    if label011bstudent == 0:
        imagebutton xpos npc1x ypos npc1y-50 idle "exclamation" hover "exclamation" action Return(1)
    imagebutton xpos npc1x ypos npc1y idle "students/3/DRStanding1.png" hover "students/3/DRStanding2.png" action Return(1) #Student2
    imagebutton xpos 1700 ypos 150 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(2) #SQQ
    imagebutton xpos 1500 ypos 800 idle "gui/Talking/move_idle.png" hover "gui/Talking/move_hover.png" action Return(3) #Leave

#=========================Snow Queen Quest School=========================#
