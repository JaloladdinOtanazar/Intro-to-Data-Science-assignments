def kwargsAcceptFun(**kwargs):
    print("We got these: ")
    for  name, value in kwargs.items(): 
        print(name, value)
print(kwargsAcceptFun(name = "Jalolbek", surname = "Otanazarov"))

