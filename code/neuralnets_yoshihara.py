from collections import defaultdict
error = defaultdict(float)
weights = defaultdict(float)
UpdatedWeights = defaultdict(float)
nodeVal = defaultdict(float)
nodeValues = [1,2,0.7311,0.0179,0.9933,0.8387]

for i in range(1,6):
	nodeVal[i] = nodeValues[i-1] 

error[6] = -0.11346127339699999
error[5] = -0.0011326458827956695
weights[56] = 0.37298917134759924
UpdatedWeights[56] = weights[56]
weights[36] = .2
weights[46] = .7

weights[13] = -3
weights[14] = 2
weights[15] = 4

weights[23] = 2
weights[24] = -3
weights[25] = 0.5

def getErrorLastNeuron(Output,Target):
	return Output*(1-Output)*(Target-Output)

def updateWeight(Weight,Error,l,Output):
	return Weight + (Error*l*Output)

def getErrorHiddenLayer(Output,weights):
	return Output*(1-Output)*reduce(lambda x,y:x+y,[i*j for i,j in weights])

error[4] = getErrorHiddenLayer(nodeVal[4],[(weights[46],error[6])])
error[3] = getErrorHiddenLayer(nodeVal[3],[(weights[36],error[6])])

UpdatedWeights[46] = updateWeight(weights[46],error[6],10,nodeVal[4])
UpdatedWeights[36] = updateWeight(weights[36],error[6],10,nodeVal[3])

error[2] = getErrorHiddenLayer(nodeVal[2],[(weights[23],error[3]),(weights[24],error[4]),(weights[25],error[5])])
error[1] = getErrorHiddenLayer(nodeVal[1],[(weights[13],error[3]),(weights[14],error[4]),(weights[15],error[5])])


UpdatedWeights[25] = updateWeight(weights[25],error[5],10,nodeVal[2])
UpdatedWeights[24] = updateWeight(weights[24],error[4],10,nodeVal[2])
UpdatedWeights[23] = updateWeight(weights[23],error[3],10,nodeVal[2])

UpdatedWeights[15] = updateWeight(weights[15],error[5],10,nodeVal[1])
UpdatedWeights[14] = updateWeight(weights[14],error[4],10,nodeVal[1])
UpdatedWeights[13] = updateWeight(weights[13],error[3],10,nodeVal[1])

for key in error.keys():
	print "error_%s = %s" % (str(key),str(error[key])) 

for key in UpdatedWeights.keys():
	print "w_%i = %f" % (int(key),UpdatedWeights[key])