class truck():
    def __init__(self,wheels,miles,maker,model,year,sold_on):
        self.wheels = wheels
        self.miles = miles
        self.maker = maker
        self.model = model
        self.year = year
        self.sold_on = sold_on


    def sale_price(self,wheels,sold_on):
        if sold_on:
            print("Already sold, we are sorry")
        print("sale price is %d") %(500 * wheels)

    def purchase_price(self,wheels):
        print("purchase price is %d") %(10000 * wheels)




jumbo = truck(4,100,'tata','a123',2016,True)
jumbo.year
jumbo.maker
jumbo.sale_price(6,True)
jumbo.sale_price(10,False)
jumbo.purchase_price(8)

