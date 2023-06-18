"""
It's the document of scgame.
"""


class Sprite:
    def __init__(self):
        pass

    def __str__(self):
        return self.__class__.__name__

    # PART1: motion
    def move_forward(self, distance):
        """
        Move forward.
        :param distance: distance to move
        :return: None
        """
        pass

    def turn(self, angle):
        """
        Turn.
        :param angle: angle to turn
        :return: None
        """
        pass

    def go_to(self, x, y, secs=0):
        """
        Go to.
        :param x: x coordinate
        :param y: y coordinate
        :param secs: time to glide
        :return: None
        """
        pass

    def point_towards(self, target):
        """
        Point towards.
        :param target: target/direction to point
        :return: None
        """
        pass

    def on_edge(self):
        """
        Check if the sprite is on edge.
        :return: bool
        """
        pass

    def bounce(self):
        """
        Bounce.
        :return: None
        """
        pass

    def restrict(self, attribute, style):
        """
        Restrict.
        :param attribute: attribute to restrict
        :param style: rules of the restriction
        :return: None
        """
        pass

    # PART2: looks
    def say(self, content, secs=0):
        """
        Say something in seconds.
        :param content: content to say
        :param secs: time to say
        :return: None
        """
        pass

    def think(self, content, secs=0):
        """
        Think something in seconds.
        :param content: content to think
        :param secs: time to think
        :return: None
        """
        pass

    def set_costume(self, costume):
        """
        Set costume.
        :param costume: costume name to set
        :return: None
        """
        pass

    def next_costume(self):
        """
        Switch to next costume.
        :return: None
        """
        pass

    def resize(self, size):
        """
        Resize.
        :param size: size to resize (%)
        :return: None
        """
        pass

    def affect(self):
        """
        Apply all effects on this sprite.
        :return: None
        """
        pass

    def clear_effects(self, *effects):
        """
        Clear effects of this sprite.
        :param effects: effects to be clear
        :return: None
        """
        pass

    def show(self):
        """
        Show this sprite.
        :return: None
        """
        pass

    def hide(self):
        """
        Hide this sprite.
        :return: None
        """
        pass
