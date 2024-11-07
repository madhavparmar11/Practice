# ques--> wap to initialize different polymorphism functions ?

class order:
    def __init__(self,  item ,price):
        self.item = item
        self.price = price
    
    def __gt__(od1, od2):
        return od1.price>od2.price
        
    def __add__(od1 , od2):
        return od1.price + od2.price
        
        od1=order("chips", 123)
        od2=order("tea", 100)
        print(od1 > od2) #true
        print("total prce is: " od1+od2)
        