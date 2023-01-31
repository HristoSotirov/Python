import random

while True:
    try:
        n = int(input("N = "))
        if n < 30 or n > 100:
            raise Exception
        break
    except ValueError:
        print("Грешен символ! Опитай пак!")
    except  Exception:
        print("Числото трчбва да е в интервала [30, 100]!")

first_list = [] 

for i in range(n):
    x = random.randint(20,600)
    first_list.append(x)

print(first_list)

count = 0
for i in first_list:
    if (i % 10) % 2 == 0:
        count += 1
print(f"Броя на елементите кратни на [2] : {count}")

min_value_index = first_list.index(min ([num for num in first_list if num % 7 ==3]))
print(f"Индекса на елемента с минимална стойност: {min_value_index}")

second_list = [i for i in first_list if i // 100 == 3 or i // 10 % 10 == 5]
print(second_list)

max_value_index = second_list.index(max(second_list))
print(f"Индекса на елемента с максимална стойност: {max_value_index}")

product = 1
for i in second_list:
    if i % 10 == 3:
        product *= i
print(f"Произведението на елементите с цифра на единиците [3] : {product}")