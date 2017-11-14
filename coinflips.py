###################################
# Alvin Shrestha
# UP826133
###################################


from random import randint

def main():
    noOfFlips = getInputs()
    
    heads, tails = simulateFlips(noOfFlips)
    
    displayResults(heads, tails)
    
def getInputs():
    userInput = eval(input("Enter the number of times you want to flip the coin: "))
    return userInput

def simulateFlips(noOfFlips):
    heads = 0
    tails = 0
    
    for counter in range(noOfFlips):
        
        currentFlip = randint(1, 2)
        
        if(currentFlip == 1):
            heads+=1
            
        if(currentFlip == 2):
            tails+=1

    return heads, tails
    
def displayResults(heads, tails):
    print("Heads: ", heads)
    print("Tails: ", tails)

main()