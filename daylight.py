# takes first light and last light times as args
# spits out a pie chart that represents daylight hours

import sys

import matplotlib.pyplot as plt

def get_args():
    """Get command line arguments"""
    if len(sys.argv) < 1:
        print "USAGE: {} [frist light] [last light]".format(argv[0])
        print "Use military time."
    else:
        return sys.argv[1:]

def light_percent(sunup, sundown):
    """INPUT: firt and last light (ints) as military time
    OUTPUT: percentage of time that it is light out"""
    total_hrs = 2400.
    light_hrs = sundown - sunup
    return (light_hrs / total_hrs) * 100

# plt.pie draws segs counterclockwise from the x-axis
# therefore, to accurately depict day chunk, we must
# calculate the offset of sundown from 1800 in degrees
def sundown_offset(sundown):
    """INPUT: sundown time, military
    OUTPUT: degree offset of sundown from 1800"""
    offset_time = 1800 - int(sundown)
    offset_fraction = offset_time / 2400.
    return 360 * offset_fraction

def main():
    sunup, sundown = tuple(get_args())
    day_percent = light_percent(int(sunup), int(sundown))
    night_percent = 100 - day_percent

    slices = [day_percent, night_percent]
    labels = ['day', 'night']
    colors = ['gold', 'darkblue']
    startangle = sundown_offset(sundown)

    plt.pie(slices, labels=labels, colors=colors, startangle=startangle)
    plt.axis('equal')
    plt.show()

main()
