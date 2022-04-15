from datetime import date


class Llama:
    def __init__(self, chip_num, name, species, food):
        self.chip_number = chip_num
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
