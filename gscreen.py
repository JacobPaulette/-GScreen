#!/usr/bin/env python3

import sys
import random
from os import listdir, system
from os.path import isfile, join, exists
from time import sleep

default_command = "gsettings set org.gnome.desktop.background picture-uri file://"
default_interval = 1

def main(arg_vars, command=default_command, interval=default_interval):
    if len(arg_vars) == 1:
        print("No Location")
        return

    path = arg_vars[1]
    if len(arg_vars) == 3:
        interval_input = arg_vars[2]
        try:
            interval = float(interval_input)
        except ValueError:
            print(interval_input, "is not a number")
            return

    if interval * 60 < 2:
       print("Interval to small")
       return
    if not exists(path):
        print("Invalid Location")
        return
    images = [i for i in listdir(path) if isfile(join(path,i)) and
                (".jpg" in i or ".png" in i)]

    while True:
        random.shuffle(images) 
        for i in images:
            system(command + join(path,i))
            sleep(int(60 * interval))


if __name__ == "__main__":
    main(sys.argv)
