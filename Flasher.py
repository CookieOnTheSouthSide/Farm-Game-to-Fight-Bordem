import pickle
from plot import Plot
from crops import Barley, Wheat, Ambroshia
from colorama import Fore, Style

from sys import exit

BASIC_PLOTS = [0]


class Garden:
    SEED_SHOP = {"Barley": Barley, "Wheat": Wheat, "Ambroshia": Ambroshia}
    
    def __init__(self):
        self.day = 0
        self.inventory = {"Agronomy Sack": {"Wheat": 0}, "Seed Pouch": {"Wheat": 2}, "Gold": 50}
        self.harvest_efficeny = 0.5
        self.plots = {'0': Plot(size='small')}
        
    # Print the inv
    def print_inv(self) -> None:
        self.barrier()
        for key in self.inventory:
            print(f"{key}: {self.inventory[key]}")
        self.barrier()
        
    # Move onto next day
    def sleep(self):
        self.barrier()
        self.day += 1
        self.barrier()
        
    # Saving and Loading the Game from a save file. Going to be a file for cross compatbility. Login system too.
    def save(self) -> None:
        pass
    
    def load(self) -> None:
        pass
    
    # QOL functions
    @staticmethod
    def barrier() -> None:
        print("-----------------------------------------------")
        
    @staticmethod
    def error_message() -> None:
        print(f"{Fore.RED}\nEnter a valid option!{Style.RESET_ALL}")
        
    # Main Functions
    def choose_action(self) -> None:
        while True:
            choice = input("0) See Plot Numbers\n1) View Plot\n2) View Inventory\n3) Buy Plot\n4) Move To Next Day\n5) Save\n6) View Map Key\n7) Quit\nEnter the number of what you want to do: ")
            match choice:
                case '0':
                    self.view_plots()
                case '1':
                    self.view_plot()
                case '2':
                    self.print_inv()
                case '3':
                    self.buy_plot()
                case '4':
                    self.sleep()
                case '5':
                    self.save()
                case '6':
                    self.view_key()
                case '7':
                    match input("Are you sure (y or no): ").lower():
                        case 'y':
                            exit()
                case _:
                    self.error_message()
                    continue
            break
        
    def buy_plot(self) -> None:
        while True:
            plot_num = input("Enter the plot number you want to buy: ")
            if not (plot_num in [key for key in self.plots]):
                self.error_message()
                continue
            break
        plot_size = input("Enter the size of the plot you want (Plot Sizes: Small, Medium, Normal, Large, Massive): ")
        self.plots.update({str(plot_num): Plot(size=plot_size.lower())})
    
    def buy_seed(self) -> None:
        print("Seed Types: "+ (key + ', ' for key in self.SEED_SHOP))
        match input("Enter the seed you want to buy: "):
            case ''
        while True:
            amount = input("Enter the amount of seeds you want to buy: ")
            if 
     
    def view_plots(self):
        self.barrier()
        for key in self.plots:
            print(f"Plot {key}")
        self.barrier()
       
    def view_plot(self) -> None:
        while True:
            plot_num = input("Enter the plot # you want to view: ")
            match self.plots.get(plot_num):
                case None:
                    self.error_message()
                    continue
            break
        
        self.barrier()
        print(f"Garden Plot {plot_num}:")
        for row in self.plots[plot_num].area:
            for crop in row:
                print(str(crop), end=' ')
            print()
        self.barrier()
     
    def update(self):
        for key in self.plots:
            for row in self.plots[key].area:
                for item in row:
                    if not (item in BASIC_PLOTS):
                        item.update()
                    
    def day_message(self):
        print(f"Day: {self.day}")
        

# Main gameplay loop
def main():
    garden = Garden()
    
    # Print the Lore And Contorl guide
    

    # Main Game loop
    while True:
        garden.day_message()
        garden.choose_action()
        garden.update()
            
if __name__ == '__main__':
    main()
    
