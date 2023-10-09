from colorama import Fore, Style

class Crop:
    COST = 0
    def __init__(self, symbol: str,
                 growth_rate: float | int, harvest: int,
                 wilt_rate: float | int, wilted: int,
                 gather_yield: int):
        self.symbol = symbol
        
        self.wilt = 0
        self.wilt_rate = wilt_rate
        self.wilted = wilted
        
        self.growth = 0
        self.growth_rate = growth_rate  
        self.growth_max = harvest
        self.harvestable = False
        
        self.gather_yield = gather_yield
    
    def __str__(self):
        growth = self.growth / self.growth_max
        if growth >= .75:
            return f"{Fore.LIGHTGREEN_EX}{self.symbol}{Style.RESET_ALL}"
        elif growth <= .25:
            return f"{Fore.RED}{self.symbol}{Style.RESET_ALL}"
        else:
            return f"{Fore.BLUE}{self.symbol}{Style.RESET_ALL}"
       
    def harvest(self):
        pass
        
    def wilt(self):
        del self

    def update(self):
        if self.growth == 5:
            self.harvestable = True
            
            if self.wilt == 5:
                self.wilt()
            self.wilt = min(self.wilted, self.wilt + self.wilt_rate)
            self.COST -= 0.1
                
        self.growth = min(self.growth_max, self.growth + self.growth_rate)
        

class Barley(Crop):
    COST = 6.3
    def __init__(self):
        super().__init__(symbol='&', growth_rate=1, harvest=5, wilt_rate=1, wilted=5, gather_yield=4)


class Wheat(Crop):
    COST = 11
    def __init__(self):
        super().__init__(symbol='#', growth_rate=1, harvest=5, wilt_rate=1, wilted=5,  gather_yield=2)


class Ambroshia(Crop):
    COST = 16
    def __init__(self):
        super().__init__(symbol='$', growth_rate=1, harvest=5, wilt_rate=1, wilted=1,  gather_yield=1)
        