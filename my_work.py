import math

#To do Radian which is (Pi/180)degrees 
Radians = (math.pi / 180) * 32

#To calculate for the area and volume
def area_volume():
	Radius = int(input("Radius: "))
	Area = (math.pi * Radius * Radius)
	Volume = (2 * math.pi * Radius)
	Answers = {"Area": Area, "Volume": Volume}
	print(Answers)


import time
#To print out the current time
time.strftime("%H:%M:%S")

#To split a sentence into its words
"UCC is a great bushu suzu".split()


def print_():
    i = 0
    while(i < 19):
        if i / 2 == 0:
            print(i)
            i = i + 1
        else:i = i + 1

    i = i + 1

#To join a list of words into a sentence
word_list = [['Mini'], ['Miny'], ['Momi'], ['Mooo']]
print(' '.join(word[0] for word in word_list))


def get_age():
    age = int(input("Age?"))
    return age
def get_name():
    name = (input("Name?"))
    return name

import threading
from threading import Thread

#starting_github_anew
