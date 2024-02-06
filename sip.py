class Tesla:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.mode = 'Mode'
    def functions(self):
        if self.mode == 'mycar':
            return 'started'
        else:
            print("need ingition from ur end")
class model3(Tesla):
    def __init__(self,name,price,milage):
        super().__init__(name,price)
        self.milage =milage
        self.consumption = milage -10
    def functions(self):
        if self.consumption > 100 :
            return 'initiating safe mode'
        elif self.consumption<100:
            print("No worry u can travel.")
        else:
            return 'search for supercharge'
        
name = input('')
price = int(input(""))
milage = int(input('Distant'))
m = model3(name,price,milage)


    
        





