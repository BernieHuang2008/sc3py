import threading
import scgame
game={}


class Generate_motion(scgame.Sprite):
    def __init__(self):
        super().__init__()

        self.name = "motion"
        self.costumes = {'造型2': scgame.Costume(name='造型2', file='src/0fb9be3e8397c983338cb71dc84d0b25.svg', center=(46, 53))}
        self.sounds = {'喵': scgame.Sound(name='喵', file='src/83c36d806dc92327b9e7049a565c6bff.wav')}

        # basic properties
        self.x = 0
        self.y = 0
        self.size = 100
        self.direction = -118.07248693585294
        game.layer.place(self, 8)

    
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

        self.name = "looks"
        self.costumes = {'造型2': scgame.Costume(name='造型2', file='src/0fb9be3e8397c983338cb71dc84d0b25.svg', center=(46, 53))}
        self.sounds = {'喵': scgame.Sound(name='喵', file='src/83c36d806dc92327b9e7049a565c6bff.wav')}

        # basic properties
        self.x = -68.1304970394062
        self.y = 19.10814159246027
        self.size = 100
        self.direction = -118.07248693585294
        game.layer.place(self, 7)

    
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
        game.layer.adjust(self, 'front')
        game.layer.adjust(self, 1)
    
    def event_whenflagclicked(self):
        threads = [
            threading.Thread(target=self.event_whenflagclicked_1)
        ]
    
        all(t.start() for t in threads)
        return threads


class Generate_sound(scgame.Sprite):
    def __init__(self):
        super().__init__()

        self.name = "sound"
        self.costumes = {'造型2': scgame.Costume(name='造型2', file='src/0fb9be3e8397c983338cb71dc84d0b25.svg', center=(46, 53))}
        self.sounds = {'喵': scgame.Sound(name='喵', file='src/83c36d806dc92327b9e7049a565c6bff.wav')}

        # basic properties
        self.x = 42.526555338817175
        self.y = 19.074579258600977
        self.size = 100
        self.direction = -118.07248693585294
        game.layer.place(self, 6)

    
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

        self.name = "events"
        self.costumes = {'造型2': scgame.Costume(name='造型2', file='src/0fb9be3e8397c983338cb71dc84d0b25.svg', center=(46, 53))}
        self.sounds = {'喵': scgame.Sound(name='喵', file='src/83c36d806dc92327b9e7049a565c6bff.wav')}

        # basic properties
        self.x = 76.35142468600206
        self.y = -40.61417286612703
        self.size = 100
        self.direction = -118.07248693585294
        game.layer.place(self, 1)

    
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

        self.name = "control"
        self.costumes = {'造型2': scgame.Costume(name='造型2', file='src/0fb9be3e8397c983338cb71dc84d0b25.svg', center=(46, 53))}
        self.sounds = {'喵': scgame.Sound(name='喵', file='src/83c36d806dc92327b9e7049a565c6bff.wav')}

        # basic properties
        self.x = -90.79198179965546
        self.y = 54.89513205018057
        self.size = 100
        self.direction = -118.07248693585294
        game.layer.place(self, 2)

    
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

