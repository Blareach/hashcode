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

def parse2(path):
    f = open(path)
    for i, line in enumerate(f):
        if i == 1:
            tmp = line.split()
            nb_diff_prod = tmp[0]
    return nb_diff_prod

def parse3(path):
  f = open(path)
  pro = list()
  for i, line in enumerate(f):
    if i == 2:
      pro = line.split()
  return pro

def parse4(path):
    f = open(path)
    for i, line in enumerate(f):
        if i == 3:
            tmp = line.split()
            nb_house = tmp[0]
    return nb_house

def parse_house(path, index):
    f = open(path)
    cpt = 0
    for i, line in enumerate(f):
        if i > 3 and cpt < 2:
            while cpt < int(index):
                l1 = list()
                l1 = line.split()
                l2 = list()
                l2 = next(f).split()
                cpt += 1
                return l1 + l2

def list_house(path):
    f = open(path)
    index = int(parse4(path))
    cpt = 0
    l = list()
    i = 0
    while i < index:
        cpt_house = 0
        for j, line in enumerate(f):
            if j > 3 and cpt_house < 2:
                cpt_tmp = 0
                l1 = list()
                l2 = list()
                cpt_de_trop = 0
                while cpt_house < index:
                    if cpt_de_trop == 0:
                        l1 = line.split()
                        l2 = next(f).split()
                        cpt_de_trop += 1
                    else:
                        l1 = next(f).split()
                        l2 = next(f).split()
                        cpt_de_trop += 1
                    tmp = l1 + l2
                    l.insert(cpt_de_trop + 1, tmp)
                    cpt_house += 1
        i += 1
    for tmp in l:
        print(tmp[0], ', '.join(map(str, tmp[1:])))
        print()
    return l

print(parse1("busy_day.in"))
print(parse2("busy_day.in"))
#print(parse3("busy_day.in"))
print(parse4("busy_day.in"))
#print(list_house("busy_day.in"))
list_house("busy_day.in")
