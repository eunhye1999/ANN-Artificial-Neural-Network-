import numpy as np
import random
class FixedIncrement():

	def __init__(self,xin,traget):
		self.j = 0
		self.xin = xin
		self.traget = traget # [c2,c1,c1,c1] or [0,1,1,1] OR gate
		self.weight = np.array([0,0,0])
		self.mainFixed()

	# if traget <= 0 return false for update Weight
	def checkTraget(self,i): 
		# d*Wt*X
		# output 1 is c1(d = +1)
		#		 0 is c2(d = -1)
		d = self.traget[i]
		Wt = self.weight.transpose()
		X = np.array(self.xin[i])
		result = sum(d*Wt*X)
		# print("ceheck : %d*%s*%s = %d" % (d, Wt, X,result))
		if(result <= 0):
			return False
		return True

	def updateWeight(self,i):
		# w(n) = w(n-1) + dX
		d = self.traget[i]
		X = np.array(self.xin[i])
		self.weight = self.weight + d*X
		self.j += 1
		# print("update : %s(%d)" % (self.weight,self.j,))
		# print()

	def checkFinish(self,i):
		if(i < 3):
			return i+1
		else:
			return 0

	def equation(self):
		print("equation: %d+%dx+%dy" % (self.weight[0]*-1,self.weight[1],self.weight[2]))
		equa={'x0':self.weight[0]*-1,'x1':self.weight[1],'x2':self.weight[2]}
		return equa

	def mainFixed(self):
		check = 0
		upWeight = 0
		i = 0
		while(1):
			upWeight += 1
			if(False == self.checkTraget(i)):
				self.updateWeight(i)
				check=0
			else:
				check+=1
				if(check == 4):
					# print(upWeight)
					return 0
			i = self.checkFinish(i)

# d = [-1, -1, -1, 1]   # AND
d = [-1, 1, 1, 1]     # OR
# d = [1, 1, 1, -1]     # NAND
# d = [1, -1, -1, -1]   # NOR
# d = [-1, 1, 1, -1]    # XOR
# d = [1, -1, -1, 1]    # XNOR

xin = [[-1,0,0],
		[-1,0,1],
		[-1,1,0],
		[-1,1,1]]
or_gate = FixedIncrement(xin,d)
equa = or_gate.equation()
print(equa)