# Created By Yigang Zhou (Mike)
# https:// MikeTech.it


class Station:

    name = ""
    lines = []

    def __init__(self, name):
        self.name = name
        self.lines = []

    def add_line(self, line_number):
        self.lines.append(line_number)

