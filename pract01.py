# Practical Worksheet 1: Getting started with Python
# Alvin Shrestha, 826133

def sayHello():
    print("Alvin Shrestha")
    
def sayHello2():
    print("Hello");
    print("World");

def euros2pounds():
    euros=input("Enter the amout in euros");
    pounds= float(euros) * 1.15;
    return pounds;
    
def changeCounter():
    oneP=input("How many 1p coins do you have?"); 
    twoP=input("How many 2p coins do you have?");
    fiveP=input("How manu 5p coins do you have?");
    totalAmount= eval(oneP)+ eval(twoP)*2+ eval(fiveP)*5;
    print(totalAmount, "p");
    
def tenHellos():
    for counter in range(1, 11):
        print("hello, world!");
        
def weightsTable():
   for counter in range (0,101,10):
       kilos2pounds(counter);

def count():
    for i in range(1,11):
        print(i)

def kilos2pounds(kilos):
    pounds = 2.2 * float(kilos);
    print(kilos,"The weight in pounds is", pounds)
    
def futureValue():
    amount=float(input("Enter the initial amount."));
    noOfYears=eval(input("Enter the no. of years, the amount is to be invested."));
    for counter in range (0,noOfYears):
        amount=amount+ amount*5.5/100;
    print(amount);
        

