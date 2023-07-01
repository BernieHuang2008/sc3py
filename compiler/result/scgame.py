"""
It's the document of scgame.
"""
import math
import time


def deg2rad(deg):
    """
    [Tool]: Convert degree to radian.
    :param deg: degree
    :return: radian
    """
    return deg / 180 * math.pi


class Sprite:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.costume = None
        self.size = 100
        self.direction = 90
        self.volume = 100
        self.layer = game.get_layer(self)
        self.effects = {
            'COLOR': 0,
            'BRIGHTNESS': 0,
            'TRANSPARENCY': 0,
            'PITCH': 100
        }
        self.backup = dict()

    def __str__(self):
        return self.__class__.__name__

    def draw(self):  # TODO: function draw
        """
        Draw the sprite from all the configurations and static.
        :return: None
        """
        ...
        time.sleep(1 / game.fps)

    # PART1: motion
    def move_forward(self, distance):
        """
        Move forward.
        :param distance: distance to move
        :return: None
        """
        delta_x = distance * math.sin(deg2rad(self.direction))
        delta_y = distance * math.cos(deg2rad(self.direction))
        self.x += delta_x
        self.y += delta_y
        self.draw()

    def turn(self, angle):
        """
        Turn.
        :param angle: angle to turn
        :return: None
        """
        self.direction += angle
        self.direction %= 360
        self.draw()

    def go_to(self, *args, secs=0):
        """
        Go to somewhere.
        :param secs: time to glide, default 0s.
        :return: None
        """
        target = [self.x, self.y]
        if len(args) == 2:
            # go to (x, y)
            target = tuple(args)
        elif len(args) == 1:
            # go somewhere
            target = args[0]
            ...  # TODO: target finding

        if secs:  # if glide is on:
            frame_num = math.ceil(secs / game.fps)
            delta_x = target[0]
            delta_y = target[1]
            for _ in range(frame_num):
                self.x += delta_x / frame_num
                self.y += delta_y / frame_num
                self.draw()
        else:
            self.x, self.y = target
            self.draw()

    def point_towards(self, target):  # TODO: function point_towards
        """
        Point towards.
        :param target: target/direction to point
        :return: None
        """
        pass

    def on_edge(self):  # TODO: function on_edge
        """
        Check if the sprite is on edge.
        :return: which edge the sprite is on. ('left', 'right', 'top' or 'bottom')
        """
        pass

    def bounce(self, mode):
        """
        Bounce.
        :param mode: mode to bounce. ('left', 'right', 'top' or 'bottom')
        :return: None
        """
        if mode in ['left', 'right']:
            self.direction = - self.direction
        elif mode in ['top', 'bottom']:
            self.direction = 180 - self.direction
        self.direction %= 360
        self.draw()

    def restrict(self, attribute, style):  # TODO: function restrict
        """
        Restrict.
        :param attribute: attribute to restrict
        :param style: rules of the restriction
        :return: None
        """
        pass

    # PART2: looks
    def say(self, content, secs=0):  # TODO: function say
        """
        Say something in seconds.
        :param content: content to say
        :param secs: time to say
        :return: None
        """
        pass

    def think(self, content, secs=0):  # TODO: function think
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
        self.costume = costume
        self.draw()

    def next_costume(self):
        """
        Switch to next costume.
        :return: None
        """
        self.costume_idx = self.costumes.index(self.costume) + 1
        self.costume_idx %= len(self.costumes)
        self.costume = self.costumes[self.costume_idx]
        self.draw()

    def resize(self, size):
        """
        Resize.
        :param size: size to resize (%)
        :return: None
        """
        self.size = size
        self.draw()

    def affect(self):  # TODO: function affect
        """
        Apply all effects on this sprite.
        :return: None
        """
        pass

    def clear_effects(self, *effects):  # TODO: function clear_effects
        """
        Clear effects of this sprite.
        :param effects: effect names to be clear
        :return: None
        """
        pass

    def show(self):
        """
        Show this sprite.
        :return: None
        """
        self.effects['TRANSPARENCY'] = self.backup.get('TRANSPARENCY', 100)
        self.draw()

    def hide(self):
        """
        Hide this sprite.
        :return: None
        """
        self.backup['TRANSPARENCY'] = self.effects['TRANSPARENCY']
        self.effects['TRANSPARENCY'] = 0
        self.draw()

    # PART3: sound
    def play_sound(self, sound, wait=False):  # TODO: function play_sound
        """
        Play sound.
        :param sound: sound name
        :param wait: whether to wait until done
        :return: None
        """
        pass

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 1 / game.fps
        time.sleep(timeout)
