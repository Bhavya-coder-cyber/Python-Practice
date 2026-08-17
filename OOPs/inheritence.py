class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding spices to the chai")

class ChaiShop:
    chai_demo = BaseChai  #Inheritance
    def __init__(self):
        self.chai = self.chai_demo("Masala Chai")
    def serve(self):
        print(f"Serving {self.chai.type} chai")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai("KAALA")  #Inheritance

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai_cls.add_spices() #Takes the instance of ChaiShop class