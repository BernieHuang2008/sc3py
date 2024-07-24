import threading
import scgame
game={}


class Generate_Stage(scgame.Sprite):
    def __init__(self):
        super().__init__()

        self.name = "Stage"
        self.costumes = {'背景1': scgame.Costume(name='背景1', file='src/cd21514d0531fdffb22204e0ec5ed84a.svg', center=(240, 180))}
        self.sounds = {'啵': scgame.Sound(name='啵', file='src/83a9787d4cb6f3b7632b4ddfebf74367.wav')}

        # basic properties
        game.layer.place(self, 0)

    


class Generate_角色1(scgame.Sprite):
    def __init__(self):
        super().__init__()

        self.name = "角色1"
        self.costumes = {'造型1': scgame.Costume(name='造型1', file='src/35c5ce84dd1fd84f24c7f7ca1b0e4a47.svg', center=(24.166515000000004, 27.114620000000002))}
        self.sounds = {'喵': scgame.Sound(name='喵', file='src/83c36d806dc92327b9e7049a565c6bff.wav')}

        # basic properties
        self.x = 115.54139494819718
        self.y = -52.718462285233215
        self.size = 100
        self.direction = -141.5288362069349
        game.layer.place(self, 1)

    
    def event_whenflagclicked_1(self):
        for _ in range(1000):
            self.move_forward(10)
            self.turn(5)
    
    def event_whenflagclicked(self):
        threads = [
            threading.Thread(target=self.event_whenflagclicked_1)
        ]
    
        all(t.start() for t in threads)
        return threads

