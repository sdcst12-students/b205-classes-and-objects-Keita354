"""
Rectangular Prism Object
Create a class that creates a rectangular prism.  You should be able to set all of the important measurements (l,w,h) when the object is instantiated in the constructor and you should have class methods that determine the surface area and volume.
You should have class methods that also allow you to change the dimensions of the object.
Instantiate 3 separate rectangular prisms with the test data given, and check the assertions are correct.
"""

class rectPrism:
    len = 0
    hig = 0
    wid = 0 
    def __init__(self, l=0, w=0,h=0):
        self.len = l
        self.hig = h
        self.wid = w
        
        pass

    def volume(self):
        if self.len ==0 or self.wid==0 or self.hig == 0:
            return None
        else:
            return self.len * self.wid * self.hig
    
    def surfaceArea(self):
        if self.len == 0 or self.wid == 0 or self.hig == 0:
            return None
        else:
            return 2 * (self.len * self.wid + self.len * self.hig + self.wid * self.hig)




a = rectPrism(l=10,w=2,h=5)
assert a.volume() == 100
assert a.surfaceArea() == 160

b = rectPrism(l=1,w=1,h=1)
assert b.volume() == 1
assert b.surfaceArea() == 6

c = rectPrism(l=2,w=0,h=10)
# note the invalid width
assert c.volume() == None
assert c.surfaceArea() == None