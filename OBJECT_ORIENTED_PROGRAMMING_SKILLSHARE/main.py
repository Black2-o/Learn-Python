# class IceCream:
#   def __init__(self):
#     self.scoops = 3

  
#   def eat(self, scoops):
#     if self.scoops >= scoops:
#       self.scoops  -= scoops
#     else:
#       print("Not enough bites left!")
#   def add(self, scoops):
#     self.scoops += scoops



# ice_cream = IceCream()
# # ice_cram.eat()
#######  RESULT ###########
#  ice_cream.eat(2)
#  ice_cream.scoops
# 1
#  ice_cream.eat(2)
# Not enough bites left!
#  ice_cream.scoops
# 1
#  ice_cream.eat(1)
#  ice_cream.scoops
# 0
#  ice_cream.eat(1)
# Not enough bites left!
#  


# # Light

# class Light:
#   def __init__(self,sync = None):
#     super().__init__()
#     self.on = False
#     self.sync = sync

#   def is_on(self):
#     return self.on
#   def toggle(self):
#     # if self.on:
#     #   self.on = False
#     # else:
#     #   self.on = True
#     self.on = not self.on
#     if self.sync is not None:
#       self.sync.toggle()

# class OldLight(Light):
#   def __init__(self, sync = None):
#     super().__init__(sync)
#     self.on = False
#     self.sync = sync
#     self.flicker = False

#   def toggle(self):
#     super().toggle()
#     if self.on:
#       self.flicker = not self.flicker



# light = OldLight()
# light1 = Light()
# light2 = Light(sync = light1)

# # light = Light()

# ## Light 
# class Light:
#   on = False


# a = Light()
# b = Light()



# Step 1: https://replit.com/@ALVINWAN1/Coding-101-OOP-Ice-Cream-Step-1
# Step 2: https://replit.com/@ALVINWAN1/Coding-101-OOP-Ice-Cream-Step-2
# Step 3: https://replit.com/@ALVINWAN1/Coding-101-OOP-Ice-Cream-Step-3
# Step 4: https://replit.com/@ALVINWAN1/Coding-101-OOP-Ice-Cream-Step-4


# class IceCream:
  
#   max_scoops = 3
  
#   def __init__(self):
#     super().__init__()
#     self.scoops = 0

#   def eat(self, scoops):
#     if self.scoops < scoops:
#       print("Not enough bites left!")
#     else:
#       self.scoops -= scoops

#   def add(self, scoops):
#     self.scoops += scoops # new - in-place op
#     if self.scoops > self.max_scoops:
#       self.scoops = 0
#       print("Too many scoops! Dropped ice cream.")



# class IceCreamTruck:
#   def __init__(self):
#     super().__init__()
#     self.sold = 0
#   def order(self, scoops):
#     ice_cream = IceCream()
#     self.add(ice_cream,scoops)
#     return ice_cream
#   def add(self, ice_cream, scoops):
#     ice_cream.add(scoops)
#     self.sold += scoops


# class DeluxeIceCreamTruck(IceCreamTruck):
#   def order(self, scoops):
#     ice_cream = super().order(scoops)
#     ice_cream.add(1)
#     return ice_cream

# truck = DeluxeIceCreamTruck()


# class A:
#   pass

# class B(A):
#   pass

# class C(A, B):
#   pass