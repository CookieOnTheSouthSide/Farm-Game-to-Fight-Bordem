from crops import Wheat, Barley, Ambroshia
from random import randint


class Plot:
    def __init__(self, size: str = 'normal'):
        match size:
            case 'medium':
                size = 8
            case 'normal':
                size = 11
            case 'large':
                size = 15
            case 'massive':
                size = 21
            case _:
                size = 5
        self.area = [[Barley() if not randint(0, 10) else 0 for _ in range(size)] for _ in range(size)]
        
    def plant(self, seed: str, location: tuple[int, int] | list[int, int]):
        match seed.lower():
            case 'barley':
                self.area[location[0]][location[1]] = Barley()
            case 'amborshia':
                self.area[location[0]][location[1]] = Ambroshia()
            case 'wheat':
                self.area[location[0]][location[1]] = Wheat()
    
    def harvest(self, location: tuple[int, int] | list[int, int]) -> dict:
        loc = self.area[location[0]][location[1]]
        if loc.harvestable:
            value = {'value': loc.COST, 'yield': loc.gather_yield}
            loc.harvest()
            self.area[location[0]][location[1]] = 0
            return value