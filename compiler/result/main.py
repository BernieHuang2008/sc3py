import threading
import scgame
game={}


class Generate_motion(scgame.Sprite):
    def __init__(self):
        super().__init__()
    
    
    def event_whenflagclicked_1(self):
        self.move_forward(10)
        self.turn(15)
        self.turn(-15)
        self.go_to('_random_')
        self.go_to(0, 0)
        self.go_to('_random_', secs=1)
        self.go_to(0, 0, secs=1)
        self.point_towards(90)
        self.point_towards('_mouse_')
        self.go_to(self.x + 10, self.y)
        self.go_to(0, self.y)
        self.go_to(self.x, self.y + 10)
        self.go_to(self.x, 0)
        if self.on_edge():
            self.bounce(self.on_edge()) # TODO
        self.restrict('rotation', 'left-right')
    
    def event_whenflagclicked(self):
        threads = [
            threading.Thread(target=self.event_whenflagclicked_1)
        ]
    
        all(t.start() for t in threads)
        return threads
class Generate_looks(scgame.Sprite):
    def __init__(self):
        super().__init__()
    
    
    def event_whenflagclicked_1(self):
        self.say('Hello!', secs=2)
        self.say('Hello!')
        self.think('Hmm...', secs=2)
        self.think('Hmm...')
        self.set_costume('造型2')
        self.next_costume()
        game.set_backdrop('背景1')
        game.next_backdrop()
        self.resize(self.size + 10)
        self.resize(100)
        self.effects['COLOR'] += 25
        self.affect()
        self.effects['COLOR'] = 0
        self.affect()
        self.clear_effects('looks')
        self.show()
        self.hide()
        game.set_layer(self, 'front')
        game.set_layer(self, self.layer + 1)
    
    def event_whenflagclicked(self):
        threads = [
            threading.Thread(target=self.event_whenflagclicked_1)
        ]
    
        all(t.start() for t in threads)
        return threads
class Generate_sound(scgame.Sprite):
    def __init__(self):
        super().__init__()
    
    
    def event_whenflagclicked_1(self):
        self.play_sound('喵', wait=True)
        self.play_sound('喵')
        game.stop_all_sounds()
        self.effects['PITCH'] += 10
        self.affect()
        self.effects['PITCH'] = 100
        self.affect()
        self.clear_effects('sound')
        self.volume += -10
        self.volume = 100
    
    def event_whenflagclicked(self):
        threads = [
            threading.Thread(target=self.event_whenflagclicked_1)
        ]
    
        all(t.start() for t in threads)
        return threads
class Generate_events(scgame.Sprite):
    def __init__(self):
        super().__init__()
    
    
    def event_whenflagclicked_1(self):
        game.broadcast('game.broadcast(message1)')
    def event_whenkeypressed_1(self):
        game.broadcast('game.broadcast(message1)', wait=True)
    def event_whenthisspriteclicked_1(self):
        ...  # TODO: Please complete the code here.
    def event_whenbackdropswitchesto_1(self):
        ...  # TODO: Please complete the code here.
    def event_whengreaterthan_1(self):
        ...  # TODO: Please complete the code here.
    def event_whenbroadcastreceived_message1_1(self):
        ...  # TODO: Please complete the code here.
    
    def event_whenflagclicked(self):
        threads = [
            threading.Thread(target=self.event_whenflagclicked_1)
        ]
    
        all(t.start() for t in threads)
        return threads
    
    def event_whenkeypressed(self):
        threads = [
            threading.Thread(target=self.event_whenkeypressed_1)
        ]
    
        all(t.start() for t in threads)
        return threads
    
    def event_whenthisspriteclicked(self):
        threads = [
            threading.Thread(target=self.event_whenthisspriteclicked_1)
        ]
    
        all(t.start() for t in threads)
        return threads
    
    def event_whenbackdropswitchesto(self):
        threads = [
            threading.Thread(target=self.event_whenbackdropswitchesto_1)
        ]
    
        all(t.start() for t in threads)
        return threads
    
    def event_whengreaterthan(self):
        threads = [
            threading.Thread(target=self.event_whengreaterthan_1)
        ]
    
        all(t.start() for t in threads)
        return threads
    
    def event_whenbroadcastreceived_message1(self):
        threads = [
            threading.Thread(target=self.event_whenbroadcastreceived_message1_1)
        ]
    
        all(t.start() for t in threads)
        return threads
class Generate_control(scgame.Sprite):
    def __init__(self):
        super().__init__()
    
    
    def event_whenflagclicked_1(self):
        self.wait(1)
        while True:
            for _ in range(10):
                if None:
                    if None:
                        while not None:
                            self.wait()
                    else:
                        ...  # TODO: Please complete the code here.
            game.stop('all')
    
    def event_whenflagclicked(self):
        threads = [
            threading.Thread(target=self.event_whenflagclicked_1)
        ]
    
        all(t.start() for t in threads)
        return threads