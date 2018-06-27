import random
# import matplotlib.pyplot as plt

class node:
    interset = 100
    def __init__(self, status, value):
        self.infected = status
        self.value = value


k =0.96
currentTimes = 0
nodes = []
isolated = 0
amount = int(input("输入节点总数："))
infected = int(input("输入感染的节点数："))
tempY=[]
tempX=[]
valueX=[]
valueY=[]
for i in range(0, amount):
    valueRand=random.randint(0,10)
    if i < infected:
        nodes.append(node(True, valueRand))
    else:
        nodes.append(node(False, valueRand))

while isolated < infected & infected != amount:
        isolated = 0
        for key in range(amount):
            #currentNode = 0
            currentNode = random.randint(0, amount - 1)
            while currentNode == key:
                currentNode = random.randint(0, amount - 1)
            
            average = (nodes[key].value+nodes[currentNode].value)/2
            nodes[key].value=average
            nodes[currentNode].value=average

            if nodes[key].infected == True:
                if nodes[key].interset == 0:
                    isolated = isolated + 1
                if nodes[currentNode].infected == False:
                    lottery = random.randint(0, 99)
                    if lottery < nodes[key].interset:
                        nodes[currentNode].infected = True
                        infected = infected + 1
                else:
                    nodes[key].interset = nodes[key].interset *k
            else:
                if nodes[currentNode].infected == True:
                    lottery = random.randint(0, 99)
                    if lottery < nodes[currentNode].interset:
                        nodes[key].infected = True
                        infected = infected + 1

        print("Round" + str(currentTimes + 1))
        print("感染：" + str(infected))
        print("Isolated:" + str(isolated))
        currentTimes = currentTimes+ 1
        tempY.append(infected)
        tempX.append(currentTimes)
i=1
for key in nodes:
    valueY.append(key.value)
    valueX.append(i)
    i=i+1

valueX.append(i)
valueY.append(10)
valueX.append(i+1)
valueY.append(0)
plt.subplot(121)
plt.plot(valueX,valueY,'ro')
plt.subplot(122)
plt.plot(tempX,tempY,'ro')
plt.show()