# Created By Yigang Zhou (Mike)
# https:// MikeTech.it
from Line import Line
from Route import Route


class LineManager:
    lines = {}

    def add_line(self, line_number, station_name):
        if line_number in self.lines:
            self.lines[line_number].add_station(station_name)
        else:
            line = Line(line_number)
            line.add_station(station_name)
            self.lines[line_number] = line

    def print_line_info(self, line_number):
        print("Line: ", line_number)
        print("lines: ", end="")
        if line_number in self.lines:
            line = self.lines[line_number]
            for each_station in line.stations:
                print(each_station, end="->")
        print()

    def print_all_info(self):
        for each in self.lines:
            self.print_line_info(self.lines[each].line_number)
            print()
        print("Line count ", len(self.lines))

    def get_best_route(self, from_station, to_station, lines):
        route = Route()
        route.from_stop = from_station
        route.to_stop = to_station
        route.stops = 9999
        if len(lines) == 0:
            route.stops = 9999
            return route
        else:
            for each_line in lines:
                line = self.lines[each_line]
                start_index = 0
                stop_index = 0

                for i in range(0, len(line.stations)):
                    if line.stations[i] == from_station:
                        start_index = i
                    elif line.stations[i] == to_station:
                        stop_index = i

                stops = abs(start_index - stop_index)

                if stops < route.stops:
                    route.stops = stops
                    route.line_number = line.line_number

        return route

    def print_stops(self, line_number, from_stop, to_stop):
        line = self.lines[line_number]
        start_index = 0
        end_index = 0
        stations = line.stations
        for i in range(0, len(stations) - 1):
            if stations[i] == from_stop:
                start_index = i
            elif stations[i] == to_stop:
                end_index = i

        if start_index > end_index:
            start_printing = False
            for each in reversed(stations):
                if each == from_stop:
                    print(each, " -> ", end="")
                    start_printing = True
                elif each == to_stop:
                    print(each)
                    start_printing = False
                elif start_printing:
                    print(each, " -> ", end="")
        else:
            start_printing = False
            for each in stations:
                if each == from_stop:
                    print(each, " -> ", end="")
                    start_printing = True
                elif each == to_stop:
                    print(each)
                    start_printing = False
                elif start_printing:
                    print(each, " -> ", end="")

        print()
