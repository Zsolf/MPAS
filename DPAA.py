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
NUMBER_OF_ITEMS = lines[0]
BIN_CAPACITY = lines[1]
WEIGHTS = []

for i in range(2, len(lines)):
    WEIGHTS.append(lines[i])
#------------------------------------#
    

#Algorithm
    
bins = []
bin1 = [] #capacity = BIN_CAPACITY
bins.append(bin1)

#First fit







file.close()