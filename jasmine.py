from keras.models import Model 
import numpy as np

class Population:
	def __init__(this):
		this.models = []
		this.scores = []
		this.popSize = 100
		this.mutate = 0.1
		this.config = None

	def initModels(this,popsize=None):
		if popsize != None:
			this.popSize = popsize

		this.models = []
		this.score = []
		for i in range(this.popSize):
			this.models.append(Model.from_config(this.config))
			this.score.append(0)

	def setModelConfig(this,config):
		this.config = config

	def selectRanking(this):
		for i in range(len(this.models)):
			for j in range(i + 1,len(this.models)):
				if this.scores[i] < this.scores[j]:
					this.scores[i] , this.scores[j] = this.scores[j] , this.scores[i]
					this.models[i] , this.models[j] = this.models[j] , this.models[i]

		this.models , this.scores = this.models[:this.popSize] , this.scores[:this.popSize]

	def crossUniform(this,newinds = 20):
		for i in range(newinds):
			weight = np.zeros((this.models[0].get_weights.shape))
			a,b = np.random.randint(0,this.popSize),np.random.randint(0,this.popSize)
			left,right = this.models[a].get_weights , this.models[b].get_weights
			for n,l,r in weight,left,right:
				if np.random.randn() < 0:
					n = l
				else:
					n = r
			this.models.append(weight)