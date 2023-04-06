

class Person:

    def __init__(self, cash, qnty=0):
       self.cash=cash
       self.qnty= qnty

    def purchased(self,used,items):
        if self.cash < used:
            print("Unable to buy! Not enough cash")
        else:
            self.cash -= used
            self.qnty+= items
            print(" Cash used : " + str(used))

    def info(self):
        print(f"Cash left {self.cash} , items : {self.qnty}" )


class Mall:
   items=0
   price=0
   
   @classmethod
   def __init__(cls,price,items):
       cls.price= price
       cls.items= items
       print(str(price) + "   " + str(items))

   @classmethod
   def purchased(cls,qnty,obj):
        cls.items-= qnty
        bill= qnty * cls.price
        print(bill , cls.price , cls.items)
        obj.purchased(bill,qnty)

class Burger(Mall):
    pass


p = Person(100)
p.info()
b = Burger(20,5)
b.purchased(2,p)
p.info()
        
