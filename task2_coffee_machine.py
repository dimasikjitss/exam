class CoffeeMachine():
    def __init__(self, milk, coffee, sugar):
        self.milk = milk
        self.coffee = coffee
        self.sugar = sugar

  
    def make_coffee(self):
        self.m = int(input("Enter the amount of milk (ml): "))
        self.c = int(input("Enter the amount of coffe (gr): "))
        self.s = int(input("Enter the amount of milk (gr): "))
        print('Your coffee is ready')

    def __subtract_milk(self):
        if self.milk - self.m > 0:
            return             
        else:
            milk_ml= self.m - self.milk
            print('Need to buy milk '+ str(milk_ml)+ ' ml')

    def __subtract_coffee(self):
        if self.coffee - self.c > 0:
            return 
        else:
            coffee_gr= self.c - self.coffee
            print('Need to buy coffee '+ str(coffee_gr)+ ' gr')

    def __subtract_sugar(self):
        if self.sugar - self.s > 0:
            return             
        else:
            sugar_gr= self.s - self.sugar
            print('Need to buy sugar '+ str(sugar_gr)+ ' gr')

if __name__ == "__main__":
    C = CoffeeMachine(
        1000 , 1000, 1000
    )
    C.make_coffee()
    C._CoffeeMachine__subtract_milk()
    C._CoffeeMachine__subtract_coffee()
    C._CoffeeMachine__subtract_sugar()

