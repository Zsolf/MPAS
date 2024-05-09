#Densest Point Avoidance Algorithm
#Legsűrűbb pont elkerülő algoritmus
#------------------------------------#
import random
import time


#BPP File reading
#file = open("BPP_1000_1000_0.1_0.7_0.txt", "r")
#lines = file.read().splitlines()
#------------------------------------#


#In the BPP format:
#Number of items (n)
#Capacity of the bins (c)
#For each item j (j = 1,...,n):
#Weight (wj)


#Constants init
NUMBER_OF_ITEMS = 0
BIN_CAPACITY = 0
WEIGHTS = []


#for i in range(2, len(lines)):
#    WEIGHTS.append(int(lines[i]))
#random.shuffle(WEIGHTS)
#------------------------------------#
    

#Algorithm
    
#WEIGHTS = [700,700,250,240]
score = [0] * 1
bins = []
bin1 = [] 

#First fit

#load as odd bin
def loadOdd(bin, weight):
    weightCount = 0
    for i in range(0,len(bin)):
          if(bin[i] == 0 and weightCount < weight):
            bin[i] = weight
            weightCount+=1

#check as odd bin
def checkThisBinOdd(bin, currentWeight):
    loadOdd(bin,currentWeight)
    return 0



def checkBins(currentWeight):
    binSpaces = [0] * len(bins)
    oddOrEven = 1
    for bin in bins:
        available = 0
        for space in bin:
            if (space == 0):
                available+=1

        if(available >= currentWeight):
            binSpaces[oddOrEven-1]=available-currentWeight
        else:
            binSpaces[oddOrEven-1]= -1
        oddOrEven+=1

    posAndValue = [-2,-2]
    position = 0
    for space in binSpaces:
        if (space > posAndValue[1] and space != -1):
            posAndValue = [position, space]
        position+=1

    if(posAndValue[0] == -2 and posAndValue[1] == -2):
        newBin = [0]*BIN_CAPACITY
        bins.append(newBin)
        checkThisBinOdd(newBin,currentWeight)
        return 0


    if (checkThisBinOdd(bins[posAndValue[0]],currentWeight)==0):
        return 0





#counts current score
def countScore():
    global score 
    score = [0] * BIN_CAPACITY  #re-initalize scores
    for pos in range(0,len(score)): #count scores
        for bin in bins:
            if(bin[pos] != 0):
                score[pos]+=1
    asd = 0



def main(file_name):

    start = time.time()

    global NUMBER_OF_ITEMS
    global BIN_CAPACITY
    global WEIGHTS


    file = open(file_name, "r")
    lines = file.read().splitlines()

    NUMBER_OF_ITEMS = int(lines[0])
    BIN_CAPACITY = int(lines[1])
    WEIGHTS = []

    for i in range(2, len(lines)):
        WEIGHTS.append(int(lines[i]))

    random.shuffle(WEIGHTS)

    global score
    global bins
    global bin1

    score = [0] * BIN_CAPACITY
    bins = []
    bin1 = [0] * BIN_CAPACITY #capacity = BIN_CAPACITY
    bins.append(bin1)

    for i in range(0, len(WEIGHTS)):
        
        currentWeight= WEIGHTS[i]
        checkBins(currentWeight)

    #test
    countScore()
    #print(score)
    #print("highest: " + str(max(score)))
    count = 0
    for sc in score:
        if (sc == max(score)):
            count+=1
    #print("times: " + str(count))
    #print("length:" + str(len(bins)))
    file.close()

    end = time.time()
    return [max(score), end-start, len(bins)]

