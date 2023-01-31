#  Програма в която се съсдавт 2 спъка. Въвеждат се числата N и K. След това от потребителя се въвеждат толкова числа колкото е стойноста на N.
#  Въведените числа по-големи от К се включват към първи списък, а тези по-малки от К и по-големи от 0 се включват към втори списък.
#  Създават се методи за намиране на произведението на нечетните числата от първи списък, индекса на елемента с минимална стойност 
#  от първи списък и разликата от най-големия и най-малкия елемент от втори списък.

first_list = []
second_list = []

while True:
    try:
        n=int(input('Enter N:'))
        if n<0:
            raise Exception
        break
    except ValueError:
        print("Wrong input. Try again.")
    except Exception:
        print("Sorry, no numbers below zero")

while True:
    try:
        k=int(input('Enter K:'))
        if k<0:
            raise ValueError
        break
    except ValueError:
        print("Sorry, no numbers below zero")

for i in range(n):
    x = float(input(f"X{i+1} = "))
    if x > k:
        first_list.append(x)
    elif x <= k and x > 0:
        second_list.append(x)

product = 1

for i in range (len(first_list)):
    if i % 2 != 0:
        product *= first_list[i]

index_min_value = first_list.index(min(first_list))


difference = max(second_list) - min(second_list)

print(first_list)
print(f"Product = {product}")
print(f"Index with minimal value: {index_min_value}")
print("")
print(second_list)
print(f"Difference: {difference}")
