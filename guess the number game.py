from random import randint
lives = 10
rand = randint(1,100)

print("Guess the number between 1 and 100!")
print("You have",str(lives),"lives!")

def get(lives):
    if lives>2:
        inp = int(input("\nEnter number between 1 ahd 100: ",))
        if inp > 100:
            print("\nThe number is higher than 100!")
            get(lives)
        elif inp < 0:
            print("\nThe number is lower than 0!") 
            get(lives)
        else:  
            if rand == inp:
                print("\nCorect!")
                print("You alreday have",str(lives),"lives!")
            else:
                lives = lives - 1
                print("\nIncorect!")
                print("You have",str(lives),"lives left!")
                if rand > inp:
                    print("The number is higher than",str(inp)+"!")
                else:
                    print("The number is lower than",str(inp)+"!")
                get(lives)
    elif lives==2:
        inp = int(input("\nEnter number between 1 ahd 100: ",))
        if inp > 100:
            print("\nThe number is higher than 100!")
            get(lives)
        elif inp < 0:
            print("\nThe number is lower than 0!") 
            get(lives)
        else:  
            if rand == inp:
                print("\nCorect!")
                print("You alreday have",str(lives),"live!")
            else:
                lives = lives - 1
                print("\nIncorect!")
                print("You have",str(lives),"live left!")
                if rand > inp:
                    print("The number is higher than",str(inp)+"!")
                else:
                    print("The number is lower than",str(inp)+"!")
                get(lives)
    elif lives==1:
        inp = int(input("\nEnter number between 1 ahd 100: ",))
        if inp > 100:
            print("\nThe number is higher than 100!")
            get(lives)
        elif inp < 0:
            print("\nThe number is lower than 0!") 
            get(lives)
        else:  
            if rand == inp:
                print("\nCorect!")
                print("You alreday have",str(lives),"live!")
            else:
                lives = lives - 1
                print("\nIncorect!")
                print("You have",str(lives),"lives left!")
                if rand > inp:
                    print("The number is higher than",str(inp)+"!")
                else:
                    print("The number is lower than",str(inp)+"!")
                get(lives)
    else:
        print("\nYou lose!")


get(lives)
