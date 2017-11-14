from Padlock import Padlock

def main():
    import random
    pattern = random.randint(0,9999)
    print(pattern)
    padlock1 = Padlock(pattern)
    
    for i in range(10):
        str = "Guess the pattern. You have ", 10-i," attempts remaining."
        
        userInput = eval(input(str))
        padlock1.openLock(userInput);
        
        if not padlock1.isLocked:
            break
    if padlock1.isLocked:
        print("Failed to open the lock")
    else:
        print("You win.")
        
main()