"""
Activity 08: Halloween Dictionary Practice
File: potion_shop.py

POTION SHOP INVENTORY MANAGER
Keep track of your magical potion ingredients!

Instructions: Complete the function below to practice basic dictionary operations.

Focus: Creating and working with dictionaries
"""

def manage_potion_inventory():
    """
    Create and manage a potion shop inventory.
    
    TODO: Complete this function to:
    1. Create a dictionary called 'inventory' with at least 4 magical ingredients and their quantities:
       Examples: "dragon_scales": 15, "unicorn_hair": 8, "bat_wings": 23, "spider_silk": 12
       (Feel free to use your own creative ingredient names and quantities!)
    
    2. Print "=== Potion Shop Inventory ==="
    
    3. Loop through the dictionary and print each ingredient:
       Format: "[ingredient]: [quantity] units"
       Example: "dragon_scales: 15 units"
    
    4. Add a new ingredient of your choice with a quantity
       Example: "ghost_essence": 6
    
    5. Update an existing ingredient quantity (add some quantity to one you already have)
       Example: Add 5 to "unicorn_hair" so it becomes 13
       Hint: inventory["unicorn_hair"] += 5
    
    6. Print the total number of different ingredients:
       Format: "Total ingredient types: [number]"
    
    7. Return the inventory dictionary
    """
    # Your code here
   

# Test your function (don't modify this part)
if __name__ == "__main__":
    print("Testing potion shop management...")
    result = manage_potion_inventory()
    print(f"\nFinal inventory dictionary: {result}")
    print("Potion shop is ready for business! 🧪")