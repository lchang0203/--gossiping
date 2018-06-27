import random
import matplotlib.pyplot as plt

class node:
    def __init__(self, status):
        self.infected = status

currentRound = 0
nodes = []
isolated = 0
amount = int(input("输入节点总数："))
infected = int(input("输入感染的节点数："))
tempY=[]
tempX=[]
for i in range(0, amount):
    if i < infected:
        nodes.append(node(True))
    else:
        nodes.append(node(False))

while infected != amount:
        for key in range(amount):
            currentNode = random.randint(0, amount - 1)
            while currentNode == key:
                currentNode = random.randint(0, amount - 1)
            if nodes[key].infected == True:
                if nodes[currentNode].infected == False:
                    nodes[currentNode].infected = True
                    infected = infected + 1

        print("Round" + str(currentRound + 1))
        print("感染：" + str(infected))
        print("Isolated:" + str(isolated))
        currentRound = currentRound + 1
        tempY.append(infected)
        tempX.append(currentRound)

plt.plot(tempX,tempY,'ro')
plt.show()