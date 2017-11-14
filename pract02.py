\# Pract02
# Alvin Shrestha
# UP826133
import math;
def circumferenceOfCircle():
    r=eval(input("Enter the radius of the circle"))
    print("The circumference of the circle is: ", 2*math.pi*r)
    
def areaOfCircle():
     r=eval(input("Enter the radius of the circle"))
     print("The area of the circle is: ", math.pi*r**2);
     
def returnAreaOfCircle(r):
    return math.pi*r**2;
    
     
def costOfPizza():
    d=eval(input("Enter the diameter of the circle in cm"));
    print("The total cost is: ", returnAreaOfCircle(d/2)*1.5, "p");
    
def slopeOfLine():
    x1=eval(input("Enter x1 "));
    y1=eval(input("Enter y1 "));
    x2=eval(input("Enter x2 "));
    y2=eval(input("Enter y2 "));
    print("The slope is", float((y2-y1)/(x2-x1)));

def distanceBetweenPoints():
    x1=eval(input("Enter x1 "));
    y1=eval(input("Enter y1 "));
    x2=eval(input("Enter x2 "));
    y2=eval(input("Enter y2 "));
    print("The distance between the points is: ",math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
    
def travelStatistics():
    avSpeed=eval(input("Enter the average speed in km/hour"));
    duration=eval(input("Enter the duration in hours"));
    totalD=avSpeed*duration;
    print("The total distance travelled is: ",totalD, "The amount of fuel used is: ", totalD/5, "l");
    
def sumOfNumbers():
    total=0;
    print(total);
    no=eval(input("How many positive numbers do you want to add up? "));
    for counter in range(1,no+1):
        total=total+counter;
    print("The sum is: ", total);
    
def averageOfNumbers():
   no=eval(input("How many numbers do you want the average of?"))
   sum=0;
   for counter in range(0,no):
       inp=eval(input("Enter the number: "))
       sum=sum+inp
   print(sum/no)

def selectCoins():
    pp2=pp1=p50=p20=p10=p5=p2=p1=0;
   
    amount=eval(input("Enter the amount in pence "))
    if(amount>=200):
        pp2=amount//200;
        amount=amount%200;
    if(amount>=100):
        pp1=amount/100;
        amount=amount%100;
    if(amount>=50):
        p50=amount//50;
        amount=amount%50;
    if(amount>=20):
        p20=amount//20;
        amount=amount%20;
    if(amount>=10):
        p10=amount//10;
        amount=amount%10;
    if(amount>=5):
        p5=amount//5;
        amount=amount%5;
    if(amount>=2):
        p2=amount//2;
        amount=amount%2;
    p1=amount;
    print(pp2, "x", "£2");
    print(pp1, "x", "£1");
    print(p50, "x", "50p");
    print(p20, "x", "20p");
    print(p10, "x", "10p");
    print(p5, "x", "5p");
    print(p2, "x", "2p");
    print(p1, "x", "1p");
                                
def test():
    print(int(7.6));
        
    