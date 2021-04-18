global categories

categories = {}

class Budget:
    def __init__(self, category):
        categories[category] = categories.get(category,0)
        self.category = category
    
    def depositFunds(self,amount):
        if amount <= 0:
            return print(f'You have entered an invalid amount.\n#{amount} is less than or equal to 0')
            
        categories[self.category] += amount
        return print(f'You have successfully added #{amount} to {self.category}')
        # 

    def withdrawFunds(self,amount):
        if categories[self.category] <= 0:
            return print(f'You have no money to withdraw from. Kindly do a topup')
            
        categories[self.category] -= amount
        return print(f'You have successfully withdrawn #{amount} from {self.category}')
        

    def computBalance(self,category=""):
        category = category if category != "" else self.category
        return print(f'Your balance for {category} is {categories[category]}')
        

    def transferBalance(self,fromCategory,amount,toCategory):
        if categories[fromCategory] <= 0 or categories[fromCategory] - amount < 0:
            return print(f'Balance of {fromCategory} is either 0 or {amount} is more than maximum withdrawal')
        categories[fromCategory] -= amount
        categories[toCategory] += amount
        return print(f'''#{amount} has been successfully transfered to {toCategory} from {fromCategory}\n
        New balance of {fromCategory} is {categories[fromCategory]}\n
        New balance of {toCategory} is {categories[toCategory]}''')
        


def test():
    food = Budget('food')
    clothing = Budget('clothing')
    entertainment = Budget('entertainment')
    football = Budget('football')

    food.depositFunds(50)
    clothing.depositFunds(35)
    entertainment.depositFunds(15)
    football.depositFunds(25)
    

    food.withdrawFunds(20)
    clothing.withdrawFunds(17)
    entertainment.withdrawFunds(13)

    entertainment.computBalance()
    entertainment.computBalance('clothing')
    entertainment.computBalance('football')

    entertainment.transferBalance('clothing',9,'entertainment')


if __name__ == '__main__':
    test()