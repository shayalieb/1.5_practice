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
            try:
              self.shopping_list.remove(item)
            except:
              print("Item not found.")

    #view the shopping list
    def view_list(self):
            print("\nItems in " + str(self.list_name) + '\n' + 30*'-')
            for item in self.shopping_list:
              print(' - ' + str(item))     

    def merge_lists(self, obj):
        #Create a name fir the new list
        merge_lists_name = "Merged list - " + str(self.list_name) + " + " + str(obj.list_name) 
        #Create empty shopping list object
        merged_list_obj = ShoppingList(merge_lists_name)
        # Add the 1st shopping list item contents to our new list
        merged_list_obj.shopping_list = self.shopping_list.copy()
        # Adding the second shopping list's items to our new list -
        # we're doing this so that there won't be any repeated items
        for item in obj.shopping_list:
                if not item in merged_list_obj.shopping_list:
                     merged_list_obj.shopping_list.append(item)

        #return merged items
        return merged_list_obj             


# Pet store shopping list
pet_store_list = ShoppingList("Pet store shopping list")    
grocery_store_list = ShoppingList('Grocery Store List')   

# List item for pet_store_list
for item in ['Dog food', 'Frisbee', 'Bowl', 'Collars', 'Flea collars']:
     pet_store_list.add_item(item)
# List for grocery items
for item in ['Fruits', 'Veggies', 'Plates', 'Ice pops']:
     grocery_store_list.add_item(item)     

pet_store_list.merge_lists(grocery_store_list)

# Remove an item from the list
# pet_store_list.remove_item("flea collars")

# add a frisbee to the shopping list
# pet_store_list.add_item("frisbee")
merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)
#vie the entire list
merged_list.view_list()