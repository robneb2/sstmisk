from general import Point

class MoveRobot:
    position = Point()
  
    def __init__(self, name):
        self.name = name
    
    def goStraight(self, distance):
	pass
    
    def rotate(self, deegress):
	pass
    
    def setSpeed(self, velocity):
	pass
    
    def getPosition(self):
	return self.position