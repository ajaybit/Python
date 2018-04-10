from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_secene = self.scene_map.open_scene()

        while True:

            print "\n----------"
            next_scene_name = current_secene.enter()
            current_secene = self.scene_map.next_scene(next_scene_name)

class Death(scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom waoul be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CenterCorridor(Scene):

    def enter(self):
        print "The Gothon of Planet Percel #25 have invaded you ship and destroyed"
        print "your entire crew. you are the last surviveing member and you last"
        print "mission is to get the neutron destruct bomb from the Wepon Armory"
        print "put it in the bridge, and blow the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the centeral corridor to the Wepon Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clow costume"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a wepon to blast you"
