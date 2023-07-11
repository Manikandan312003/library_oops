class laptop():
    def print(self):
        print("Laptop")

class Desktop():
    def print(self):
        print("Desktop")

class dev():
    def print(self,java):
        try:
            (java.print())
        except:
            print("The object you passed not belongs to the laptop or Desktop object")
lap=laptop()
des=Desktop()
d=dev()
d.print(lap)
d.print(des)
