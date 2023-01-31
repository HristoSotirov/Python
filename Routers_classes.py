class My_Routers:
    def __init__(self, manufacturer, code_of_product, price, quantity):
        self.manufacturer = manufacturer
        self.code_of_product = code_of_product
        self.price = price
        self.quantity = quantity
 
    def __str__(self):
         return f"{self.manufacturer}, {self.code_of_product}, {self.price}, {self.quantity} \n"
 
    def __repr__(self):
         return f"{self.manufacturer}, {self.code_of_product}, {self.price}, {self.quantity} \n"
 
    def add_router(routers):
        new_manufacturer = str(input("Enter the new manufacturer: "))
        new_code = str(input("Enter the new code: "))
        new_price = float(input("Enter the router price: "))
        new_quantity = int(input("Enter quantity of the product: "))
        new_list = My_Routers(new_manufacturer, new_code, new_price, new_quantity)
        routers.append(new_list)
 
    def price_calc(routers):
        final_price = 0
 
        for router in routers:
            price = router.price
            quantity = router.quantity
 
            price_for_router = (price * 1.20) * quantity
            final_price += price_for_router
 
        price_file = open("price.txt", "w")
        price_file.write(f"The price for all routers is {final_price:.2f}lv.")
        price_file.close()
 
 
routers = [
    My_Routers("Xiaomi Mi Router", "4C", 50, 12),
    My_Routers("Xiaomi Mi Router", "4A", 65.60, 10),
    My_Routers("TP-Link Archer", "C54", 45, 20),
    My_Routers("TP-Link Archer", "C80", 70.20, 8)
]
 
My_Routers.add_router(routers)
My_Routers.price_calc(routers)
print(*routers, )

