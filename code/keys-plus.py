
from talon import Context, Module

mod = Module()

@mod.capture(rule="{self.letter}")
def upper_letter(m) -> str:
    "Return one upper case"
    return m.letter.upper()

