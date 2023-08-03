# Classes and object 
# Classes are used to create your own dataype

class Robot:
    
    def __init__(self, name, use, company, is_working, points):   
	    self.name = name
	    self.use = use
	    self.company = company
	    self.is_working = is_working
	    self.points = points
        
    def awesome(self):
        return self.points >= 9