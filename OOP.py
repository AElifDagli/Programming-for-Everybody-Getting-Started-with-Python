

# Let’s expand a bit on our Clothing classes from the previous in-video question.
# Your mission: Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material
# that is in stock. When you’re finished, the script should add up to 10 cotton Polo shirts.

class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):                              # constructor method
        material = ""                                      # attribute material
        self.name = name                                   # parameter name

    def add_item(self, name, material, amount):            # defining method add_item
        Clothing.stock['name'].append(self.name)           # creating add_item method,
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):                    # defining method Stock_by_Material
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):                                   # making sub class as shirt in parent class Clothing
    material = "Cotton"                                  # making sub attribute for shirt class


class pants(Clothing):                                   # making sub class as pants in parent class Clothing
    material = "Cotton"                                  # making sub attribute for shirt class

                                        # create a new polo instance of shirt class and set name value
polo = shirt("Polo")                                          # polo: object/instance, shirt: class, 'Polo':name value
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)  # constructorda belirttiğin parametreleri polo objectinde add_item methodunda kullan
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)
