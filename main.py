# -*- coding: utf-8 -*-
"""
    Petri net simulation
    ------------------------
    An example of petri net simulation of a chemical processes based on
    code from http://www.azimuthproject.org/azimuth/show/Petri+net+programming.
    :copyright: (c) 2015 by A. Kassahun.
    :license: BSD.
"""

import random
import copy


# check arcs

# check check initial markings

#Run simulations
def get_enabled_transitions():
    enabled_list = []
    for t in arcs:
        enabled = True
        for p, m in arcs[t]['inputs'].iteritems():
            if markings[p] < m: enabled = False; break
        if enabled: enabled_list += [t]
    return enabled_list

def get_markings_values(markings, places):
    values = []
    for p in places:
        values += [markings[p]]
    return tuple(values)

#run simulation
def run_simulation(places, arcs, markings, steps):
    results = []
    for i in xrange(steps):
        # find enabled transition
        fire_list = get_enabled_transitions()

        if fire_list:
            # select random
            to_fire_i = random.randrange(len(fire_list))
            to_fire_t = fire_list[to_fire_i]

            # fire the event
            for p, m in arcs[to_fire_t]['inputs'].iteritems():
                markings[p] -= m
      
            for p, m in arcs[to_fire_t]['outputs'].iteritems():
                markings[p] += m

            result = [get_markings_values(markings, places), to_fire_t]
            results += [result]
        else:
            break
    return results
    
if __name__ == '__main__':
    # initialization of the petri net
    # define places, transitions and arcs
    places = ['H', 'O', 'H2O']
    transitions = ['Combine', 'Split']
    arcs = {
        'Combine': {'inputs' : {'H': 2, 'O': 1},
                    'outputs': {'H2O': 1}},         
        'Split'  : {'inputs':  {'H2O': 1},
                    'outputs': {'H': 2, 'O': 1}}
       }

    # set the markings
    init_markings = {"H": 5, "O": 3, "H2O": 3}

    #decide on the number of steps to simulate
    steps = 10

    # run simulation
    markings = copy.deepcopy(init_markings)
    results = run_simulation(places, arcs, markings, steps)

    fmt_str = ' %3s '*len(places)
    print fmt_str % tuple(places), 'Transitions'
    print fmt_str % get_markings_values(init_markings, places), '*Init*'

    for markings, trans in results:
        print fmt_str % markings, trans


