import os
import sys
from typing import Set

from talon import Context, Module, actions

mod = Module()
mod.list("first_names", desc="Common first names")
mod.list("last_names", desc="Common first names")

cwd = os.path.dirname(os.path.realpath(__file__))
first_names_file = os.path.join(cwd, "common_names", "first_names.csv")
last_names_file = os.path.join(cwd, "common_names", "last_names.csv")

# These list should contain values you don't want to be published publicly.
private_first_names_file = os.path.join(cwd, "common_names", "private_first_names.csv")
private_last_names_file = os.path.join(cwd, "common_names", "private_last_names.csv")


def populate_list(name_list, file_name):
    with open(file_name, "r") as f:
        for line in f:
            line = line.rstrip()
            if "," in line:
                sound, word = line.split(",")
                if word is None:
                    word = sound
            else:
                sound = word = line
            if line not in name_list.keys():
                name_list[sound] = word


first_names = {}
last_names = {}
populate_list(first_names, first_names_file)
populate_list(first_names, private_first_names_file)
populate_list(last_names, last_names_file)
populate_list(last_names, private_last_names_file)


@mod.capture
def first_name(m) -> str:
    "One first name"


@mod.capture
def last_name(m) -> str:
    "One last name"


ctx = Context()
ctx.lists["self.first_names"] = first_names
ctx.lists["self.last_names"] = last_names


@ctx.capture(rule="{self.first_names}")
def first_name(m):
    return m.first_names


@ctx.capture(rule="{self.last_names}")
def last_name(m):
    return m.last_names
