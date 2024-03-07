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
    
#WEIGHTS = [700,700,250,240]
score = [0] * BIN_CAPACITY
bins = []
bin1 = [0] * BIN_CAPACITY #capacity = BIN_CAPACITY
bins.append(bin1)

#First fit

#load as odd bin
def loadOdd(bin, weight):
    weightCount = 0
    for i in range(0,len(bin)):
          if(bin[i] == 0 and weightCount < weight):
            bin[i] = weight
            weightCount+=1

#load as even bin
def loadEven(bin, weight):
    weightCount = 0
    for i in reversed(range(0,len(bin))):
          if(bin[i] == 0 and weightCount < weight):
            bin[i] = weight
            weightCount+=1

#check as odd bin
def checkThisBinOdd(bin, currentWeight):
    available = 0
    for space in bin:
        if (space == 0):
            available+=1
            if (available == currentWeight):
                break
    if (available == currentWeight):
        countScore()
        if(bin[0] == 0 & bin[len(bin)-1] == 0):           #if the bin is brand new, follow the odd-even pattern
             loadOdd(bin,currentWeight)
             return 0
        path = chooseMinimumResult(bin,currentWeight)  #if the bin is not new, follow the minimum density path
        if (path == 0):
            loadEven(bin,currentWeight)
            return 0
        elif (path == 1):
            loadOdd(bin,currentWeight)
            return 0
        else:
            loadEven(bin,currentWeight)
            return 0
    return 1
        
#check as even bin (reversed)
def checkThisBinEven(bin, currentWeight):
    available = 0
    for space in reversed(bin):
        if (space == 0):
            available+=1
            if (available == currentWeight):
                break
    if (available == currentWeight):
        
        countScore()
        if(bin[0] == 0 & bin[len(bin)-1] == 0): #if the bin is brand new, follow the odd-even pattern
            loadEven(bin,currentWeight)
            return 0
        path = chooseMinimumResult(bin,currentWeight)    #if the bin is not new, follow the minimum density path
        if (path == 0):
            loadEven(bin,currentWeight)
            return 0
        elif (path == 1):
            loadOdd(bin,currentWeight)
            return 0
        else:
            loadOdd(bin,currentWeight)
            return 0
    return 1


def checkBins(currentWeight):
    oddOrEven = 1 #even or odd tracker
    for bin in bins:
        if(oddOrEven % 2 != 0): #checks if even
            if (checkThisBinOdd(bin,currentWeight)==0):
                break
            if(bin == bins[len(bins)-1]): #new bin if there is no suitable bin
                newBin = [0]*BIN_CAPACITY
                bins.append(newBin)
                checkThisBinEven(newBin,currentWeight)
                break
        else:
            if (checkThisBinEven(bin,currentWeight)==0): #checks if we found a place for current weight in one of the bins
                break
            if(bin == bins[len(bins)-1]): #new bin if there is no suitable bin
                newBin = [0]*BIN_CAPACITY
                bins.append(newBin)
                checkThisBinOdd(newBin,currentWeight)
                break
        oddOrEven+=1

#counts current score
def countScore():
    global score 
    score = [0] * BIN_CAPACITY  #re-initalize scores
    for pos in range(0,len(score)): #count scores
        for bin in bins:
            if(bin[pos] != 0):
                score[pos]+=1
    asd = 0

#decision based on least density score output
def chooseMinimumResult(bin,weight):
    tempScoreForEven = score.copy()   
    tempScoreForOdd = score.copy()
    weightCount = 0
    for i in reversed(range(0,len(bin))):
        if(bin[i] == 0 and weightCount < weight):
            tempScoreForEven[i]+=1
            weightCount+=1
    weightCount = 0
    for i in range(0,len(bin)):
        if(bin[i] == 0 and weightCount < weight):
            tempScoreForOdd[i]+=1
            weightCount+=1
    if(max(tempScoreForOdd) > max(tempScoreForEven)): #check which path leads to least maximum score
        return 0
    elif(max(tempScoreForOdd) < max(tempScoreForEven)):
        return 1
    else:
        return -1


#iterate through weights Algorithm starts here
for i in range(0, len(WEIGHTS)):
    
    currentWeight= WEIGHTS[i]
    checkBins(currentWeight)

          
#test
countScore()
print(score)





file.close()