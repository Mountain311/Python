a={"c_price":0,"s_price":0,"inventory":0}

def PROFIT(d):
    profit=(float((a["s_price"])-float(a["c_price"]))*float(a["inventory"]))
    print("Total Profit Earned in Dollars = $",int(profit))
    

a={"c_price":0,"s_price":0,"inventory":0}

a["c_price"]=input("Enter Cost Price of Product in Dollars = $")
a["s_price"]=input("Enter Selling Price of Product in Dollars = $")
a["inventory"]=input("Enter Inventory of Product =")

PROFIT(a)