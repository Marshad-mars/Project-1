def Number_Guess():
    import random
    print("Guess any number game!")

    #verify-
    q=str(input("Do you wanna play this game?(yes/no): "))
    if(q.lower() != "yes"):
        print("Thankyou for visiting this site :)")
        quit()
    else:
        print()
        num=random.randrange(0,11)
        while True:
            guess_ver=str(input("Do you wanna guess the number?(yes/no): "))
            if(guess_ver.lower() == "yes"):
                break 
            else:
                print("Please guess a number")
            print()
            #return guess_ver
        while True:
            guess=int(input("Guess your number between 0 to 10: "))
            if(guess <= 10):    
                break
            else:
                print("Please a guess a number which is less then or equal to 10")
            return guess 
        if(guess == num):
            print("That was a fair guess!","\n","Actually your random number is",num)
        else:
            print("Better luck next time, your guessing is wrong and it is actially:",num)
            #print(num)
            #return guess
        if(guess < num):
            print("And Your guessing is less then the random number.")
        else:
            print("And Your guessing is grater then the random number.")
            return guess 
        return num 
Number_Guess() 