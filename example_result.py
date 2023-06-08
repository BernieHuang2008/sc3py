import ourlib

class Generate_角色1(ourlib.Sprite):    # DEVcomment: each Sprite has its own Generator Class.
  def __init__():
    super().__init__()
    ...
  
  def onGreenFlag():    # run when user click the green flag.     # DEVcomment: there's detailed comments in the final result.
    self.onGreenFlag_1()
    self.onGreenFlag_2()
    ...
  
  def onGreenFlag_1():
    self.moveToXY(10, 10)   # move to (10, 10).     # DEVcomment: self.moveToXY is defined in 'ourlib.Sprite'.
    ...
  
  def onGreenFlag_2():
    self.say_for_seconds("hi", 2)   # say "hi" for 2 seconds.
    ...
    
  ...

    
def start_program():
  outlib.initEngine()
  ...
    
if __name__=='__init__':
  # init global variables.
  sprite_list = []
  ...
  
  # init Sprites.
  角色1 = Generate_角色1()
  sprite_list.append(角色1)
#   角色2 = Generate_角色2()
#   sprite_list.append(角色2)
  ...
  
  # start program.
  start_program()
    
