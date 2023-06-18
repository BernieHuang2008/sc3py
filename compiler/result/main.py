import threading
import scgame


class Generate_motion(scgame.Sprite):
    def __init__(self):
        super().__init__()

    def event_whenflagclicked_1(self):
        self.move_forward(10)  # move forward for 10 steps.
        self.turn(15)  # turn right 15 degrees.
        self.turn(-15)  # turn left 15 degrees.
        self.go_to('_random_')  # go to '_random_'.
        self.go_to(0, 0)  # go to (0, 0).
        self.go_to('_random_', secs=1)  # glide to '_random_' in 1s.
        self.go_to(0, 0, secs=1)  # gilde to (0, 0) in 1s.
        self.point_towards(90)  # point in direction 90.
        self.point_towards('_mouse_')  # point towards '_mouse_'.
        self.go_to(self.x + 10, self.y)  # change x by 10.
        self.go_to(0, self.y)  # set x to 0.
        self.go_to(self.x, self.y + 10)  # change y by 10.
        self.go_to(self.x, 0)  # set y to 0.
        if self.on_edge():
            self.bounce()  # bounce if on edge.
        self.restrict('rotation', 'left-right')  # set rotation style to left-right.

    def event_whenflagclicked(self):
        threading.Thread(target=self.event_whenflagclicked_1)


class Generate_looks(scgame.Sprite):
    def __init__(self):
        super().__init__()

    def event_whenflagclicked_1(self):
        self.say('Hello!', secs=2)  # say 'Hello!' for 2s.
        self.say('Hello!')  # say 'Hello!'.
        self.think('Hmm...', secs=2)  # think 'Hmm...' for 2s.
        self.think('Hmm...')  # think 'Hmm...'.
        self.set_costume('造型2')  # switch costume.
        self.next_costume()  # next costume.
        game.set_backdrop('背景1')  # switch backdrop.
        game.next_backdrop()  # next backdrop.
        self.resize(self.size + 10)  # change size by 10%.
        self.resize(100)  # set size to 100%.
        self.effects['COLOR'] += 25  # change COLOR effect by 25.
        self.affect()
        self.effects['COLOR'] = 0  # set COLOR effect to 0.
        self.affect()
        self.clear_effects('looks')  # clear graphic effects.
        self.show()  # show.
        self.hide()  # hide.
        game.set_layer(self, 'front')  # go to front layer.
        game.set_layer(self, self.layer + 1)  # go forward 1 layers.

    def event_whenflagclicked(self):
        threading.Thread(target=self.event_whenflagclicked_1)


class Generate_sound(scgame.Sprite):
    def __init__(self):
        super().__init__()

    def event_whenflagclicked_1(self):
        self.play_sound('喵', wait=True)  # play sound '喵' until done.
        self.play_sound('喵')  # play sound '喵'.
        game.stop_all_sounds()  # stop all sounds.
        self.effects['PITCH'] += 10  # change PITCH effect by 10.
        self.affect()
        self.effects['PITCH'] = 100  # set PITCH effect to 100.
        self.affect()
        self.clear_effects('sound')  # clear sound effects.
        self.volume += -10  # change volume by -10.
        self.volume = 100  # set volume to 100.
    
    def event_whenflagclicked(self):
        threading.Thread(target=self.event_whenflagclicked_1)
