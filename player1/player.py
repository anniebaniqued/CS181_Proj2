import common
import random
import cPickle
import neural_net
import neural_net_impl
import game_interface

filename = "moves.txt"

#def get_move(view):
	#return common.get_move(view)

# figure out direction
def get_move(view):
  state = 0
  testNum = 0
  direction = getDirection(view)
  if view.GetPlantInfo() == game_interface.STATUS_UNKNOWN_PLANT:
	  while testNum < 3:
	  	(output_probs, result) = test(view)
	  	if output_probs[1]>=0.97:
	  		print "Classified as: Poisonous"
	 		return (direction, False)
	  	if result == 1:
	  		state -= 1
	  	else:
	  		state += 1
	  	if state == 2:
	  		print "Classified as: Nutritious"
	  		return (direction, True)
	  	if state == -2:
	  		#return (direction, False)
	  		print "Classified as: Poisonous"
	  		return (direction, True)
	  	testNum += 1

	  if state > 0 :
	  	print "Classified as: Nutritious"
	  	return (direction, True)
	  else:
	  	#return (direction, False)
	  	print "Classified as: Poisonous"
	  	return (direction, True)
  else: 
  	#return (direction, False)
  	return (direction, False)

# output 0 for poisonous, 1 for nutritious
def test(view):
	nn = neural_net_impl.HiddenNetwork()
	trainedWeights = [-0.37394162753934884, 0.008417890433957966, -0.41602698324960685, -0.40319811718621834, -0.34640657231565125, 0.02923567730036491, 0.003369318686340195, -0.42183363772706095, -0.41497320617139494, -0.42812799626540804, -0.23583708196262046, -0.3354762611906808, -0.32519043377256085, -0.4182721345958921, -0.4139123101547406, -0.43587022276233206, -0.3760841709637373, -0.10833192289521516, -0.025753238092162626, -0.3243752932346408, 0.04381710433091638, 0.01004873238684757, -0.412405100183634, 0.02952841016995824, -0.0011462852145902153, -0.20770298500955978, -0.3311964567074992, -0.3060752789969199, -0.2941894473025382, -0.22878342307747965, -0.21486489186072505, -0.3601001694445269, -0.1091110120081313, -0.006604324120645899, -0.3733786765049916, -0.12563665948333735, -0.0035316852318625336, 0.3389588388287541, 0.007974179902291581, 0.26771485509551407, 0.3495295173910134, 0.271635590474621, -0.2674818313408928, -0.22471291958804152, 0.26267214576849585, 0.3501073454596171, 0.34057215864372636, 0.18926212391638475, 0.15641234089732123, 0.12947048803301575, 0.23848080538255614, 0.2913870338479804, 0.22317118429948288, 0.386443379361676, 0.032267614011625353, -0.04665145428891137, 0.26943795975151197, -0.160363005053877, -0.23645766703934112, 0.22548269348434327, -0.23013644287415164, -0.21155911444950914, 0.07202921223686903, -0.025586932227896306, 0.13985117925453605, 0.14353957029334063, 0.11505446753391436, 0.08195443461204448, 0.42537274028352845, 0.06305289292843477, -0.14130224274170625, 0.27206739238425953, 0.11088503199796718, -0.147494618747263, -1.9217447617538717, -0.0027560644791257147, -1.8706356357724327, -2.2503014347819956, -1.3330926034629837, 7.37525360972735, 6.756643270054489, -1.6277173853200189, -2.5815679046228093, -2.9054867445412174, 0.3862664315116735, 0.8126735596411665, 1.3258098276465349, -1.2059604759077949, -1.9755599589565709, -1.77325811804889, -5.2058907507682886, 0.17142956777239815, 1.8827201311977066, -0.6552479236790246, 5.705483284891082, 6.656087289305911, -0.7906331511657533, 7.165884316046883, 7.41075141076856, 1.3084469548885058, 3.25081498953044, 1.5171403849192089, 0.6156651347850798, 1.8621888909863302, 2.004783811825019, -5.335244798298684, 0.13274025412134183, 3.5240495074999703, -3.2613822791813614, 0.3398374222888009, 3.986112074776255, -0.4433233459337292, -0.004428032284334262, -0.49882306936141607, -0.48002371007570577, -0.4072591612941408, 0.34123319251090256, 0.3109464041780269, -0.4903525207096212, -0.519577673234908, -0.5291181022233232, -0.20721575300854223, -0.2890195276960668, -0.26303197936334627, -0.5095251468433036, -0.48588970681523114, -0.5574217886654902, -0.5853466363584223, -0.09605777300802003, 0.0803030156621646, -0.38440686691648285, 0.3630983655244027, 0.2926072842915069, -0.4760688408199047, 0.361219459312146, 0.31809584309486366, -0.16519435379870945, -0.24875255761003506, -0.27748635586825876, -0.33010686348197155, -0.10230376434889023, -0.10219522875477786, -0.6160197505472096, -0.11374000152959934, 0.1099642940580237, -0.5803542619311306, -0.07430298281919587, 0.15520641430877066, -0.9255387052284582, -0.006112672549701448, -0.8553000773141702, -1.0922535566475542, -0.5659984665455384, 3.293480278392143, 2.9840800504900566, -0.7575626115654807, -1.2958293500133746, -1.326545710314233, 0.18016998855523508, 0.39616344553584665, 0.586556911645849, -0.5655690092833368, -0.8902310252204588, -0.8533059093027312, -2.293664151082615, 0.1950189402502635, 0.7313432799801362, -0.2601485228433012, 2.5309199852616566, 2.9621568238757807, -0.44923102947708504, 3.355796211072677, 3.4914920197280783, 0.6077236281013324, 1.449195215268799, 0.6613119780126246, 0.07281362569776863, 0.8060419454861427, 1.0511741736647806, -2.549458789777637, -0.06779160806446449, 1.5404032791170768, -1.4591097365902466, 0.17421873170484511, 1.7793202792872527, 3.196235238546957, -0.0015851070394307509, 5.586834769440259, -7.644674605246018, 2.5054190925080477, -3.0313164213398704, -3.1807819495841954, -0.006616755897966218, -5.5783585662753765, 7.6435052345704255, -2.5130339003002296, 3.032476317676825]
	for i in range(len(nn.network.weights)):
		nn.network.weights[i].value = trainedWeights[i]
	
	# 5 samples
	summed = view.GetImage()
	for i in range(1):
		next = view.GetImage()
		summed = [a + b for a,b in zip(summed, next)]
	nodeVals = neural_net.Input()
	for el in summed:
		nodeVals.values.append(el/2.0)
	
	"""
	img = view.GetImage()
	nodeVals = neural_net.Input()
	for el in img:
		nodeVals.values.append(el)
"""
	neural_net_impl.FeedForward(nn.network, nodeVals)

	#resultClass = nn.GetNetworkLabel()
	output_probs = nn.GetNetworkLabel()
	print output_probs
	resultClass = output_probs.argmax(axis=0)
	print "classification: " + str(resultClass)
	return (output_probs, resultClass)

# right now, random int
def getDirection(view):
	(x, y) = (view.GetXPos(), view.GetYPos())
	"""
	if x == 0 and y == 0:
		origin = [(x,y)]
		file = open(filename, 'w')
		cPickle.dump(origin, file)
		file.close()
		return random.randint(0,3)

	# open file, get list, append current location, dump to file
	file = open(filename, 'r')
	# list of coordinate tuples we've visited before
	history = cPickle.load(file)
	file.close()

	history.append((x, y))

	file = open(filename, 'w')
	cPickle.dump(history, file)
	file.close()
"""
	if not hasattr(view, "hist"):
		view.hist = [(x,y)]
	else:
		view.hist.append((x,y))
	history = view.hist



	candidateList = [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]
	candCopy = [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]
	for el in candidateList:
		if el in history:
			candidateList.remove(el)

	#if been everywhere, go the max distance maybe - used to be random
	if len(candidateList) == 0:
		dists = [abs(coord[0]**2 + coord[1]**2) for coord in candCopy]
		maxIndex = dists.index(max(dists))
		newSquare = candCopy[maxIndex]
	else: 
		epsilon = 0.3
		rand = random.uniform(0,1)
		if rand > epsilon:
			dists = [abs(coord[0]**2 + coord[1]**2) for coord in candidateList]
			minIndex = dists.index(min(dists))
			newSquare = candidateList[minIndex]
		else:
			randIndx = random.randint(0,len(candidateList) - 1)
			newSquare = candidateList[randIndx]
	#print "candidate length " + str(len(candidateList))
	#print "minIndex: " + str(minIndex)
	#print "candidateList: " + str(candidateList)
	#print "dists: " + str(dists)
	
	if x == newSquare[0]:
		if y+1 == newSquare[1]:
			return 0 # UP
		else:
			return 2 # DOWN
	else:
		if x+1 == newSquare[0]:
			return 3 # RIGHT
		else:
			return 1 # LEFT




	"""
	def find_indices(lst, condition):
	   return [i for i, elem in enumerate(lst) if condition(elem)]

	minIndex = find_indices(dists, lambda e: e == min(dists))"""


	"""
	candidateList = [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]
	for el in candidateList:
		if el in history:
			candidateList.remove(el)

	if len(candidateList) == 0:
		return random.randint(0,3)

	dists = [coord[0]**4 + coord[1]**4 for coord in candidateList]
	minIndex = dists.index(min(dists))

	newSquare = candidateList[minIndex]
	if x == newSquare[0]:
		if y+1 == newSquare[1]:
			return 0
		else:
			return 1
	else:
		if x+1 == newSquare[0]:
			return 3
		else:
			return 2

	return random.randint(0, 3)
	"""
