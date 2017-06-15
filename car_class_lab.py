
class Car(object):
  num_of_doors = 4
  num_of_wheels = 4
  speed = 0  
  
  def __init__(self, name='General', model='GM', car_type=None):
    self.name = name
    self.model = model
    self.car_type = car_type
    if self.name == 'Koenigsegg' or self.name == 'Porshe':
      self.num_of_doors = 2
    elif car_type == 'trailer':
       self.num_of_wheels = 8
    else:
       pass
          
  def is_saloon(self):
      if self.car_type is not 'trailer':
        return self
  def drive(self, speed):
        self.speed = speed
        if self.name == 'MAN':
          self.speed = 77
          return self
        elif self.name == 'Mercedes':
          self.speed = 1000
          return self
        else:
          pass
             




