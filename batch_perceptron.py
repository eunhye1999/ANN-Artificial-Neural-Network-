import numpy as np
import random
class BatchPerceptron():

	def __init__(self,xin,traget,learning):
		self.lrate = learning
		self.xin = xin
		self.traget = traget 
		self.weight = np.array([0,0,0])
		self.mainBatch()

	def updateWeight(self,array):
		for i in array:
			self.weight = self.weight.transpose() + (self.lrate*self.traget[i]*np.array(self.xin[i]))
		# print(self.weight)

	def checkTragetAll(self):
		pout = []
		w=self.weight
		for i in range(0,len(self.xin)):
			# print("ceheck : %d*%s*%s = %d" % (d[i], w, self.xin[i],sum(self.traget[i]*w*self.xin[i])))
			if(sum(self.traget[i]*w*np.array(self.xin[i])) <= 0):
				pout.append(i)
		return pout
	def equation(self):
		print("equation: %f+%dx+%dy" % (self.weight[0]*-1.0,self.weight[1],self.weight[2]))
		equa={'x0':self.weight[0]*-1,'x1':self.weight[1],'x2':self.weight[2]}
		return equa 

	def mainBatch(self):
		i = 0
		while(1):
			result = self.checkTragetAll()
			if(result == []):
				return 0
			else:
				self.updateWeight(result)



d = [-1, -1, -1, 1]   # AND
# d = [-1, 1, 1, 1]     # OR
# d = [1, 1, 1, -1]     # NAND
# d = [1, -1, -1, -1]   # NOR
# d = [-1, 1, 1, -1]    # XOR
# d = [1, -1, -1, 1]    # XNOR

xin = [[-1,0,0],
		[-1,0,1],
		[-1,1,0],
		[-1,1,1]]
or_gate = BatchPerceptron(xin,d,0.5)
equa = or_gate.equation()
print(equa)