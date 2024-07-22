from datetime import datetime

#for welcome message

print("\n")
print("------------------------------------------------------------------------------")
print("\t \t \t welcome to c1")
print("------------------------------------------------------------------------------")
print("\t \t \t Address: BSL contact: 9813180929")
print("------------------------------------------------------------------------------")
print("\n")

file = open("laptop.txt","r")
#laptopkoid = 1
idoflaptop = 1
dictionary={}
for line in file:
    line = line.replace("\n","")
    #merodict[idoflaptop]] = line.split(",")
    dictionary.update({idoflaptop:line.split(",")})
    #print(line.split(","))
    idoflaptop+=1
file.close()

#print(dictionary)
continueLoop = True
while continueLoop == True:
    print("\n")
    print("press 1 to buy from manufacture")
    print("press 2 to sell customer")
    print("press 3 to exit")
    userinput = int(input("press 1, 2 or 3: "))

    if userinput == 1:
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
        print("S.N. \t Name \t \t Brand \t \t Quantity \t price \t \t processor \t \t graphic card \t")
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
        #user_quantity = int(input(enter the quantity))
        
    elif userinput == 2:
        print("thank you for selling")
        print("\n")
        print("--------------------------------------------------------------------")
        print("for bill generation you will have to enter your details first: ")
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
        valid_id = int(input("please provide the id of the laptop you want to buy: "))
        print("\n")

        #valid ID
        while valid_id <= 0 or valid_id > len(dictionary):
            print("please provide a valid laptop ID !!!")
            print("\n")
            valid_id = int(input("please provide the id of the laptop you want to buy: "))
        user_quantity= int(input("please provide the quantity of laptop you want to buy: "))
        print("\n")

        #valid quantity
        get_quantity = dictionary[valid_id][3]
        while user_quantity <= 0 or user_quantity > int(get_quantity):
            print("dear admin the quantity you looking for is not avilable in our shop. please look again")
            print("\n")
            user_quantity = int(input("please provide the quantity of the laptop you want to buy: "))
        print("\n")

        #update the text file
        dictionary[valid_id][3] = int(dictionary[valid_id][3])-int(user_quantity)
        
        file = open("laptop.txt","w")
        for values in dictionary.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
            file.write("\n")
        file.close

        #getting user purchased items
        nameofproduct = dictionary[valid_id][0]
        quantity = user_quantity
        #unit_price_eutako = merodict[valid_id][2]
        unit_price = dictionary[valid_id][2]

        #price_of_itemkunai_eutako = merodict[valid_id][2].replace("$",'')
        unit_price_item = dictionary[valid_id][2].replace("$",'')
        #jammaprice = int(price_of_itemkunai_eutako)*int(quantity_userle_deko)
        final_price = int(unit_price_item)*int(quantity)

        user_purchased_laptops = []
        user_purchased_laptops.append([nameofproduct, quantity, unit_price, final_price])

        shipping_cost = input("dear user do you want your laptop to be shipped ? (Y/N)")

        if shipping_cost=="Y":
            total = 0
            shipping_cost = 500
            for i in user_purchased_laptops:
                total+=int(i[3])
            grand_total = total + shipping_cost
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
            if shipping_cost:
                print("your shipping cost is:",shipping_cost)
                print("grand_total: $"+str(grand_total))
                print("note: shipping cost is added to the grand total")
            else:
                print("grand total: $"+str(grand_total))

            #today_date-and_time=datetime.now()
            with open(str(name)+str(phone)+".txt","w")as file:
                file.write("\n")
                file.write("\t \t \t \t laptop shop bill ")
                file.write("\n")
                file.write("\t \t kamalpokhari, kathamandu | phone no: 9813180929 ")
                file.write("\n")
                file.write("----------------------------------------------------------------------------------------------------------")
                file.write("Laptop Details are: ")
                file.write("----------------------------------------------------------------------------------------------------------")
                file.write("Name of the custumer:"+ str(name))
                file.write("contact no:"+ str(phone))
                file.write("date and time of purchased: "+str(today_date_and_time))
                file.write("------------------------------------------------------------------------------------------------------------")
                file.write("\n")
                file.write("purchased details are:")
                file.write("------------------------------------------------------------------------------------------------------------")
                file.write("Item Name \t \t total quantity \t \t unit price \t \t total")
                file.write("-------------------------------------------------------------------------------------------------------------")
                for i in user_purchased_laptops:
                    file.write(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+"$"+str(i[3]))
                file.write("----------------------------------------------------------------------------------------------------------")
                file.write("\n")
                if shipping_cost:
                    file.write("your shipping cost is:"+""+str(shipping_cost)+"\n")
                    file.write("\n")
                    file.write("grand_total: $"+str(grand_total))
                    file.write("\n")
                    file.write("***note: shipping cost is added to the grand total***"+"\n")
                else:
                    file.write("grand total: $"+str(grand_total))
        else:
            total = 0
            shipping_cost = 0
            for i in user_purchased_laptops:
                total+=int(i[3])
            grand_total = total + shipping_cost
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
            if shipping_cost:
                print("your shipping cost is:",shipping_cost)
                print("grand_total: $"+str(grand_total))
                print("note: shipping cost is added to the grand total")
            else:
                print("grand total: $"+str(grand_total))

            #today_date_and_time=datetime.now()
            with open(str(name)+str(phone)+".txt","w")as file:
                file.write("\n")
                file.write("\t \t \t \t laptop shop bill ")
                file.write("\n")
                file.write("\t \t kamalpokhari, kathamandu | phone no: 9813180929 ")
                file.write("\n")
                file.write("----------------------------------------------------------------------------------------------------------")
                file.write("Laptop Details are: ")
                file.write("----------------------------------------------------------------------------------------------------------")
                file.write("Name of the custumer:"+ str(name))
                file.write("contact no:"+ str(phone))
                file.write("date and time of purchased: "+str(today_date_and_time))
                file.write("------------------------------------------------------------------------------------------------------------")
                file.write("\n")
                file.write("purchased details are:")
                file.write("------------------------------------------------------------------------------------------------------------")
                file.write("Item Name \t \t total quantity \t \t unit price \t \t total")
                file.write("-------------------------------------------------------------------------------------------------------------")
                for i in user_purchased_laptops:
                    file.write(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+"$"+str(i[3]))
                file.write("----------------------------------------------------------------------------------------------------------")
                file.write("\n")
                if shipping_cost:
                    file.write("your shipping cost is:"+""+str(shipping_cost)+"\n")
                    file.write("\n")
                    file.write("grand_total: $"+str(grand_total))
                    file.write("\n")
                    file.write("***note: shipping cost is added to the grand total***"+"\n")
                else:
                    file.write("grand total: $"+str(grand_total))
            
                 
    elif userinput == 3:
        continueLoop = False
    else:
        print("enter correct option")


