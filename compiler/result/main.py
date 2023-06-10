class Generate_角色1(scgame.Sprite):

    def event_whenflagclicked_1(self):
        for _ in range(10):  # repeat 10 times.
            for _ in range(10):  # repeat 10 times.
                self.move_forward(10)  # move forward for 10 steps.
            