
class Storehouse:
    def __init__(self, places, stations, dockStations, stationBuffors, paths):
	self.palets = self.places = places
	self.stations = stations
	self.dockStations = dockStations
	self.stationBuffors = stationBuffors
	self.paths = paths
      
    def getPalletePosition(self, paletteId):
	return self.palets[paletteId]
    
    def getStationPosition(self, stationName):
	return self.stations[int(stationName)]
    
    def getDockStationPosition(self, dockStationName):
	return self.dockStations[int(dockStationName)]
      
    def getStationBuffor(self, stationBufforName):
	return self.stationBuffors[int(stationBufforName)]
    
    def getPath(self, pathId):
	return self.paths[pathId]
      
    def reset(self):
	self.palets = self.places
	pass