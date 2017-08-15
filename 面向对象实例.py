class Vehicle:
  
    def __init__(self,distance,speed):
      self.time=distance/speed
    def result(self):
        print('need %.2f minutes'%self.time)
  
class Bike(Vehicle):
    pass
class Car(Vehicle):
    def __init__(self,distance,speed,fuel):
        Vehicle.__init__(self,distance,speed)
        self.fuel=fuel
        self.distance=distance

    def result(self):
        print('need %.2f minute and %.2f fuels'%(self.time,self.fuel*self.distance))

b=Bike(120,60)
b.result()
c=Car(240,80,0.1)
c.result()

