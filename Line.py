# Created By Yigang Zhou (Mike)
# https:// MikeTech.it


class Line:

    line_number = 0
    stations = []

    def __init__(self, line_number):
        self.line_number = line_number
        self.stations = []

    def add_station(self, station_name):
        self.stations.append(station_name)
