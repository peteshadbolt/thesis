#!/usr/bin/python
from glob import glob
from os import path
import matplotlib.image as mpimg
import numpy as np
import os
import re

def get_color(filename):
    """ Is this image in color or black and white? """
    filename = path.join("../", filename)
    temp_filename = "%s/%s_temp.jpg" % tuple(os.path.split(filename))
    if not path.exists(temp_filename):
        os.system("convert %s %s" % (filename, temp_filename))

    # Load the image into numpy
    image = mpimg.imread(temp_filename)
    R = image[:,:, 0]
    G = image[:,:, 1]
    B = image[:,:, 2]

    # Check the difference between R,G,B channels
    tol = 1e-3
    if np.allclose(R, G, rtol=tol) and np.allclose(G, B, rtol=tol):
        return "bw"
    else:
        return "color"


def count_figures(filename):
    """ Count the B&W / color figures """
    totals = {"bw":0, "color":0}
    data = open(filename, "r").read()
    figures = re.findall("\\includegraphics.*\}", data)
    getfilename = lambda x: x.split("{")[1][:-1]
    figures = map(getfilename, figures)
    for figure in figures:
        print figure + " "*(50-len(figure)),
        color = get_color(figure)
        print color
        totals[color] += 1
    return totals
        

if __name__ == "__main__":
    root = "../"
    files = glob("../chapter*/chapter*.tex") + glob("../appendix*/*.tex")
    totals = {"bw":0, "color":0}
    for filename in files:
        chap_total = count_figures(filename)
        totals["bw"] += chap_total["bw"]
        totals["color"] += chap_total["color"]
    print totals
    
        



