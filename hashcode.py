#!/usr/bin/env python3

def parse1(path):
    f = open(path)
    for i, line in enumerate(f):
        list_weights = list()
        if i == 0:
            tmp = line.split()
            rows = tmp[0]
            columns = tmp[1]
            nb_drones = tmp[2]
            nb_turns = tmp[3]
            max_pl = tmp[4]
    return rows, columns, nb_drones, nb_turns, max_pl

print(parse1("busy_day.in"))
