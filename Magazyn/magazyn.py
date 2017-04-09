from Source import *

robot = MoveRobot("Pioneer_p3dx")

robot.setSpeed(12)

moveRobotinStorehouse = MoveRobotsInStorehouse()
moveRobotinStorehouse.setSpeed(Robots.Robot1, 12)

storehouse = Storehouse(places, stations, dockStations, stationBuffors, paths)
print(storehouse.getPalletePosition(1).getX(), storehouse.getPalletePosition(1).getY())
print(storehouse.getStationPosition(Stations.A).getX(), storehouse.getStationPosition(Stations.A).getY())