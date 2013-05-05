import game_interface
import random
import time
import cPickle
import neural_net
import neural_net_impl

filename = "moves.txt"

def get_move(view):
	return (random.randint(0,3), False)

# DEFAULT GET_MOVE
# def get_move(view):
#   # Choose a random direction.
#   # If there is a plant in this location, then try and eat it.
#   hasPlant = view.GetPlantInfo() == game_interface.STATUS_UNKNOWN_PLANT
#   # Choose a random direction
#   if hasPlant:
#     for i in xrange(5):
#       view.GetImage()
#   time.sleep(0.1)
#   return (random.randint(0, 4), hasPlant)

# def get_move(view):
#   # Choose a random direction.
#   # If there is a plant in this location, then try and eat it.
#   hasPlant = view.GetPlantInfo() == game_interface.STATUS_UNKNOWN_PLANT
#   # Choose a random direction
#   if hasPlant:
#     for i in xrange(5):
#       view.GetImage()
#   time.sleep(0.1)
#   #print "RoundNum: " + str(view.GetRound()) + " (" + str(view.GetXPos()) + ", " + str(view.GetYPos()) + ")"
#   print getDirection(view)
#   return (getDirection(view), hasPlant)

# def getDirection(view):
# 	(x, y) = (view.GetXPos(), view.GetYPos())
# 	if x == 0 and y == 0:
# 		origin = [(x,y)]
# 		file = open(filename, 'w')
# 		cPickle.dump(origin, file)
# 		file.close()
# 		return random.randint(0,3)

# 	# open file, get list, append current location, dump to file
# 	file = open(filename, 'r')
# 	# list of coordinate tuples we've visited before
# 	history = cPickle.load(file)
# 	#print history
# 	file.close()

# 	history.append((x, y))

# 	file = open(filename, 'w')
# 	cPickle.dump(history, file)
# 	file.close()

# 	candidateList = [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]
# 	for el in candidateList:
# 		if el in history:
# 			candidateList.remove(el)

# 	if len(candidateList) == 0:
# 		return random.randint(0,3)

# 	dists = [abs(coord[0]**2 + coord[1]**2) for coord in candidateList]

# 	def find_indices(lst, condition):
# 	   return [i for i, elem in enumerate(lst) if condition(elem)]

# 	minIndex = find_indices(dists, lambda e: e == min(dists))
# 	minIndex = random.randint(0,len(minIndex))

# 	newSquare = candidateList[minIndex]
# 	if x == newSquare[0]:
# 		if y+1 == newSquare[1]:
# 			return 0 # UP
# 		else:
# 			return 2 # DOWN
# 	else:
# 		if x+1 == newSquare[0]:
# 			return 3 # RIGHT
# 		else:
# 			return 1 # LEFT

# 	return random.randint(0, 3)