"""
Activity 08 - File 2: Inventory Manager
Difficulty: Intermediate
Focus: Dictionary methods (keys, values, items, pop)
Estimated Time: 10-12 minutes

Complete the TODO comments below to create an inventory management system.
"""

def create_initial_inventory():
    """
    Create and return an initial inventory dictionary.
    
    TODO: Create a dictionary with the following items and quantities:
    - "apples": 50
    - "bananas": 30
    - "oranges": 25
    - "grapes": 40
    - "strawberries": 15
    """
    # Your code here
    inventory = {}
    
    return inventory

def display_all_items(inventory):
    """
    Display all items in the inventory.
    
    TODO: Use the .keys() method to get all item names and print each one
    Print in the format: "Available items: apple, banana, orange, ..."
    """
    # Your code here
    pass

def display_all_quantities(inventory):
    """
    Display all quantities in the inventory.
    
    TODO: Use the .values() method to get all quantities
    Print the total number of items and the sum of all quantities
    """
    # Your code here
    pass

def display_inventory_details(inventory):
    """
    Display detailed inventory information.
    
    TODO: Use the .items() method to loop through the inventory
    Print each item in the format: "[item]: [quantity] units"
    """
    # Your code here
    pass

def add_new_item(inventory, item_name, quantity):
    """
    Add a new item to the inventory.
    
    TODO: Add the new item with its quantity to the inventory dictionary
    If the item already exists, add to the existing quantity
    """
    # Your code here
    pass

def sell_item(inventory, item_name, quantity_sold):
    """
    Remove items from inventory when sold.
    
    TODO: Check if the item exists and has enough quantity
    If yes, subtract the quantity_sold from the inventory
    If not enough quantity, print an appropriate message
    Return True if sale was successful, False otherwise
    """
    # Your code here
    return False

def remove_item_completely(inventory, item_name):
    """
    Remove an item completely from the inventory.
    
    TODO: Use the .pop() method to remove the item from inventory
    Return the quantity that was removed, or 0 if item didn't exist
    """
    # Your code here
    return 0

def find_low_stock_items(inventory, threshold=20):
    """
    Find items with stock below the threshold.
    
    TODO: Loop through the inventory and find items with quantity <= threshold
    Return a list of item names that need restocking
    """
    # Your code here
    low_stock = []
    
    return low_stock

# Test your functions (don't modify this part)
if __name__ == "__main__":
    print("=== Inventory Management System ===")
    
    # Test creating initial inventory
    print("1. Creating initial inventory...")
    inventory = create_initial_inventory()
    print(f"Initial inventory: {inventory}")
    
    # Test displaying all items
    print("\n2. Displaying all items...")
    display_all_items(inventory)
    
    # Test displaying quantities
    print("\n3. Displaying all quantities...")
    display_all_quantities(inventory)
    
    # Test displaying detailed inventory
    print("\n4. Displaying inventory details...")
    display_inventory_details(inventory)
    
    # Test adding new item
    print("\n5. Adding new item...")
    add_new_item(inventory, "pears", 35)
    add_new_item(inventory, "apples", 10)  # Add to existing
    print(f"Inventory after additions: {inventory}")
    
    # Test selling items
    print("\n6. Testing sales...")
    success1 = sell_item(inventory, "bananas", 15)
    success2 = sell_item(inventory, "grapes", 50)  # Not enough stock
    print(f"Sale 1 successful: {success1}")
    print(f"Sale 2 successful: {success2}")
    print(f"Inventory after sales: {inventory}")
    
    # Test removing item completely
    print("\n7. Removing strawberries completely...")
    removed_qty = remove_item_completely(inventory, "strawberries")
    print(f"Removed {removed_qty} strawberries")
    print(f"Inventory after removal: {inventory}")
    
    # Test finding low stock items
    print("\n8. Finding low stock items...")
    low_stock = find_low_stock_items(inventory, 20)
    print(f"Items needing restock: {low_stock}")
    
    print("\n=== All tests completed! ===")