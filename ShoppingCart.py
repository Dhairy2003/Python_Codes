
# A program to show shops enetered by 2 different people and number of items brought


class Person:
   
   items=0
   store_entered=0

   def __init__(self,cash):
      self.cash=cash
      print(f"U got {self.cash} in hands ! Enjoy ")

   def info(self):
       print(f"cash left : {self.cash}")

   def cart(self,b):
      if self.cash < b:
          print("U cant buy the item")
      else:    
       self.cash=self.cash- b
       Person.items+=1
    
   @classmethod
   def entered():
      Person.store_entered+=1

   
class Mall:
   
   def __init__(self, items , price ) :  
         self.items = items
         self.price= price


   def info(self):
        print(f" price = {self.price}, items = {self.items}")

   
   def purchased(self,qnty,p):
         self.items= self.items - qnty
         b=qnty*self.price
         print("Purcahsed Bill : " + str(b))
         p.cart(b)
         return qnty*self.price



class Burgers(Mall):
    pass

class clothing(Mall):
    pass
   

p1=Person(100)
b= Burgers(10,10)
c= clothing(5,20)

p1.info()
b.info()
b.purchased(9,p1)
b.info()
p1.info()







      
      