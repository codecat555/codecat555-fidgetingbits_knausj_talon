from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: terminal
and tag: user.systemd
"""


@ctx.action_class("user")
class UserActions:
    # System-wide services
    def service():
        actions.insert("systemctl --no-pager ")

    def service_stop():
        actions.insert("systemctl --no-pager stop ")

    def service_start():
        actions.insert("systemctl --no-pager start ")

    def service_restart():
        actions.insert("systemctl --no-pager restart ")

    def service_status():
        actions.insert("systemctl --no-pager status ")

    def service_enable():
        actions.insert("systemctl --no-pager enable ")

    def service_disable():
        actions.insert("systemctl --no-pager disable ")

    # System-Wide timers
    def timer():
        actions.user.insert_cursor("systemctl --no-pager [|].timer")

    def timer_stop():
        actions.user.insert_cursor("systemctl --no-pager stop [|].timer")

    def timer_start():
        actions.user.insert_cursor("systemctl --no-pager start [|].timer")

    def timer_status():
        actions.user.insert_cursor("systemctl --no-pager status [|].timer")

    def timer_enable():
        actions.user.insert_cursor("systemctl --no-pager enable [|].timer")

    def timer_disable():
        actions.user.insert_cursor("systemctl --no-pager disable [|].timer")

    # User timers
    def timer_user():
        actions.user.insert_cursor("systemctl --user --no-pager [|].timer")

    def timer_user_stop():
        actions.user.insert_cursor("systemctl --user --no-pager stop [|].timer")

    def timer_user_start():
        actions.user.insert_cursor("systemctl --user --no-pager start [|].timer")

    def timer_user_status():
        actions.user.insert_cursor("systemctl --user --no-pager status [|].timer")

    def timer_user_enable():
        actions.user.insert_cursor("systemctl --user --no-pager enable [|].timer")

    def timer_user_disable():
        actions.user.insert_cursor("systemctl --user --no-pager disable [|].timer")

    def service_status_by_name(name: str):
        actions.insert(f"systemctl --no-pager status {name}")

    def service_stop_by_name(name: str):
        actions.insert(f"systemctl stop {name}")

    def service_start_by_name(name: str):
        actions.insert(f"systemctl start {name}")

    def service_enable_by_name(name: str):
        actions.insert(f"systemctl enable {name}")

    def service_disable_by_name(name: str):
        actions.insert(f"systemctl disable {name}")
