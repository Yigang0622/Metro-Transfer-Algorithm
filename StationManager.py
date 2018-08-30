# Created By Yigang Zhou (Mike)
# https:// MikeTech.it

from Station import Station


class StationManager:

    stations = {}
    station_names = set()

    def add_station(self, name, line):
        self.station_names.add(name)
        if name in self.stations:
            self.stations[name].add_line(line)
        else:
            station = Station(name)
            station.add_line(line)
            self.stations[name] = station

    def print_station_info(self, name):
        print("Station: ", name, "-> ", end="")
        print("lines: ", end="")
        if name in self.stations:
            station = self.stations[name]
            for each_line in station.lines:
                print(each_line, end=", ")

    def print_all_info(self):
        for each in self.stations:
            self.print_station_info(self.stations[each].name)
            print()
        print("Station count ", len(self.stations))

    def get_same_lines(self, from_station, to_station):
        line_numbers = []
        for each_line in from_station.lines:
            if each_line in to_station.lines:
                line_numbers.append(each_line)
        return line_numbers

