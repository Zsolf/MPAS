#Densest Point Avoidance Algorithm
#Legsűrűbb pont elkerülő algoritmus
#------------------------------------#


#BPP File reading
file = open("BPP_1000_1000_0.1_0.7_0.txt", "r")
lines = file.read().splitlines()
#------------------------------------#


#In the BPP format:
#Number of items (n)
#Capacity of the bins (c)
#For each item j (j = 1,...,n):
#Weight (wj)


#Constants init
NUMBER_OF_ITEMS = int(lines[0])
BIN_CAPACITY = int(lines[1])
WEIGHTS = []

for i in range(2, len(lines)):
    WEIGHTS.append(int(lines[i]))
#------------------------------------#
    

#Algorithm
    
bins = []
bin1 = [0] * BIN_CAPACITY #capacity = BIN_CAPACITY
bins.append(bin1)

#First fit

def load(bin, weight):
    weightCount = 0
    for i in range(0,len(bin)):
          if(bin[i] == 0 and weightCount < weight):
            bin[i] = weight
            weightCount+=1

def checkThisBin(bin, currentWeight):
    available = 0
    for space in bin:
        if (space == 0):
            available+=1
            if (available == currentWeight):
                break
    if (available == currentWeight):
        load(bin,currentWeight)
        return 0
    return 1
        


def checkBins(currentWeight):
    for bin in bins:
        if (checkThisBin(bin,currentWeight)==0):
            break
        newBin = [0]*1000
        bins.append(newBin)
        checkThisBin(newBin,currentWeight)
        break

for i in range(0, len(WEIGHTS)):
    
    currentWeight= WEIGHTS[i]
    checkBins(currentWeight)

          
     

print(bins[890])





file.close()