
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
             
#class instance    
honda = Car('Honda')
#car properties
toyota = Car('Toyota', 'Corolla')
toyota.name
toyota.model
#car number of doors
opel = Car('Opel', 'Omega 3')
porshe = Car('Porshe', '911 Turbo')

[opel.num_of_doors, porshe.num_of_doors, Car('Koenigsegg', 'Agera R').num_of_doors]
#car number of wheels
man = Car('MAN', 'Truck', 'trailer')
man.num_of_wheels
koenigsegg = Car('Koenigsegg', 'Agera R')
koenigsegg.num_of_wheels
[koenigsegg.num_of_wheels, man.num_of_wheels]

koenigsegg = Car('Koenigsegg', 'Agera R')
koenigsegg.is_saloon()

man = Car('MAN', 'Truck', 'trailer')
parked_speed = man.speed
moving_speed = man.drive(7).speed
[parked_speed, moving_speed]

man = Car('Mercedes', 'SLR500')
parked_speed = man.speed
moving_speed = man.drive(3).speed
[parked_speed, moving_speed]



