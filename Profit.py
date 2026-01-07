costprice =int(input("enter the cp: "))
sellingprice =int(input("enter the sp: "))
pt=sellingprice-costprice

if(sellingprice>costprice):
    print(pt,"profit")
else :
    print(pt,"No profit")