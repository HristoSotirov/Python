#  Програма, в която се създава клас Телефони с 3 инстанции на класа. 
#  Създават се методи за сортиране по цена и година.
#  Резултатите се записват във файл Phones_file.

import os

class phone:
  def __init__(self, phone_brand, phone_model, phone_year, phone_color, phone_price):
    self.phone_brand = phone_brand
    self.phone_model = phone_model
    self.phone_year = phone_year
    self.phone_color = phone_color
    self.phone_price = phone_price
  def __str__(self): 
    return f' {self.phone_brand}, {self.phone_model}, {self.phone_year}, {self.phone_color}, {self.phone_price} '
  def __repr__(self): 
    return f' {self.phone_brand}, {self.phone_model}, {self.phone_year}, {self.phone_color}, {self.phone_price} '

phones = [
  phone("iPhone", "11 Pro", 2021, "white", 2000),
  phone("Samsung", "Galaxy", 2020, "black", 1800),
  phone("Huawei", "P20", 2019, "blue", 1600)
]


print("Phones sorted by price:")
def price(phone_price):
    return sorted(phone_price, key = lambda x: x.phone_price, reverse = True)
print(*price(phones), sep = '\n')

print("\nPhones sorted by year:")
def last_modele(phone_year):
    return sorted(phone_year, key = lambda x: x.phone_year, reverse = False)
print(*last_modele(phones), sep = '\n')

file = open("Phones_file", "x")
file.write(str(price(phones)))
file.write(str(last_modele(phones)))
file.close()
os.remove("Phones_file.txt")
