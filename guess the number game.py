#  Напишете програма в която се създава числов списък с n на брой елементи, 
#  като n се въвежда от потребителя и n е цяло число между 30 и 100 (30 < n < 100). 
#  Да се провери входа (дали условието "30 < n < 100" е изпълнено). 
#  Списъкът се запълва със случайни числа в интервала 20 до 600. 
#  Да се намери броят на елементите от списъка чиято цифра на единиците е кратна на 2. 
#  Да се намери индекса на минималният елемент от този списък, който има остатък 3 при целочислено делене на 7.
#  Да се създаде втори списък като използва LIST COMPREHENSION и в него да се включат тези числа от първия списък, 
#  които имат цифра на единиците 3 или цифра на десетиците 5. 
#  Да се намери произведението на елементите от списъка с цифри на единиците 3.

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
