class Animal:
  def __init__(self):
    self.num_of_eyes = 2

  def breath(self):
    print("inhale and exhale")
#Fish inherited from the class animal.
class Fish(Animal):
  def __init__(self):
      super().__init__() #Initilise everthing into fish from animal
  
  def breath(self):
    super().breath()
    print("Doing this in the water.")

  def swim(self):
    print("moving in the water.")



lemo = Fish()
print(lemo.num_of_eyes)
print(lemo.breath())


