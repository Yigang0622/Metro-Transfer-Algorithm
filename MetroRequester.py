# Created By Yigang Zhou (Mike)
# https:// MikeTech.it

import requests
import MetroUtil
import json
from StationManager import StationManager
from LineManager import LineManager
import os

url_shanghai_metro = "http://m.shmetro.com/core/shmetro/mdstationinfoback_new.ashx?act=getAllStations"


def request_shanghai_metro_data():
    station_manager = StationManager()
    line_manager = LineManager()
    offline_file_exist = os.path.isfile("shanghai.json")
    if offline_file_exist:
        f = open("shanghai.json")
        content = f.read()
        data = json.loads(content, encoding="utf-8")
        for each in data:
            line_number = MetroUtil.get_line_number(each["key"])
            station_name = str(each["value"])
            station_manager.add_station(station_name, line_number)
            line_manager.add_line(line_number, station_name)

        # station_manager.print_all_info()
        # line_manager.print_all_info()
        return station_manager, line_manager
    else:
        print("offline data not found, downloading")
        data = requests.get(url_shanghai_metro)
        if data.status_code == 200:
            for each in data.json():
                line_number = MetroUtil.get_line_number(each["key"])
                station_name = str(each["value"])
                station_manager.add_station(station_name, line_number)
                line_manager.add_line(line_number, station_name)
            f = open("shanghai.json", "w")
            json.dump(data.json(), f)

        # station_manager.print_all_info()
        # line_manager.print_all_info()
        return station_manager, line_manager
