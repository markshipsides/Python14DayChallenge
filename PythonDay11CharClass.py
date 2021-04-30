# MarkS - Python Challenge Day 11 Character Class - Object Oriented Programming

from typing import Dict


class Superhero:

    def __init__(self, name: str, sex: str, dob: list, alive: bool, superpowers: Dict[str, int]):
        self.name = name
        self.sex = sex
        self.dob = dob
        self.alive = alive
        self.superpowers = superpowers

    def print_dob(self):
        print(self.dob)

    def print_superpowers(self):
        print(self.superpowers)


jimmy_superhero = Superhero("Jimmy", "Male", [1945, 5, 1], True, {"Flight": 50})
jimmy_superhero.print_dob()
jimmy_superhero.print_superpowers()
