#ingredients class
#name is string, cal is int, vegan veg and gf are bools

class ingredients(object):
    def __init__(self, name, vegan, veg, gf):
        self.name = name
        #self.cal = cal
        self.vegan = vegan
        self.veg = veg
        self.gf = gf
        
    def is_vegan(self):
        if self.vegan == True:
            return True
        else:
            return False

    def is_veg(self):
        if self.veg == True:
            return True
        else:
            return False

    def is_gf(self):
        if self.gf == True:
            return True
        else:
            return False

    