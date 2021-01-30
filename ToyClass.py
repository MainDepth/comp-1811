class toys:
    def __init__(self, name, image, price, stock,category):
        self.name=name
        self.image=image
        self.price=float(price)
        self.stock=int(stock)
        self.category=str(category)

    def Stock(self):
        stockLevel=str()
        if(self.stock<=0):
            stockLevel=f"'Out Of Stock'"
        elif(self.stock<=20):
            stockLevel=f"'Low Stock'"
        else:
            stockLevel=f"'In Stock'"
        return stockLevel


    def getName(self):
        return self.name

    def getImage(self):
        return self.image

    def getPrice(self):
        return self.price

    def getStock(self):
        return self.Stock()

    def getCategory(self):
        return self.category

    def getInfo(self):
        list=[]

        name=self.name
        image=self.image
        price=self.price
        stock=self.stock

        list.extend([name,image,price, stock])
        return list

