from talon import ui, imgui, Module, speech_system, actions, app

# We keep command_history_size lines of history, but by default display only
# command_history_display of them.
mod = Module()
setting_command_history_auto = mod.setting("command_history_auto", bool, default=0)
setting_command_history_auto_more = mod.setting("command_history_auto_more", bool, default=0)
setting_command_history_size = mod.setting("command_history_size", int, default=50)
setting_command_history_display = mod.setting(
    "command_history_display", int, default=10
)
setting_command_history_sticky = mod.setting("command_history_sticky", int,
        default=0)

hist_more = False
history = []
gui = None

def parse_phrase(word_list):
    return " ".join(word.split("\\")[0] for word in word_list)


def on_phrase(j):
    global history

    try:
        val = parse_phrase(getattr(j["parsed"], "_unmapped", j["phrase"]))
    except:
        val = parse_phrase(j["phrase"])

    if val != "":
        history.append(val)
        history = history[-setting_command_history_size.get() :]


# todo: dynamic rect?
def update_gui(gui: imgui.GUI):
    global history
    global hist_more
    gui.text("Command History")
    gui.line()
    text = (
        history[:] if hist_more else history[-setting_command_history_display.get() :]
    )
    for line in text:
        gui.text(line)

    gui.spacer()
    if gui.button("Command history close"):
        actions.user.history_disable()

def on_ready():
    global hist_more
    global gui
    if setting_command_history_auto_more.get():
        hist_more = True

    y = 0
    # XXX - This should be used once we have sticky support
    main_screen = ui.main_screen()
    x = main_screen.x + main_screen.width / 2.6

    img = imgui.open(y=y)
    gui = img(update_gui)
    if setting_command_history_sticky.get():
        gui.fixed(0, 100)

    if setting_command_history_auto.get():
        if not gui.showing:
            gui.show()

app.register("ready", on_ready)


speech_system.register("phrase", on_phrase)



@mod.action_class
class Actions:
    def history_toggle():
        """Toggles viewing the history"""
        if gui.showing:
            gui.hide()
        else:
            gui.show()

    def history_enable():
        """Enables the history"""
        gui.show()

    def history_disable():
        """Disables the history"""
        gui.hide()

    def history_clear():
        """Clear the history"""
        global history
        history = []

    def history_more():
        """Show more history"""
        global hist_more
        hist_more = True

    def history_less():
        """Show less history"""
        global hist_more
        hist_more = False

    def history_get(number: int):
        """returns the history entry at the specified index"""
        num = (0 - number) - 1
        return history[num]
