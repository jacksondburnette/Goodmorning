# takes first light and last light times as args
# spits out a pie chart that represents daylight hours

import sys

def get_args():
    """Get command line arguments"""
    if len(sys.argv) < 1:
        print "USAGE: {} [frist light] [last light]".format(argv[0])
        print "Use military time."
    else:
        return sys.argv[1:]

def light_percent(first_light, last_light):
    """INPUT: firt and last light (ints) as military time
    OUTPUT: percentage of time that it is light out"""
    total_hrs = 24.0
    light_hrs = last_light - first_light
    return (light_hrs / total_hrs) * 100
