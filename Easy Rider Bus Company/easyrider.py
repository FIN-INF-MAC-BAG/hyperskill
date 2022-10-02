import itertools
import json
import re
import sys
from collections import Counter
import numpy as np

class busrider:
    def __init__(self):
        self.date_bus = json.loads(input())
        self.bus_id = 0
        self.stop_id = 0
        self.stop_name = 0
        self.next_stop = 0
        self.stop_type = 0
        self.a_time = 0
        self.list_stop = {}
        self.load_json()

    def create_dict(self):
        for i in self.date_bus:
            self.list_stop[i['bus_id']] = 0

    def check_bus_stop(self):
        for i in self.date_bus:
            if i['bus_id'] == "" or not isinstance(i['bus_id'], int):
                self.bus_id += 1
            # self.list_stop[i['bus_id']] += 1

    def check_time(self):
        p = 0
        b = 0
        ap = []
        print("Arrival time test:")
        for i in self.date_bus:
            if self.list_stop[i['bus_id']] < i['a_time']:
                self.date_bus[p]['Valid_time'] = 'False'
                self.list_stop[i['bus_id']] = i['a_time']
            else:
                self.date_bus[p]['Valid_time'] = 'True'
                self.list_stop[i['bus_id']] = i['a_time']

            p += 1
        for i in self.date_bus:
            if i['Valid_time'] == 'True' and i['bus_id'] not in ap:
                b += 1
                ap.append(i['bus_id'])
                if b != 0 :
                    print(f"bus_id line {i['bus_id']}: wrong time on station {i['stop_name']}")
        if b == 0:
            print("OK")
        # print(ap)

    def stop_start(self):
        start_stop = ['S', 'F']

        startstop = []
        finishstop = []
        transferstop = []
        allstops = []
        for i in self.date_bus:
            if i['stop_type'] in start_stop:
                self.list_stop[i['bus_id']] += 1

            if i['stop_type'] == "S":
                startstop.append(i["stop_name"])
            elif i['stop_type'] == "F":
                finishstop.append(i["stop_name"])
            allstops.append(i["stop_name"])
        list_keys = list(self.list_stop.keys())
        for p in range(len(self.list_stop)):
            if self.list_stop.get(list_keys[p]) < 2:
                print(f"There is no start or end stop for the line: {list_keys[p]}.")
                sys.exit()

        values, counts = np.unique(allstops, return_counts=True)
        for l in range(len(values)):
            if counts[l] >= 2:
                transferstop.append(values[l])
        startstop = sorted(set(startstop))
        transferstop = sorted(set(transferstop))
        finishstop = sorted(set(finishstop))
        # print(f"Start stops: {len(startstop)} {startstop}")
        # print(f"Transfer stops: {len(transferstop)} {transferstop}")
        # print(f"Finish stops: {len(finishstop)} {finishstop}")
        stops = []
        wrong_demand = []
        for s in itertools.chain(startstop, transferstop, finishstop):
            stops.append(s)
        for i in self.date_bus:
            if i['stop_type'] == "O" and i['stop_name'] in stops:
                wrong_demand.append(i['stop_name'])
        demand = set(wrong_demand)
        print("On demand stops test:")
        if not wrong_demand:
            print("OK")
        else:

            print(f"Wrong stop type: {sorted(list(set.intersection(demand)))}")

    def check_stop_id(self):
        for i in self.date_bus:
            if i['stop_id'] == "" or not isinstance(i['stop_id'], int):
                self.stop_id += 1

    def check_stop_name(self):
        template = r'[A-Z](\w+\s)([A-Z](\w*\s))?(Street|Road|Boulevard|Avenue)$'
        for i in self.date_bus:
            # print(str(i))
            if not re.match(template, i['stop_name']):
                # if i not in street:
                self.stop_name += 1

    def check_next_stop(self):
        for i in self.date_bus:
            if i['next_stop'] == "" or not isinstance(i['next_stop'], int):
                self.next_stop += 1

    def check_stop_type(self):
        print("On demand stops test:")
        line_128 = ['Sesame Street',  'Sunset Boulevard', 'Elm Street', 'Prospekt Avenue']
        line_256 = ['Sesame Street', 'Fifth Avenue', 'Elm Street', 'Pilotow Street']
        line_512 = ['Sunset Boulevard', 'Bourbon Street']
        pole = ['S', 'O', 'F', '']
        start_stop = ['S', 'F']
        demand = ['']
        lala = []
        for i in self.date_bus:
            if i['bus_id'] == 128:
                if i['stop_name'] not in line_128:
                    lala.append(i['stop_name'])
                elif i['stop_type'] in demand:
                    lala.append(i['stop_name'])
            elif i['bus_id'] == 256:
                if i['stop_name'] not in line_256:
                    lala.append(i['stop_name'])
                elif i['stop_type'] in demand:
                    lala.append(i['stop_name'])
            elif i['bus_id'] == 512:
                if i['stop_name'] not in line_512:
                    lala.append(i['stop_name'])
                elif i['stop_type'] in demand:
                    lala.append(i['stop_name'])
        ondeman = set(lala)
        if not lala:
            print("OK")
        else:
            print(f"Wrong stop type: {sorted(list(set.intersection(ondeman)))}")

    def check_a_time(self):
        time_format = re.compile('^([0-1][0-9]|2[0-3]):[0-5][0-9]$')
        for i in self.date_bus:
            if i['a_time'] == "" or not isinstance(i['a_time'], str) or not time_format.match(i['a_time']):
                # if time_format.match(i['a_time']):
                self.a_time += 1

    def load_json(self):

        column_names = ("bus_id", "stop_id",
                        "stop_name", "next_stop",
                        "stop_type", "a_time")
        self.create_dict()
        self.check_bus_stop()
        self.check_stop_id()
        self.check_stop_name()
        self.check_next_stop()
        # self.check_stop_type()
        self.check_a_time()
        self.stop_start()
        # self.check_time()


busrider()