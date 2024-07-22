def read_file():    
    file = open("laptop.txt","r")
    idoflaptop = 1
    dictionary={}
    for line in file:
        line = line.replace("\n","")
        #dictionary[idoflaptop] = line.split(",")
        dictionary.update({idoflaptop:line.split(",")})
        #print(line.split(","))
        idoflaptop+=1
    file.close()
    return dictionary