class MenuItem:
    def __init__(self, name, description, price, category):
        self.__id = MenuItem.__generate_id()
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    __id_counter = 1

    @classmethod
    def __generate_id(cls):
        id_ = cls.__id_counter
        cls.__id_counter += 1
        return id_

    def get_id(self):
        return self.__id

    def update(self, name=None, description=None, price=None, category=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price
        if category:
            self.category = category

    def display(self):
        return f"ID: {self.get_id()}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}, Category: {self.category}"

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def update_item(self, item_id, name=None, description=None, price=None, category=None):
        for item in self.items:
            if item.get_id() == item_id:
                item.update(name, description, price, category)
                return f"Item ID {item_id} updated."
        return f"Item ID {item_id} not found."

    def remove_item(self, item_id):
        for item in self.items:
            if item.get_id() == item_id:
                self.items.remove(item)
                return f"Item ID {item_id} removed."
        return f"Item ID {item_id} not found."

    def display_menu(self):
        for item in self.items:
            print(item.display())

class FoodItem(MenuItem):
    def __init__(self, name, description, price, category, is_vegetarian=False):
        super().__init__(name, description, price, category)
        self.is_vegetarian = is_vegetarian

    def display(self):
        vegetarian_status = "Vegetarian" if self.is_vegetarian else "Non-Vegetarian"
        return f"{super().display()}, {vegetarian_status}"

class BeverageItem(MenuItem):
    def __init__(self, name, description, price, category, is_alcoholic=False):
        super().__init__(name, description, price, category)
        self.is_alcoholic = is_alcoholic

    def display(self):
        alcoholic_status = "Alcoholic" if self.is_alcoholic else "Non-Alcoholic"
        return f"{super().display()}, {alcoholic_status}"

# Test the Restaurant Management System

# Create a Menu instance
menu = Menu()

# Create FoodItem instances
food1 = FoodItem(name="Burger", description="A delicious beef burger", price=8.99, category="Main Course", is_vegetarian=False)
food2 = FoodItem(name="Salad", description="A fresh garden salad", price=4.99, category="Appetizer", is_vegetarian=True)

# Create BeverageItem instances
beverage1 = BeverageItem(name="Coke", description="Chilled Coca-Cola", price=1.99, category="Soft Drink", is_alcoholic=False)
beverage2 = BeverageItem(name="Beer", description="Craft beer", price=5.99, category="Alcohol", is_alcoholic=True)

# Add items to the menu
menu.add_item(food1)
menu.add_item(food2)
menu.add_item(beverage1)
menu.add_item(beverage2)

# Display the menu
print("Initial Menu:")
menu.display_menu()

# Update an item
print("\nUpdating Item ID 1...")
menu.update_item(1, price=9.99)

# Remove an item
print("\nRemoving Item ID 3...")
menu.remove_item(3)

# Display the updated menu
print("\nUpdated Menu:")
menu.display_menu()
