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

proizwedenie = 1

for i in range (len(first_list)):
    if i % 2 != 0:
        proizwedenie = proizwedenie * first_list[i]

index_min_value = first_list.index(min(first_list))


razlika = max(second_list) - min(second_list)

print(first_list)
print(f"Proizwedenie = {proizwedenie}")
print(f"Indeksa s minimalna stoinost: {index_min_value}")
print("")
print(second_list)
print(f"Razlika: {razlika}")