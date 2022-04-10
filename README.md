This is my copy of the [fidgetingbits/knausj_talon](https://github.com/fidgetingbits/knausj_talon) fork of the [knausj_talon](https://github.com/knausj85/knausj_talon) repository for [Talon](https://talonvoice.com/) code.

This repo has good support for vim, as well as other useful stuff.

I pull parts this repo into my tree using git sparse checkout. Here's what my config looks like:

    $ cat .git/info/sparse-checkout
    # to refresh:
    #  git read-tree -mu HEAD
    apps/vim/doc
    apps/vim/vim.py
    apps/vim/vim.talon
    apps/vim/vim_command_mode.py
    apps/vim/vim_command_mode.talon
    apps/vim/vim_editing.py
    apps/vim/vim_motion_mode.py
    apps/vim/vim_motion_mode.talon
    apps/vim/vim_normal_mode.py
    apps/vim/vim_visual_mode.py
    apps/vim/vim_visual_mode.talon
    code/keys-plus.py
    misc/paths.py
    apps/systemd/journalctl.talon
    apps/systemd
    code/service_manager.py
    apps/generic_service_manager.talon
    code/timer_manager.py
    apps/generic_timer_manager.talon
    README.md