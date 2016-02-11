#!/usr/bin/env python3

def parse1(path):
    f = open(path)
    for i, line in enumerate(f):
        if i == 0:
            tmp = line.split()
            rows = tmp[0]
            columns = tmp[1]
            nb_drones = tmp[2]
            nb_turns = tmp[3]
            max_pl = tmp[4]
    return rows, columns, nb_drones, nb_turns, max_pl

<<<<<<< 55c507c1461cb10aafbe3d64b2d8a4c4fcf6ddfb
def parse3(path):
  f = open(path)
  pro = list()
  for i, line in enumerate(f):
    if i == 2:
      pro = line.split()
  return pro


print(parse3("busy_day.in"))
=======
def parse2(path):
    f = open(path)
    for i, line in enumerate(f):
        if i == 1:
            tmp = line.split()
            nb_diff_prod = tmp[0]
    return nb_diff_prod

def parse4(path):
    f = open(path)
    for i, line in enumerate(f):
        if i == 3:
            tmp = line.split()
            nb_house = tmp[0]
    return nb_house

print(parse1("busy_day.in"))
>>>>>>> LOL
