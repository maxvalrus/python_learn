class Laser():
    def does(self):
        return "desintegrate"

class Claw():
    def does(self):
        return "crush"

class SmartPhone():
    def does(self):
        return "ring"

class Robot():
    def __init__(self):
        self.l = Laser()
        self.c = Claw()
        self.s = SmartPhone()

    def does(self):
        print(self.l.does())
        print(self.c.does())
        print(self.s.does())

r = Robot()
r.does()

