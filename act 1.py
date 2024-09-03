class Vehicle:
 def __init__(self, name, maxspeed, mileage):
  self.name = name
  self.maxspeed = maxspeed
  self.mileage = mileage
class Bus(Vehicle):
 pass
 
schoolbus = Bus('Ishaan Bus', '300', '1000')
print(schoolbus.name, schoolbus.maxspeed, schoolbus.mileage)