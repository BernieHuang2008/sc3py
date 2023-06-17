import threading

class Generate_motion(scgame.Sprite):

    def event_whenflagclicked_1(self):
        self.move_forward(10)  # move forward for 10 steps.
        self.turn(15)  # turn right 15 degrees.
        self.turn(-1 * 15)  # turn left 15 degrees.
        self.go_to('_random_')  # go to '_random_'.
        self.go_to(0, 0)  # go to (0, 0).
        self.go_to('_random_', secs=1)  # glide to '_random_' in 1s.
        self.go_to(0, 0, secs=1)  # gilde to (0, 0) in 1s.
        self.point_towards(90)  # point in direction 90.
        self.point_towards('_mouse_')  # point towards '_mouse_'.
        self.change_x(10)  # change x by 10.
        self.set_x(0)  # set x to 0.
        self.change_y(10)  # change y by 10.
        self.set_y(0)  # set y to 0.
        if self.on_edge():
            self.bounce()  # bounce if on edge.
        self.restrict('rotation', 'left-right')  # set rotation style to left-right.

    def event_whenflagclicked(self):
        threading.Thread(target=self.event_whenflagclicked_1)
