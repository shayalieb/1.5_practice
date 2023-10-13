# Shipping list object
class ShoppingList:
    #define the list params
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []
    #add a new item
    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)

    ##remove an item from the list
    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item) 

    #view the shopping list
    def view_list(self):
        for item in self.shopping_list:
            print(item)                  

# Pet store shopping list
pet_store_list = ShoppingList("Pet store shopping list")       

# List item for pet_store_list
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Remove an item from the list
pet_store_list.remove_item("flea collars")

# add a frisbee to the shopping list
pet_store_list.add_item("frisbee")

#vie the entire list
pet_store_list.view_list()