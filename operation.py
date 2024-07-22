from datetime import datetime
def buy(dictionary):
    print("thank you for buying")
    print("\n")
    print("---------------------------------------------------------------------------------")
    print("for bill generation you have to enter your details first: ")
    print("---------------------------------------------------------------------------------")
    print("\n")
    name = input("enter your name: ")
    print("---------------------------------------------------------------------------------")
    phone = input("enter your phone number: ")
    print("---------------------------------------------------------------------------------")
    print("S.N. \t Name \t \t \t Brand \t \t Quantity \t price \t \t processor \t \t graphic card \t")
    a=1
    file = open("laptop.txt","r")
    for line in file:
        print(a,"\t "+line.replace(",","\t"))
        a+=1
    file.close()

    print("\n")
    valid_id = int(input("please provide the id of the laptop you want to buy: "))
    print("\n")

    #valid ID
    while valid_id <= 0 or valid_id > len(dictionary):
        print("please provide a valid laptop ID !!!")
        print("\n")
        valid_id = int(input("please provide the id of the laptop you want to buy: "))
        
        print("\n")
        
    #valid quantity
    user_quantity = int(input("please provide the quantity of laptop you want to buy: "))
    get_quantity = dictionary[valid_id][3]
    while user_quantity <= 0 or user_quantity > int(get_quantity):
        print("dear admin the quantity you looking for is not avilable in our shop. please look again")
        print("\n")
        user_quantity = int(input("please provide the quantity of the laptop you want to buy: "))
    print("\n")

    #update the text file
    dictionary[valid_id][3] = int(dictionary[valid_id][3])+int(user_quantity)
        
    file = open("laptop.txt","w")
    for values in dictionary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close

    #getting user purchased items
    nameofproduct = dictionary[valid_id][0]
    quantity = user_quantity
    unit_price = dictionary[valid_id][2]
    unit_price_item = dictionary[valid_id][2].replace("$",'')
    final_price = int(unit_price_item)*int(quantity)


    user_purchased_laptops = []
    user_purchased_laptops.append([nameofproduct, quantity , unit_price, final_price])
    
    total = 0
    VAT = 0.13*(final_price)
    for i in user_purchased_laptops:
        total += int(i[3])
    total_price = final_price + VAT

    today_date_and_time = datetime.now()
    
            

    print("\n")
    print("\t \t \t \t laptop shop bill ")
    print("\n")
    print("\t \t kamalpokhari, kathamandu | phone no: 9813180929 ")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------")
    print("Laptop Details are: ")
    print("----------------------------------------------------------------------------------------------------------")
    print("Name of the custumer:"+ str(name))
    print("contact no:"+ str(phone))
    print("date and time of purchased: "+str(today_date_and_time))
    print("------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("purchased details are:")
    print("------------------------------------------------------------------------------------------------------------")
    print("Item Name \t \t \t total quantity \t \t unit price \t \t \t total")
    print("-------------------------------------------------------------------------------------------------------------")
    for i in user_purchased_laptops:
        print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
        print("----------------------------------------------------------------------------------------------------------")
        
        print("your Vat Amount is:", VAT)
        print("grand_total: $"+str(total_price))
        print("note: Vat Amount is added to the grand total")
    
    return name,phone,today_date_and_time,user_purchased_laptops,VAT,total_price


def sell(dictionary):
    print("thank you for selling")
    print("\n")
    print("--------------------------------------------------------------------")
    print("for bill generation you will have to enter your details firstL: ")
    print("----------------------------------------------------------------------")
    print("\n")
    name = input("enter your name: ")
    print("-----------------------------------------------------------------------")
    phone = input("enter your phone number: ")
    print("--------------------------------------------------------------------------")
    print("S.N. \t Name \t \t \t Brand \t \t Quantity \t price \t \t processor \t \t graphic card \t")
    a=1
    file = open("laptop.txt","r")
    for line in file:
            print(a,"\t "+line.replace(",","\t"))
            a+=1
    file.close()

    print("\n")
    valid_id = 0
    try:
        valid_id = int(input("please provide the id of the laptop you want to buy: "))
    except:
        print("Enter a valid id")
    print("\n")

    #valid ID
    user_quantity = 0
    while valid_id <= 0 or valid_id > len( dictionary):
        print("please provide a valid laptop ID !!!")
        print("\n")
        try:
            valid_id = int(input("please provide the id of the laptop you want to buy: "))
            user_quantity= int(input("please provide the quantity of laptop you want to buy: "))
            break
        except:
            print("Enter a valid id")
            print("\n")

    #valid quantity
    get_quantity = dictionary[valid_id][3]
    while user_quantity <= 0 or user_quantity > int(get_quantity):
        print("dear admin the quantity you looking for is not avilable in our shop. please look again")
        print("\n")
        try:
            user_quantity = int(input("please provide the quantity of the laptop you want to buy: "))
            break
        except:
            print("enter a valid id")
        print("\n")

    #update the text file
    dictionary[valid_id][3] = int(dictionary[valid_id][3])+int(user_quantity)
        
    file = open("laptop.txt","w")
    for values in dictionary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close

    #getting user purchased items
    nameofproduct = dictionary[valid_id][0]
    quantity = user_quantity
    unit_price = dictionary[valid_id][2]
    unit_price_item = dictionary[valid_id][2].replace("$",'')
    final_price = int(unit_price_item)*int(quantity)
    
    user_purchased_laptops = []
    user_purchased_laptops.append([nameofproduct, quantity, unit_price, final_price])
    shipping_cost = input("dear user do you want your laptop to be shipped ? (Y/N)")

    today_date_and_time = datetime.now()

    #print bill onscreen
    print("\n")
    print("\t \t \t \t laptop shop bill ")
    print("\n")
    print("\t \t kamalpokhari, kathamandu | phone no: 9813180929 ")
    print("\n")
    print("----------------------------------------------------------------------------------------------------------")
    print("Laptop Details are: ")
    print("----------------------------------------------------------------------------------------------------------")
    print("Name of the custumer:"+ str(name))
    print("contact no:"+ str(phone))
    print("date and time of purchased: "+str(today_date_and_time))
    print("------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("purchased details are:")
    print("------------------------------------------------------------------------------------------------------------")
    print("Item Name \t \t \t total quantity \t \t unit price \t \t \t total")
    print("-------------------------------------------------------------------------------------------------------------")
    for i in user_purchased_laptops:
        print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
        print("----------------------------------------------------------------------------------------------------------")

    if shipping_cost=="Y":
        total = 0
        shipping_cost = 500
        for i in user_purchased_laptops:
            total+=int(i[3])
            grand_total = total + shipping_cost
        if shipping_cost:
            print("your shipping cost is:",shipping_cost)
            print("grand_total: $"+str(grand_total))
            print("note: shipping cost is added to the grand total")
        else:
            print("grand total: $"+str(grand_total))
    return name,phone,today_date_and_time,user_purchased_laptops,shipping_cost,grand_total




