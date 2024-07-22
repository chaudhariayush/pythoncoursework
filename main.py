
from operation import *
from write import *
from read import *


print("\n")
print("------------------------------------------------------------------------------")
print("\t \t \t welcome to c1")
print("------------------------------------------------------------------------------")
print("\t \t \t Address: BSL contact: 9813180929")
print("------------------------------------------------------------------------------")
print("\n")

dictionary = read_file()
continueLoop = True
while continueLoop == True:
    print("\n")
    print("press 1 to buy from manufacture")
    print("press 2 to sell customer")
    print("press 3 to exit")
    userInput = int(input("press 1, 2 or 3: "))
    if userInput == 1:
        name,phone,today_date_and_time,user_purchased_laptops,VAT,grand_total = buy(dictionary)
        invoice_manufacturer( name,phone,today_date_and_time,user_purchased_laptops,VAT,grand_total)
    elif userInput == 2:
        name,phone,today_date_and_time,user_purchased_laptops,shipping_cost,grand_total = sell(dictionary)
        invoice_customer(name, phone, today_date_and_time, user_purchased_laptops, shipping_cost, grand_total)
    elif userInput == 3:
        continueLoop = False
        print("Thank you for visiting")
    else:
        print("Enter correct option")
