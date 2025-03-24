class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []


    def add_item(self, item_name):
        self.furniture += [item_name]

    def print_inventory(self):

        if len(self.furniture) == 0:
            print(" Inventory empty")
            return
        
        counter = dict()
        
        for item in self.furniture:

            if item in counter:
                counter[item] += 1
            else:
                counter[item] = 1
        
        print(counter)

        inventory = "" 
        
        for item in counter:
            inventory += f"{item}: {counter[item]}, "
        print(inventory)

alice = Villager("Alice", "Koala", "guvnor")

alice.add_item("Desk")

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.print_inventory()

alice.print_inventory()






