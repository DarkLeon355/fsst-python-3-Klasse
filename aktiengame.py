import random
import matplotlib.pyplot as plt
import numpy as np


class Player():
    def __init__(self, name, money, depot):
        self.name = name
        self.money = money
        self.depot = depot
    def __str__(self):
        return (f"{self.name} currently has {self.money} dollars and holds these stocks {self.depot}")
    

class Stock():
    def __init__(self, name, current_value):
        self.name = name
        self.current_value = current_value
        
        
class Low_Risk_Stock(Stock):
    
    def __init__(self,current_value, name):
        super().__init__(current_value, name)
        self.current_value = current_value
        self.name = name
        self.chart = [self.current_value]
    def update_current_value(self):
        self.chance = random.randint(1, 11)
        
        if 1 <= self.chance <= 6:
            self.current_value = self.current_value * 1.05
            
        if 7 <= self.chance <= 8:
            self.current_value = self.current_value * 0.98
            
        if 9 <= self.chance <= 10:
            self.current_value = self.current_value
        
        self.chart.append(self.current_value)
            
        return
        
        

class Med_Risk_Stock(Stock):
    def __init__(self, current_value, name):
        super().__init__(current_value, name)
        self.current_value = current_value
        self.name = name
        self.chart = [self.current_value]
    def update_current_value(self):
        self.chance = random.randint(0, 10)
        
        if self.chance < 5:
            self.current_value *= 1.1
            
        elif self.chance > 5:
            self.current_value *= 0.9
            
        elif self.chance == 5:
            self.current_value = self.current_value
            
        self.chart.append(self.current_value)
            
        return


class High_Risk_Stock(Stock):
    
    def __init__(self,current_value, name):
        super().__init__(current_value, name)
        self.current_value = current_value     
        self.name = name
        self.chart = [self.current_value]
    
    def update_current_value(self):
        self.chance = random.randint(1,11)
        
        if(self.chance <= 2):
            self.current_value = self.current_value * 1.25
            
        if(self.chance > 2 or self.chance < 9):
            self.current_value = self.current_value * 0.92
            
        if(self.chance >= 9):
             self.current_value = self.current_value
             
        self.chart.append(self.current_value)
        return




def Buy(Player1):
    global stocks
    c = 0
    print(f"\nWhat Stock do you want to buy?  exit = enter")
    while c < len(stocks):
        print(f"{c+1}. {stocks[c].name} currently valued at {round(stocks[c].current_value, 2)}$")
        c = c + 1
    try:
        b = int(input())
    except:
        return 0
    if  (Player1.money >= stocks[b-1].current_value):
        Player1.depot.append(stocks[b-1])
        Player1.money = Player1.money - stocks[b-1].current_value
    else:
        print("You are too Poor!")
        return 0
    

def daycycle():
    global stocks
    global days
    global day
    stocks[0].update_current_value()
    stocks[1].update_current_value()
    stocks[2].update_current_value()
    day = day+1
    days.append(day)

def Stats(Player1):
    total = 0
    print("\nYour depot currently holds:")
    for x in Player1.depot:
        print(f"   -One Share of {x.name} currently valued at {round(x.current_value, 2)}$")
        total = total + x.current_value
    print(f"Your portfolio values at {round(total, 2)}$")
    print(f"Your Money equals {Player1.money}$\n")
    
def Sell(Player1):
    print("Your Portfolio currently holds the following Stocks, which one would you like to sell?")
    c = 1
    while (c-1) < len(Player1.depot):
        print(f"{c} - One Stock of {Player1.depot[c-1].name} currently valued at {round(Player1.depot[c-1].current_value, 2)}")
        c = c + 1
    ui = int(input())
    Player1.money = Player1.money + Player1.depot[ui-1].current_value
    Player1.depot.remove(Player1.depot[ui-1])

def charts():
    global stocks
    global days
    c = 0
    print(f"\nWhat Chart do you want to see?")
    while c < len(stocks):
        print(f"{c+1}. {stocks[c].name}")
        c = c + 1
    try:
        ui = int(input())
    except:
        return 0
    plt.plot(days, stocks[ui-1].chart)
    plt.axis((0, (len(days)-1), 0, 20000))
    print(days)
    plt.show()
    

    

def Menu(Player1):
    global stocks
    print(f"\n1-Buy\n2-Sell\n3-Statistics\n4-Charts\n5-Sleep\n")
    i = int(input())
    if (i == 1):
        Buy(Player1)
    elif (i == 2):
        Sell(Player1)
    elif (i == 3):
        Stats(Player1)
    elif (i == 4):
        charts()
    elif (i == 5):
        daycycle()
   

pname = str(input(f"Please type in your Name: \n"))
depot = []
Player1 = Player(pname, 20000, depot)
stocks = []
day = 0
days = [0]
Apple = Low_Risk_Stock(random.randint(5000, 12000), "Apple")
Tesla = Med_Risk_Stock(random.randint(2000, 6500), "Tesla")
Shell = High_Risk_Stock(random.randint(1000, 2500), "Shell")
stocks.append(Apple)
stocks.append(Tesla)
stocks.append(Shell)
while(True):
    Menu(Player1)

